-- A script that lists all cities contained in the database 'hbtn_0d_usa'
SELECT cities.id, cities.name, state.name
FROM cities INNER JOIN state
ORDER BY cities.id ASC;
