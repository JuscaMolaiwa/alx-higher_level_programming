-- Selects the city and calculates the average temperature for each city from the temperatures table, then orders the results by the average temperature in descending order.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
