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

SELECT * FROM Class WHERE Class_ID NOT IN 
(SELECT Users.Class_ID FROM Users WHERE Users.User_ID > 1014
);

SELECT Machine.Machine_Name, Machine.Location 
FROM Machine JOIN Muscle 
WHERE Muscle.Muscle_Name = 'Quads';

SELECT COUNT(Staff_ID) 
FROM Staff 
WHERE Title = 'Student Employment';

SELECT * 
FROM Users join Class ON Users.Class_ID = Class.Class_ID 
WHERE Class.Class_ID < 100007

SELECT Sports_ID, Sports.Sports_Name, Muscle.Muscle_ID 
FROM Sports INNER JOIN Muscle 
WHERE Sports.Muscle_ID = Muscle.Muscle_ID;

SELECT * 
FROM users 
WHERE First_Name LIKE '_a%'

SELECT Time,COUNT(*)
FROM Class
GROUP BY Time
ORDER BY Time desc;

SELECT Time
FROM Class
ORDER BY Time asc;

SELECT Sports_ID, Muscle_ID
FROM sports
LIMIT 5, 10;

SELECT Last_Name, First_Name
FROM users
WHERE First_Name LIKE 'J%' OR Last_Name LIKE 'D%';

SELECT Machine_ID, Muscle_ID
FROM Machine 
GROUP BY Machine.Muscle_ID;

SELECT Staff.Staff_ID 
FROM Staff 
GROUP by Staff.Title;

SELECT Machine_ID, Muscle_ID
FROM Machine 
GROUP BY machine.Muscle_ID;