from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("finance.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM Students").fetchall()
    conn.close()
    return render_template("index.html", students=students)

@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form["name"]
    department = request.form["department"]
    year = request.form["year"]
    conn = get_db_connection()
    conn.execute("INSERT INTO Students (name, department, year) VALUES (?, ?, ?)", 
                 (name, department, year))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
