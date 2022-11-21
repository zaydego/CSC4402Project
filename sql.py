import sqlite3
import pandas as pd
import for_pandas

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    c.execute(create_table_sql)

def insert_to_table(conn, insert_into):
    c = conn.cursor()
    c.execute(insert_into)
    conn.commit()


def main():
    users = """CREATE TABLE IF NOT EXISTS Users (
                User_ID integer PRIMARY KEY,
                Email text NOT NULL,
                First_Name text NOT NULL,
                Last_Name text NOT NULL,
                Class_ID integer,
                Sports_ID integer,
                FOREIGN KEY (Class_ID) REFERENCES Class (Class_ID),
                FOREIGN KEY (Sports_ID) REFERENCES Sports (Sports_ID)
            );"""

    staff = """CREATE TABLE IF NOT EXISTS Staff (
                Staff_ID integer PRIMARY KEY,
                Title text NOT NULL,
                Maintains integer,
                Class_ID integer,
                Sports_ID integer,
                FOREIGN KEY (Maintains) REFERENCES Machine (Machine_ID),
                FOREIGN KEY (Class_ID) REFERENCES Class (Class_ID),
                FOREIGN KEY (Sports_ID) REFERENCES Sports (Sports_ID)
            );"""

    muscle = """CREATE TABLE IF NOT EXISTS Muscle (
                Muscle_ID integer PRIMARY KEY,
                Muscle_Name text NOT NULL,
                Category text NOT NULL
            );"""

    machine = """CREATE TABLE IF NOT EXISTS Machine (
                Machine_ID integer PRIMARY KEY,
                Machine_Name text NOT NULL,
                Location text NOT NULL,
                Muscle_ID integer,
                Sports_ID integer,
                FOREIGN KEY (Muscle_ID) REFERENCES Muscle (Muscle_ID),
                FOREIGN KEY (Location) REFERENCES Location (Name),
                FOREIGN KEY (Sports_ID) REFERENCES Sports (Sports_ID)
            );"""

    classes = """CREATE TABLE IF NOT EXISTS Class (
                Class_ID integer PRIMARY KEY,
                Day text NOT NULL,
                Time text NOT NULL,
                Muscle_ID integer,
                Machine_ID integer,
                Sports_ID integer,
                FOREIGN KEY (Muscle_ID) REFERENCES Muscle (Muscle_ID),
                FOREIGN KEY (Machine_ID) REFERENCES Machine (Machine_ID),
                FOREIGN KEY (Sports_ID) REFERENCES Sports (Sports_ID)
            );"""

    sports = """CREATE TABLE IF NOT EXISTS Sports (
                Sports_ID integer PRIMARY KEY,
                Sports_Name text,
                Muscle_ID integer,
                FOREIGN KEY (Muscle_ID) REFERENCES Muscle (Muscle_ID)
            );"""

    insert_users = """INSERT INTO Users (User_ID, Email, First_Name, Last_Name, Class_ID, Sports_ID)
                        VALUES (1001, 'firstuser@lsu.edu', 'John', 'Doe', 100001, 1000001);"""
    insert_users2 = """INSERT INTO Users (User_ID, Email, First_Name, Last_Name, Class_ID, Sports_ID)
                        VALUES (1002, 'seconduser@lsu.edu', 'Jane', 'Doe', 100002, 1000002);"""

    insert_classes = """INSERT INTO Class (Class_ID, Day, Time, Muscle_ID, Machine_ID, Sports_ID)
                        VALUES (100001, 'Tuesday', '7pm', 01, 101, 1000003);"""
    insert_classes2 = """INSERT INTO Class (Class_ID, Day, Time, Muscle_ID, Machine_ID, Sports_ID)
                        VALUES (100002, 'Wednesday', '9pm', 02, 102, 1000004);"""    
    
    insert_machine1 = """INSERT INTO Machine (Machine_ID, Machine_Name, Location, Muscle_ID, Sports_ID)
                        VALUES (111, 'Treadmill', '2nd Floor', 08, 1234567);"""
    insert_machine2 = """INSERT INTO Machine (Machine_ID, Machine_Name, Location, Muscle_ID, Sports_ID)
                        VALUES (120, 'Dumbbells', '3rd Floor', 10, 1457839);"""

    insert_staff = """INSERT INTO Staff (Staff_ID, Title, Maintains, Class_ID, Sports_ID)
                        VALUES (10001, 'Manager', '888', 1000001, 1000000); """

    insert_staff_2 = """INSERT INTO Staff (Staff_ID, Title, Maintains, Class_ID, Sports_ID)
                        VALUES (10002, 'Staff', '999', 100002, 1000001);"""

    insert_sports = """INSERT INTO Sports (Sports_ID,Sports_Name,Muscle_ID)
                        VALUES (1000001, 'Basketball', 123);"""                   
    
    insert_sports2 = """INSERT INTO Sports (Sports_ID,Sports_Name,Muscle_ID)
                        VALUES (1000002, 'Tennis', 124);"""
    
    insert_muscle = """INSERT INTO muscle (Muscle_ID, Muscle_Name, Category)
                        VALUES(01, "Bicep", "Arms");"""
    insert_muscle_2 = """INSERT INTO muscle (Muscle_ID, Muscle_Name, Category)
                        VALUES(02, "Tricep", "Arms");"""

    
    conn = create_connection("4402 Table.db")
    create_table(conn, users)
    create_table(conn, staff)
    create_table(conn, muscle)
    create_table(conn, machine)
    create_table(conn, classes)
    create_table(conn, sports)
    insert_to_table(conn, insert_users)
    insert_to_table(conn, insert_users2)
    insert_to_table(conn, insert_classes)
    insert_to_table(conn, insert_classes2)
    insert_to_table(conn, insert_machine1)
    insert_to_table(conn, insert_machine2)
    insert_to_table(conn, insert_staff)
    insert_to_table(conn, insert_staff_2)
    insert_to_table(conn, insert_sports) 
    insert_to_table(conn, insert_sports2)
    insert_to_table(conn, insert_muscle)
    insert_to_table(conn, insert_muscle_2)
    using_pandas(conn)


