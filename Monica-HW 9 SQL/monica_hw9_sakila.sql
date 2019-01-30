USE sakila;

-- 1a find first name and last name of actors in table 'actor'
SELECT first_name, last_name
FROM actor;

-- 1b show first name and last name in the same field
SELECT CONCAT(first_name, ' ' , last_name) AS 'Actor Name'
FROM actor;

-- 2a find the ID number, first name, and last name for 'Joe'
SELECT actor_id, first_name,last_name
FROM actor WHERE first_name = "Joe";

-- 2b Find all actors whose last name contain the letters `GEN`:
SELECT * FROM actor WHERE (last_name LIKE '%GEN%');

-- 2c Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:
SELECT last_name, first_name
FROM actor
WHERE (last_name LIKE '%LI%')
ORDER BY last_name,first_name;

-- 2d. Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China')
ORDER BY country_id;

-- 3a create a column in the table `actor` named `description` and use the data type `BLOB` 
ALTER TABLE actor
ADD  description BLOB;

-- Delete the `description` column.
ALTER TABLE actor
DROP COLUMN description;

SELECT * FROM actor;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name,
COUNT(*) AS count
FROM actor
GROUP BY last_name
ORDER BY count DESC;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name,
COUNT(*) AS count
FROM actor
GROUP BY last_name
HAVING count>1
ORDER BY count DESC;

-- 4c. The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`. Write a query to fix the record.
UPDATE actor SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO' and last_name = 'WILLIAMS';

-- 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! 
-- In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`.
UPDATE actor SET first_name = 'GROUCHO'
WHERE first_name = 'HARPO' and last_name = 'WILLIAMS';

-- 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
SHOW CREATE TABLE address;

-- * 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:
SELECT first_name, last_name, address
FROM address, staff
WHERE address.address_id = staff.address_id;

SELECT first_name, last_name, address
FROM address i
JOIN staff f
ON (i.address_id = f. address_id);

-- * 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`.
SELECT first_name, last_name, SUM(amount)
FROM staff s
JOIN payment p
ON s.staff_id = p.staff_id
GROUP BY p.staff_id
ORDER BY last_name ASC;

-- * 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
SELECT title, COUNT(actor_id)
FROM film f
INNER JOIN film_actor fa
ON f.film_id = fa.film_id
GROUP BY title;

-- * 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
SELECT title, COUNT(title)
FROM film f
INNER JOIN inventory i
ON f.film_id=i.film_id
WHERE title = 'Hunchback Impossible';

--  * 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT last_name, first_name, SUM(amount)
FROM payment p
INNER JOIN customer c
ON p.customer_id=c.customer_id
GROUP BY last_name, first_name
ORDER BY last_name, first_name ASC;

SELECT * FROM language;

  SELECT language_id
  FROM language
  WHERE name = 'English';

-- * 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.
SELECT title
FROM film
WHERE title like ('K%') or title like('Q%')  and language_id IN
(
  SELECT language_id
  FROM language
  WHERE name = 'English'
);
-- * 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
SELECT first_name,last_name
FROM actor
WHERE actor_id IN
(
SELECT actor_id
FROM film_actor
WHERE film_id IN
(
  SELECT film_id
  FROM film
  WHERE title = 'Alone Trip'
)
);

-- * 7c. You want to run an email marketing campaign in Canada, for which you will need the names 
-- and email addresses of all Canadian customers. Use joins to retrieve this information.
SELECT * FROM address;

SELECT c.first_name,c.last_name, c.email, cr.country
FROM customer c
    INNER JOIN address a ON c.address_id = a.address_id
    INNER JOIN city ci ON a.city_id  = ci.city_id
    INNER JOIN country cr ON cr.country_id=ci.country_id
WHERE cr.country='Canada';

-- * 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as _family_ films.
SELECT * FROM category;

SELECT f.title, ca.name
FROM film f
    INNER JOIN film_category fc ON f.film_id=fc.film_id
    INNER JOIN  category ca ON ca.category_id=fc.category_id
WHERE ca.name='Family';

-- * 7e. Display the most frequently rented movies in descending order.
SELECT f.title, COUNT(r.inventory_id) AS 'count'
FROM film f
    INNER JOIN inventory i ON i.film_id=f.film_id
    INNER JOIN rental r ON r.inventory_id=i.inventory_id
GROUP BY f.title    
ORDER BY COUNT(r.inventory_id)  DESC;

SELECT * FROM address;

-- * 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id, SUM(p.amount) AS 'Dollar Amount'
FROM payment p
    INNER JOIN rental r ON p.customer_id=r.customer_id
    INNER JOIN inventory i ON i.inventory_id=r.inventory_id
    iNNER JOIN store s ON s.store_id=i.store_id
GROUP BY s.store_id;


-- * 7g. Write a query to display for each store its store ID, city, and country.
SELECT s.store_id, ci.city, cr.country
FROM store s
    INNER JOIN address a ON a.address_id=s.address_id
    INNER JOIN city ci ON ci.city_id=a.city_id
    iNNER JOIN country cr ON cr.country_id=ci.country_id
GROUP BY s.store_id;

-- * 7h. List the top five genres in gross revenue in descending order. (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT cat.name, SUM(p.amount) AS 'Gross Revenue'
FROM category cat
    INNER JOIN film_category fc ON cat.category_id=fc.category_id
    INNER JOIN inventory i ON i.film_id=fc.film_id
    INNER JOIN rental r ON r.inventory_id=i.inventory_id
    INNER JOIN payment p ON p.customer_id=r.customer_id
GROUP BY cat.name
ORDER BY SUM(p.amount) DESC
LIMIT 5;

-- * 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW top_sales AS
SELECT cat.name 'Genre', SUM(p.amount) AS 'Gross Revenue'
FROM category cat
    INNER JOIN film_category fc ON cat.category_id=fc.category_id
    INNER JOIN inventory i ON i.film_id=fc.film_id
    INNER JOIN rental r ON r.inventory_id=i.inventory_id
    INNER JOIN payment p ON p.customer_id=r.customer_id
GROUP BY cat.name
ORDER BY SUM(p.amount) DESC
LIMIT 5;

-- * 8b. How would you display the view that you created in 8a?
SELECT * FROM top_sales;

-- * 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
DROP VIEW top_sales;