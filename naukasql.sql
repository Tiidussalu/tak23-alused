SELECT authors.id, authors.author_name
FROM authors a
LEFT JOIN books b ON authors.id = books.author_id
WHERE books.id IS NULL
LIMIT 0, 1000;
