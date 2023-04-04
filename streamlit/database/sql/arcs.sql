CREATE TABLE IF NOT EXISTS arcs(
    arcname TEXT NOT NULL, 
    location TEXT NOT NULL, 
    chair TEXT NOT NULL, 
    capacity VARCHAR NOT NULL, 
    products TEXT NOT NULL, 
    arcid INTEGER PRIMARY KEY AUTOINCREMENT
)