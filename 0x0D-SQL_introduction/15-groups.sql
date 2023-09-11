-- lists the number of records with the same score together in a group
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY COUNT(score) DESC;
