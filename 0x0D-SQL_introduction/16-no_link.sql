-- lists all records of the table second_table
SELECT score, name
FROM second_table
WHERE name IS NOT null
ORDER BY score DESC;
