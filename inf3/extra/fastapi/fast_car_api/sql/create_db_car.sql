CREATE TABLE IF NOT EXISTS car (
    id SERIAL NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    color VARCHAR(100),
    factory_year INT,
    model_year INT,
    description TEXT
);