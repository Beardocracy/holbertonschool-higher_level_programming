-- displays the average temperature (Fahrenheit) by city
SELECT city, AVG(value) AS avg_temp 
FROM temperatures WHERE city IS NOT null
GROUP BY city ORDER BY avg_temp DESC;
