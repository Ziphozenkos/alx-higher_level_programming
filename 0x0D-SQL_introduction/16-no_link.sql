-- script that lists all records of the table second_table of the database hbtn_0c_0
-- Don’t list rows without a name value
-- Results should display the score and the name 
-- Records should be listed by descending score
-- database name will be passed as an argument to the mysql command

SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score
DESC
