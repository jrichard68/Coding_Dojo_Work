
# 1- countries and percentage that speak Slovene

SELECT countries.name, languages.language, languages.percentage
FROM world.countries
JOIN languages on world.countries.id = languages.country_id
WHERE LANGUAGE ='Slovene' 
ORDER BY languages.percentage DESC;

# 2- total number of cities for each country
SELECT countries.name, COUNT(cities.id)
FROM world.countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY COUNT(cities.id) DESC;

# 3 - All cities in Mexico wiht pop > 500,000
SELECT name, population
FROM cities
WHERE country_id = 136 and population > 500000
ORDER BY population DESC;

# 4 - all languages in each country with a percentage greater than 89%
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages on countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

# 5 - countries with Surface Area below 501 and Population greater than 100,000
SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

#6 - countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years?
SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

#7 - all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000
SELECT name, district, population
FROM cities
WHERE district = 'Buenos Aires' AND population > 500000;

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities on countries.id = cities.country_id
WHERE cities.district = 'Buenos Aires' AND cities.population > 500000;

#8 - summarize the number of countries in each region
SELECT region, COUNT(id)
FROM countries
GROUP BY region;

