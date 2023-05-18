-- Lists all records with score >= 10 in second_table
-- Result displays both the score and name
-- Records is ordered by score(top first)
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
