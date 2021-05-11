from flask import Flask,render_template,request,session,redirect,url_for
from chatterbot import ChatBot
from models.models import User, studyuser
from models.database import db_session
from datetime import datetime
from app import key
from hashlib import sha256


app = Flask(__name__)
app.secret_key = key.SECRET_KEY

bot = ChatBot(
        name='MyBot',     
)

@app.route("/")
def index():    
    return render_template("top.html") 

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 

@app.route("/home")
def home():
    if "user_name" in session:
        name = session["user_name"]
        return render_template("home.html",name=name)
    else:
        return redirect(url_for("top",status="logout"))

@app.route("/top")
def top():
    status = request.args.get("status")
    return render_template("top.html",status=status)


@app.route("/login",methods=["post"])
def login():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        if user.hashed_password == hashed_password:
            session["user_name"] = user_name
            return redirect(url_for("home"))
        else:
            return redirect(url_for("top",status="wrong_password"))
    else:
        return redirect(url_for("top",status="user_notfound"))


@app.route("/signup")
def signup():
    status = request.args.get("status")
    return render_template("signup.html",status=status)


@app.route("/registar",methods=["post"])
def registar():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return redirect(url_for("signup",status="exist_user"))
    else:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        user = User(user_name, hashed_password)
        db_session.add(user)
        db_session.commit()
        session["user_name"] = user_name
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top",status="logout"))

if __name__ == "__main__":
    app.run(debug=True)