-- 1. Quantos clientes moram em tantas cidades? ---
-- 2. Um ator atuou em quantos filmes? ---
-- 3. Um ator atuou em quantos filmes de língua inglesa (English)?

-- -- Question 1
-- SELECT city, COUNT(customer_id) AS numberpeople
-- FROM city AS c 
-- LEFT JOIN address USING (city_id)
-- LEFT JOIN customer USING (address_id)
-- GROUP BY city;

-- -- Question 2
-- SELECT actor_id,first_name,last_name, COUNT(*) AS films_qnt
-- FROM film_actor AS fa 
-- RIGHT JOIN actor AS a USING(actor_id)
-- GROUP BY actor_id, first_name, last_name
-- ORDER BY films_qnt ASC, first_name ASC, last_name ASC, actor_id ASC;

-- -- Question 3:
-- SELECT actor_id, actor.first_name, actor.last_name, COUNT(*)
-- FROM language
-- RIGHT JOIN film USING(language_id)
-- RIGHT JOIN film_actor USING(film_id)
-- RIGHT JOIN actor USING(actor_id)
-- WHERE language.name = 'English'
-- GROUP BY actor.actor_id, actor.first_name, actor.last_name
-- ORDER BY first_name, last_name;