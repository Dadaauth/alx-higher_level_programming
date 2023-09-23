-- @DB1: hbtn_0d_usa
-- Lists all the cities contained in the database @DB1
SELECT cities.id, cities.name, states.name FROM
cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
