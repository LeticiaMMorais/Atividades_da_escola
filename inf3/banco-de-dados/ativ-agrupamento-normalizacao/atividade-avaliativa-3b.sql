-- Question 1: List rental films for a specific customer (use JOIN)
-- if you want check just one of the customers:

SELECT c.customer_id, 
	c.first_name, 
	c.last_name, 
	film.film_id, 
	film.title, 
	rental.rental_id
FROM customer AS c INNER JOIN rental USING (customer_id)
INNER JOIN inventory USING(inventory_id) 
INNER JOIN film USING(film_id)
GROUP BY c.first_name, c.last_name;

-- Question 2: List the attendant (staff) and quantity rented (use JOIN)
SELECT staff.staff_id, 
    staff.first_name, 
    staff.last_name, 
    COUNT(rental_id) AS quantity_rented 
FROM rental INNER JOIN staff USING(staff_id)
GROUP BY staff.staff_id, staff.first_name, staff.last_name;


-- Question 3: number of films per category (use GROUP BY)
SELECT category.category_id, 
    category.name, 
    COUNT(film) AS number_of_films
FROM film INNER JOIN film_category USING(film_id) 
INNER JOIN category USING(category_id)
GROUP BY category.category_id, category.name
ORDER BY category.category_id;

-- Question 4: Show categories with more than 50 films.
SELECT category.category_id, 
    category.name, 
    COUNT(film) AS number_of_films
FROM film INNER JOIN film_category USING(film_id) 
INNER JOIN category USING(category_id)
GROUP BY category.category_id, category.name
HAVING COUNT(film)>50
ORDER BY category.category_id;


-- Question 5: Find actors whose last name begins with the letter "A" (use LIKE)
SELECT * FROM actor WHERE last_name LIKE 'A%';

-- Question 6: Find films whose title contains "ACTION":
SELECT * FROM film WHERE title LIKE '%ACTION%';

-- Question 7: List the top 10 customers by total amount paid
SELECT customer.customer_id, 
    customer.first_name, 
    customer.last_name, 
    SUM(payment.amount) AS amount_paid 
FROM customer INNER JOIN payment USING(customer_id)
GROUP BY customer.customer_id, customer.first_name, customer.last_name
ORDER BY SUM(payment.amount) DESC 
LIMIT 10;

-- Question 8: Customers whose have more than 20 rentals.
SELECT c.customer_id, 
    c.first_name, 
    c.last_name, 
    COUNT(r) AS number_of_rentals
FROM customer AS c LEFT JOIN rental AS r USING(customer_id)
GROUP BY c.customer_id
HAVING COUNT(r)>20
ORDER BY COUNT(r);

/*
-- Question 9 and 10: ok, here I'll write in portuguese: As tabelas foram criadas no excel e estão em anexo da atividade.
*/

-- Question 9 (in SQL):
CREATE DATABASE locadora_filme;

CREATE TABLE IF NOT EXISTS Cliente_filme (
    customer_id INT,
    filme_locado VARCHAR(120)
);

CREATE TABLE IF NOT EXISTS Cliente (
    customer_id SERIAL,
    nome VARCHAR(50),
    sobrenome VARCHAR(100),
    telefone VARCHAR(20),
    numero INT,
    logradouro VARCHAR(120),
    bairro VARCHAR(120),
    cidade VARCHAR(120),
    estado CHAR(2)
);

ALTER TABLE Cliente_filme
ADD CONSTRAINT pk_cliente_filme 
PRIMARY KEY(customer_id, filme_locado);

ALTER TABLE Cliente
ADD CONSTRAINT pk_cliente
PRIMARY KEY(customer_id);

ALTER TABLE Cliente_filme
ADD CONSTRAINT fk_cliente
FOREIGN KEY(customer_id) REFERENCES Cliente(customer_id);



-- Question 10 (in SQL):
CREATE DATABASE loja_roupa;

CREATE TABLE IF NOT EXISTS Pedido_Cliente(
    pedido_id SERIAL,
    data_pedido DATE,
    cliente_id INT,
    valor_total DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS Cliente(
    cliente_id SERIAL,
    nome VARCHAR(100),
    sobrenome VARCHAR(120),
    email VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS Item(
    item_id SERIAL,
    nome VARCHAR(100),
    preco_uni DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS Pedido_Itens(
    pedido_id INT,
    item_id INT,
    quantidade INT
)


ALTER TABLE Pedido_Cliente
ADD CONSTRAINT pk_pedido_cliente
PRIMARY KEY(pedido_id);

ALTER TABLE Cliente
ADD CONSTRAINT pk_cliente
PRIMARY KEY(cliente_id);

ALTER TABLE Item
ADD CONSTRAINT pk_item
PRIMARY KEY(item_id);

ALTER TABLE Pedido_Itens
ADD CONSTRAINT pk_pedido_item
PRIMARY KEY(pedido_id, item_id);

ALTER TABLE Pedido_Cliente
ADD CONSTRAINT fk_pedido_cliente
FOREIGN KEY(cliente_id) REFERENCES Cliente(cliente_id);

ALTER TABLE Pedido_Itens
ADD CONSTRAINT fk_pedido_cliente
FOREIGN KEY(pedido_id) REFERENCES Pedido_Cliente(pedido_id);

ALTER TABLE Pedido_Itens
ADD CONSTRAINT fk_item
FOREIGN KEY(item_id) REFERENCES Pedido_Itens(item_id);



