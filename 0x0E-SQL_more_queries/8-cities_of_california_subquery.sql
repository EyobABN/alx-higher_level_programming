-- lists all the cities of california that can be found in the hbtn_0d_usa database
SELECT id, name FROM cities WHERE state_id = (SELECT id from states WHERE name = 'California') ORDER BY cities.id ASC;
