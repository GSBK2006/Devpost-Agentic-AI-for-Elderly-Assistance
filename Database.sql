CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE medications (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    medicine_name VARCHAR(100),
    dose VARCHAR(50),
    time TIME,
    adherence BOOLEAN DEFAULT FALSE
);
