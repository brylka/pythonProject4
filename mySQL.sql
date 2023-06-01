CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    surname VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO users (name, surname, email)
VALUES ('Jan', 'Kowalski', 'jan.kowalski@example.com'),
       ('Anna', 'Nowak', 'anna.nowak@example.com'),
       ('Michał', 'Zielonka', 'michal.zielonka@example.com'),
       ('Marta', 'Wójcik', 'marta.wojcik@example.com'),
       ('Tomasz', 'Piotrowski', 'tomasz.piotrowski@example.com'),
       ('Agnieszka', 'Jankowska', 'agnieszka.jankowska@example.com'),
       ('Jakub', 'Włodarczyk', 'jakub.wlodarczyk@example.com'),
       ('Magdalena', 'Szymańska', 'magdalena.szymanska@example.com'),
       ('Piotr', 'Kaczmarek', 'piotr.kaczmarek@example.com'),
       ('Barbara', 'Krawczyk', 'barbara.krawczyk@example.com');