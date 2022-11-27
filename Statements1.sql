SELECT User_ID, First_Name, Last_Name
FROM Users
WHERE User_ID > 1012

SELECT Class.Class_ID, Class.Day, Class.Time, Machine.Machine_Name
FROM Machine, Class
WHERE Class.Class_ID > 100005 AND Day = 'Monday'

SELECT Staff_ID, Title, Maintains, Machine_Name
FROM Machine, Staff
WHERE Maintains = Machine.Machine_ID

UPDATE Staff
SET Title = 'Staff', Maintains = 101
WHERE Staff_ID = 10001