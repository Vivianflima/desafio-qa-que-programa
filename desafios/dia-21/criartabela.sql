CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    idade INT,
    email VARCHAR(255)
);

INSERT INTO usuarios (id, nome, idade, email) VALUES
(1, 'João', 30, 'joao@example.com'),
(2, 'Maria', 25, 'maria@example.com'),
(3, 'Carlos', 35, 'carlos@example.com');
