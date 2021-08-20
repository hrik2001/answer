from quart import Blueprint, session, render_template, request, redirect , current_app
from . import models
import bcrypt
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import secrets
import string
engine = create_engine("sqlite:///data.db")
models.create(engine)

sess = Session(engine)

def gen(N):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))

guild = Blueprint("guild", __name__ , template_folder="templates")

@guild.route("/create", methods=["GET"])
async def create():
    if request.method == "GET":
        try:
            prev_entry = sess.query(models.Verify).filter_by(username = session["user"]).first()
            if prev_entry:
                return(prev_entry.otp)
            else:
                otp = gen(10)
                verification = models.Verify(username = session["user"] , otp = otp)
                sess.add(verification)
                sess.commit()
                # return(session["user"])
                return(otp)
        except:
            return(redirect("/login"))

@guild.route("/context/<int:guild_id>", methods=["GET", "POST"])
async def context(guild_id):
    try:
        username = session["user"]
        guild = sess.query(models.Guild).filter_by(id = int(guild_id)).first()
        if username == guild.username:
            if(not guild):
                return "Guild doesnt exist"
            if request.method == "GET":
                return(await render_template("context.html" , guild_id = guild_id, guild_name = guild.name))
            elif request.method == "POST":
                form = await request.form
                guild.context = form["context"]
                sess.commit()
                return("context changed for "+ str(guild_id))
        else:
            return "You don't own this server"
    except:
        return "You need to login first"

@guild.route("/dashboard" , methods = ["GET"] )
async def dashboard():
    try:
        username = session["user"]
        guilds = sess.query(models.Guild).filter_by(username = username).all()
        return (await render_template("dashboard.html" , guilds = guilds))
    except:
        return "You need to login first"
