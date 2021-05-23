from flask import Flask,render_template,request,session,redirect,url_for
from chatterbot import ChatBot
from models.models import User, studyuser
from models.database import db_session
from datetime import datetime
from app import key
from hashlib import sha256
from sqlalchemy.sql import func


app = Flask(__name__)
app.secret_key = key.SECRET_KEY

bot = ChatBot(
        name='MyBot', 
        read_only=True,
        # logic_adapters = [
        #     {
        #         'import_path': 'chatterbot.logic.BestMatch', 
        #         'default_response': ['もうしわけありません。わかりません。','理解できませんでした。','ごめんなさい分かりません。'], 
        #         'maximum_similarity_threshold': 0.50, 
        #     },
        # ],    
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


@app.route("/study")
def study():
    if "user_name" in session:
        name = session["user_name"]
        # Stime = studyuser(time)
        all_study = studyuser.query.all()
        countS = studyuser.query.filter_by(userid=name).count()
        # studytime = studyuser.query(func.sum(time=Stime)).filter_by(userid=name)
        return render_template("study.html",name=name,all_study=all_study,countS=countS)
    else:
        return redirect(url_for("top",status="logout"))


@app.route('/new')
def new():
    if "user_name" in session:
        name = session["user_name"]
        return render_template("new.html",name=name)
    else:
        return redirect(url_for("top",status="logout"))


@app.route("/add",methods=["post"])
def add():
    if "user_name" in session:
        userid = session["user_name"] 
        kamoku = request.form["kamoku"]
        kiroku = request.form["kiroku"]
        time = request.form["time"]
        content = studyuser(userid,kamoku,kiroku,time,datetime.now())
        db_session.add(content)
        db_session.commit()
        return redirect(url_for("study"))


@app.route("/edit/<int:id>/")
def edit(id):
    if "user_name" in session:
        name = session["user_name"]
        study = studyuser.query.get(id)
        return render_template("edit.html", name=name, id=id, study=study)
    else:
        return redirect(url_for("top",status="logout"))


@app.route("/update/<int:id>",methods=["post"])
def update(id):
    content = studyuser.query.filter_by(id=id).first()
    content.kamoku = request.form["kamoku"]
    content.kiroku = request.form["kiroku"]
    content.time = request.form["time"]
    db_session.commit()
    return redirect(url_for("study"))


@app.route("/delete/<int:id>/",methods=["post"])
def delete(id):
    id_list = request.form.getlist("delete")
    content = studyuser.query.filter_by(id=id).first()
    db_session.delete(content)
    db_session.commit()
    return redirect(url_for("study"))


if __name__ == "__main__":
    app.run(debug=True)