def insert_records(name, db, records):
    df = pd.DataFrame(records)
    df.to_sql(name, db, if_exists= 'replace', index = False)

def using_pandas(db):
    df = pd.DataFrame(for_pandas.machines)
    df.columns = ['Machine_ID', 'Machine_Name', 'Location', 'Muscle_ID', 'Sports_ID']
    df.to_sql('Machine', db, if_exists='append', index = False)

    df = pd.DataFrame(for_pandas.muscles)
    df.columns = ['Muscle_ID', 'Muscle_Name', 'Category']
    df.to_sql('Muscle', db, if_exists='append', index = False)

    df = pd.DataFrame(for_pandas.sports)
    df.columns = ['Sports_ID','Sports_Name','Muscle_ID']
    df.to_sql('Sports', db, if_exists='append', index = False)

    df = pd.DataFrame(for_pandas.staffs)
    df.columns = ['Staff_ID', 'Title', 'Maintains', 'Class_ID', 'Sports_ID']
    df.to_sql('Staff', db, if_exists='append', index = False)

    df = pd.DataFrame(for_pandas.users)
    df.columns = ['User_ID', 'Email', 'First_Name', 'Last_Name', 'Class_ID', 'Sports_ID']
    df.to_sql('Users', db, if_exists='append', index = False)

    df = pd.DataFrame(for_pandas.classes)
    df.columns = ['Class_ID', 'Day', 'Time', 'Muscle_ID', 'Machine_ID', 'Sports_ID']
    df.to_sql('Class', db, if_exists='append', index = False)

    db.commit()

if __name__ == '__main__':
    main()
