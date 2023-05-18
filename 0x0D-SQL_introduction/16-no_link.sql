-- Lists all records of the table `second_table` of the database
-- Rows without a name value is not listed
-- Result will display score and name
-- Records are listed in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
