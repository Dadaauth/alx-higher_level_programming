-- lists all records in the TABLE 'second_table' with a score
-- greater than or equals to 10
-- And orders them by the score in descending order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
