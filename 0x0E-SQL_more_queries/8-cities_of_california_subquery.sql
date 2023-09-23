-- @DB1: hbtn_0d_usa

-- lists all the cities of California that can be
-- found in the database @DB1
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states
	WHERE name = 'California')
ORDER BY id ASC;
