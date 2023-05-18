-- A script that lists all the cities of California that can be found in the
-- database hbtn_0d_usa
SELECT states.id, name
FROM states, cities
WHERE name='California'
ORDER BY cities.id ASC;
