CREATE TABLE IF NOT EXISTS users(
    username TEXT NOT NULL, 
    location TEXT NOT NULL, 
    useremail TEXT NOT NULL, 
    password VARCHAR NOT NULL, 
    userid INTEGER PRIMARY KEY AUTOINCREMENT
)