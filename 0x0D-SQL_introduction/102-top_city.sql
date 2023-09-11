-- displays the top of the 3 cities temperatur during july
-- and august ordered by temperature in descending order
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
