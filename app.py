"""CloudTask - a cloud-hosted task manager (Mini Project). Flask + SQLite, deployable on AWS EC2 / GCP / local machine."""
import sqlite3, os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
DB = os.environ.get("DB_PATH", "tasks.db")

def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER DEFAULT 0)")
    return con

@app.route("/")
def index():
    with db() as con:
        tasks = con.execute("SELECT * FROM tasks ORDER BY done, id DESC").fetchall()
    return render_template("index.html", tasks=tasks, host=os.uname().nodename)

@app.post("/add")
def add():
    title = request.form.get("title", "").strip()
    if title:
        with db() as con:
            con.execute("INSERT INTO tasks(title) VALUES(?)", (title,))
    return redirect(url_for("index"))

@app.post("/toggle/<int:tid>")
def toggle(tid):
    with db() as con:
        con.execute("UPDATE tasks SET done = 1 - done WHERE id=?", (tid,))
    return redirect(url_for("index"))

@app.post("/delete/<int:tid>")
def delete(tid):
    with db() as con:
        con.execute("DELETE FROM tasks WHERE id=?", (tid,))
    return redirect(url_for("index"))

@app.get("/api/tasks")
def api():
    with db() as con:
        return jsonify([dict(r) for r in con.execute("SELECT * FROM tasks")])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
