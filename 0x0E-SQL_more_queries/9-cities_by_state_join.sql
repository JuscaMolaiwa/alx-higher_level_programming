-- Lists all cities with their corresponding state names from the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON state.id = cities.state_id
ORDER BY cities.id ASC;
