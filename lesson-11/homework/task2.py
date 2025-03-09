import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
""")

cursor.executemany("""
    INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

cursor.execute("""
    UPDATE Books SET Year_Published = 1950 WHERE Title = "1984"
""")

cursor.execute("""
    SELECT Title, Author FROM Books WHERE Genre = "Dystopian"
""")
print("Dystopian Books:", cursor.fetchall())

cursor.execute("""
    DELETE FROM Books WHERE Year_Published < 1950
""")

cursor.execute("""
    PRAGMA table_info(Books)
""")
columns = [row[1] for row in cursor.fetchall()]
if "Rating" not in columns:
    cursor.execute("""
        ALTER TABLE Books ADD COLUMN Rating REAL
    """)

ratings = {
    "To Kill a Mockingbird": 4.8,
    "1984": 4.7,
    "The Great Gatsby": 4.5
}
for title, rating in ratings.items():
    cursor.execute("""
        UPDATE Books SET Rating = ? WHERE Title = ?
    """, (rating, title))

cursor.execute("""
    SELECT * FROM Books ORDER BY Year_Published ASC
""")
print("Sorted Books:", cursor.fetchall())

# Commit changes and close connection
conn.commit()
conn.close()
