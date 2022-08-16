
-- Create 3 Dojos
INSERT INTO dojos (name)
VALUES ('Maria'), ('Harry'), ('Rachel');

-- Delete 3 Dojos
DELETE FROM dojos
WHERE id=1 OR id=2 OR id=3;

-- Create 3 more Dojos
INSERT INTO dojos (name)
VALUES ('Maria'), ('Harry'), ('Rachel');

-- Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojos_id)
VALUES ('Maria', 'Arriviello', 28, 1),
('Harry', 'Chang', 29, 1),
('Rachel', 'Victoria', 27, 1);

-- Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojos_id)
VALUES ('Sam', 'Arriviello', 28, 2),
('Vincent', 'Chang', 29, 2),
('Ava', 'Victoria', 27, 2);

-- Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, dojos_id)
VALUES ('Stacy', 'Arriviello', 28, 3),
('Dean', 'Chang', 29, 3),
('Richard', 'Victoria', 27, 3);

-- Retrieve all the ninjas from the first dojo
SELECT * FROM dojos
LEFT JOIN ninjas ON ninjas.dojos_id=dojos.id
WHERE dojos.id=1;

-- Retrieve all ninjas from last dojo
SELECT * FROM dojos
LEFT JOIN ninjas on ninjas.dojos_id=dojos.id
WHERE dojos.id = (SELECT id FROM dojos ORDER BY id DESC);

-- Retrieve last ninja's dojo
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojos_id FROM ninjas ORDER BY id DESC);

