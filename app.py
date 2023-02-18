from flask import Flask, render_template, redirect, session, flash, request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL

from helpers import login_required, apology
from datetime import datetime

app = Flask(__name__)
now = datetime.now()

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Database
db = SQL("sqlite:///sangeetkar.db")


@app.route("/")
@login_required
def index():
    return render_template("index.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure old_password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and old_password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        password1 = request.form.get("confirmation")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        phone_number = request.form.get("phone_number")

        # checking possible errors
        if not username or not password or not password1:
            return apology("Field left blank")
        if password != password1:
            return apology("old_password doesnot match !")
        x = db.execute(
            "SELECT username FROM users WHERE username = ?", username)
        if len(x) == 0:
            pass
        elif username == x[0]["username"]:
            return apology("Sorry! username already taken")

        hash = generate_password_hash(password)

        db.execute(
            "INSERT INTO users (username, hash, first_name, last_name, phone_number) VALUES(?, ?, ?, ?, ?)", username, hash, first_name, last_name, phone_number)

        id = db.execute("SELECT id FROM users WHERE username = ?", username)
        return redirect("/")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    # chat feature
    user_id = session["user_id"]

    # TODO display previous chat messeges

    if request.method == "GET":
        return render_template("chat.html")
    
    else:
        message = request.form.get("message")
        db.execute("INSERT INTO messages (user_id, message, datetime) VALUES(?, ?, ?)", user_id, message, now)

        return redirect("/chat")

