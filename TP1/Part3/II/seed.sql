CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    favorite_insult TEXT
);

INSERT INTO users (name, favorite_insult) VALUES
('Alice', 'Tu as le charisme d’un slip humide.'),
('Bob', 'T’es pas bête, t’es... très conceptuel.'),
('Charlie', 'Si la bêtise était un sport, tu serais médaillé.'),
('Diana', 'Même Google ne te trouve pas intéressant.');
