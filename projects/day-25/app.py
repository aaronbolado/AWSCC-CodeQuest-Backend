from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.config["DB_NAME"] = "books.db"

def get_db():
    db = sqlite3.connect(app.config["DB_NAME"])
    db.row_factory = sqlite3.Row
    return db

@app.route("/")
def index():
    conn = get_db()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)