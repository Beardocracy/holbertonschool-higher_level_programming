-- displays the max temperature of each state
SELECT state, MAX(value) AS max_temp 
FROM temperatures 
WHERE state IS NOT null 
GROUP BY state 
ORDER BY state;
