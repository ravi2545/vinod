from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/edit")
def edit():
    return render_template("edit.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        address = request.form["address"]
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS emp (name VARCHAR(50), email VARCHAR(50), addres VARCHAR(50))")
            cur.execute("INSERT into emp (name,email,addres) values (?,?,?)", (name, email, address))
            con.commit()
    return render_template("index.html")


@app.route("/editdetails", methods=["POST", "GET"])
def editdetails():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        address = request.form["address"]
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            cur.execute('''UPDATE emp SET email=?,addres=? WHERE name=?''', (email, address, name))
            con.commit()
    return render_template("index.html")


@app.route("/deletedetails", methods=["POST", "GET"])
def deletedetails():
    if request.method == "POST":
        name = request.form["name"]
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            cur.execute('''DELETE FROM emp WHERE name = ?''', (name,))
            con.commit()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)