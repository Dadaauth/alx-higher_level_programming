-- lists all records of the TABLE 'second_table' that has a name value
-- records whose name values are NULL are not listed
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
