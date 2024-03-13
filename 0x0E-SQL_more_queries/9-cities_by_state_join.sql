-- Lists all cities with their corresponding state names from the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
