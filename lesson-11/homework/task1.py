import sqlite3


# Connect to SQLite database (or create it)
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
""")

# Insert data
cursor.executemany("""
    INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Update data
cursor.execute("""
    UPDATE Roster SET Name = "Ezri Dax" WHERE Name = "Jadzia Dax"
""")

# Query data
cursor.execute("""
    SELECT Name, Age FROM Roster WHERE Species = "Bajoran"
""")
print("Bajoran Characters:", cursor.fetchall())

# Delete data
cursor.execute("""
    DELETE FROM Roster WHERE Age > 100
""")

# Add new column if it doesn't exist
cursor.execute("""
    PRAGMA table_info(Roster)
""")
columns = [row[1] for row in cursor.fetchall()]
if "Rank" not in columns:
    cursor.execute("""
        ALTER TABLE Roster ADD COLUMN Rank TEXT
    """)

# Update Rank
ranks = {
    "Benjamin Sisko": "Captain",
    "Ezri Dax": "Lieutenant",
    "Kira Nerys": "Major"
}
for name, rank in ranks.items():
    cursor.execute("""
        UPDATE Roster SET Rank = ? WHERE Name = ?
    """, (rank, name))

# Advanced Query
cursor.execute("""
    SELECT * FROM Roster ORDER BY Age DESC
""")
print("Sorted Characters:", cursor.fetchall())

# Commit changes and close connection
conn.commit()
conn.close()
