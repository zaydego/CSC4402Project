import sqlite3
import pandas as pd

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
                Muscle_ID integer,
                FOREIGN KEY (Muscle_ID) REFERENCES Muscle (Muscle_ID)
            );"""

    insert_users = """INSERT INTO Users (User_ID, Email, First_Name, Last_Name, Class_ID, Sports_ID)
                        VALUES (1001, 'firstuser@lsu.edu', 'John', 'Doe', 001, 100);"""
    
    conn = create_connection("4402 Table.db")
    create_table(conn, users)
    create_table(conn, staff)
    create_table(conn, muscle)
    create_table(conn, machine)
    create_table(conn, classes)
    create_table(conn, sports)
    insert_to_table(conn, insert_users)
    insert_to_table(conn, insert_staff)
    insert_to_table(conn, insert_staff_2)


def insert_records(name, db, records):
    df = pd.DataFrame(records)
    df.to_sql(name, db, if_exists= 'replace', index = False)

if __name__ == '__main__':
    main()
