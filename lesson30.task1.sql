CREATE TABLE guests(id INTEGER NOT NULL PRIMARY KEY, 
name TEXT NOT NULL, email NOT NULL, region TEXT NOT NULL);

INSERT INTO guests(name,email,region)
VALUES ("Jon","JonK@gmail.com","Portugal");

UPDATE guests
SET name = 'Jenny', email = 'jenaa@gmail.com', region = 'Italy'
WHERE id = 2;

DELETE FROM guests 
WHERE name = 'Jon';

SELECT * from guests;