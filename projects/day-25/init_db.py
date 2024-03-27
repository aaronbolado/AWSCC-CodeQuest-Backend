import sqlite3

conn = sqlite3.connect('books.db')

with open("projects\\day-25\\schema.sql") as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute('''
            INSERT INTO books (title, author, published_year) 
            VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960);
            ''')

cur.execute('''
            INSERT INTO books (title, author, published_year) 
            VALUES ('Sample title', 'John Doe', 2000);
            ''')

conn.commit()
conn.close()