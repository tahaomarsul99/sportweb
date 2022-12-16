--USERS
CREATE TABLE users(
    id INTEGER PRIMARY KEY ,
    first_name TEXT NOT NULL,
    middle_name TEXT ,
    last_name TEXT NOT NULL,
    password TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE,
    age INTEGER NOT NULL,
    country TEXT,
    gender TEXT
    );
--SPORT
CREATE TABLE sport(
    id INTEGER PRIMARY KEY ,
    sport_name TEXT NOT NULL,
    image TEXT NOT NULL
    );
--TOOLS
CREATE TABLE tools
(
    sport_id INTEGER,
    tools_name TEXT NOT NULL,
    image TEXT NOT NULL,
    url TEXT,
    FOREIGN KEY(sport_id) REFERENCES sport(id)
);



