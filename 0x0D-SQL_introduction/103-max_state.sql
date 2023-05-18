-- A script that displays that max temperature of each state (ordered by State
-- name)
SELECT state, MAX(value)
FROM temperatures
GROUP BY STATE
ORDER BY state;

