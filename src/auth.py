from quart import Blueprint, session, render_template, request, redirect , current_app
from . import models
import bcrypt
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
engine = create_engine("sqlite:///data.db")
models.create(engine)

sess = Session(engine)

auth = Blueprint("auth", __name__ , template_folder="templates")

@auth.route("/login", methods=["GET" , "POST"])
async def login():
    if request.method == "GET":
        return await render_template("login.html")
    elif request.method == "POST":
        form = await request.form
        user_obj = sess.query(models.User).filter_by(username = form["username"]).first()
        # print(form)
        # print(user_obj)
        if(user_obj):
            if(bcrypt.checkpw(form["password"].encode() , user_obj.password)):
                # print("so true!")
                session["user"] = user_obj.username
            else:
                try:
                    session.pop("user")
                except:
                    pass
                return("wrong password")
        else:
            return("account doesn't exist")
        return(redirect("/"))

@auth.route("/signup", methods=["GET" , "POST"])
async def signup():
    if request.method == "GET":
        return await render_template("signup.html")
    elif request.method == "POST":
        form = await request.form
        print(form)
        new_user = models.User(username = form["username"] , password = bcrypt.hashpw(form["password"].encode() , bcrypt.gensalt()))
        sess.add(new_user)
        sess.commit()
        return(redirect("/login"))

@auth.route("/logout", methods=["GET"])
async def logout():
    if request.method == "GET":
        try:
            session.pop("user")
        except:
            pass
        return(redirect("/login"))

@auth.route("/context/<int:guild_id>", methods=["GET", "POST"])
async def context(guild_id):
    if request.method == "GET":
        return(await render_template("context.html" , guild_id = guild_id))
    elif request.method == "POST":
        form = await request.form
        return("context changed")

