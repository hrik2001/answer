from quart import Blueprint, session, render_template, request, redirect , current_app
from . import models
import bcrypt
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import secrets
import string
engine = create_engine("sqlite:///data.db")
models.create(engine)
import os
from discord.ext import ipc
ipc_client = ipc.Client(secret_key = os.getenv("IPC_SECRET"))
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
                # return(prev_entry.otp)
                return(await render_template("otp.html", otp=prev_entry.otp))

            else:
                otp = gen(10)
                verification = models.Verify(username = session["user"] , otp = otp)
                sess.add(verification)
                sess.commit()
                # return(session["user"])
                # return(otp)
                return(await render_template("otp.html", otp=otp))
        except:
            return(redirect("/login"))

@guild.route("/context/<int:guild_id>", methods=["GET", "POST"])
async def context(guild_id):
    try:
        username = session["user"]
        guild = sess.query(models.Guild).filter_by(id = int(guild_id)).first()
        if username == guild.username:
            if(not guild):
                return(await render_template("error.html", error="Guild doesnt exist"))
            if request.method == "GET":
                return(await render_template("context.html" , guild_id = guild_id, guild_name = guild.name))
            elif request.method == "POST":
                form = await request.form
                guild.context = form["context"]
                sess.commit()
                return(await render_template("error.html",error="context changed for" + str(guild_id)))
        else:
            return(await render_template("error.html", error="You don't own this server"))
    except:
        return(await render_template("error.html", error="You need to login first"))



@guild.route("/channelContext/<int:guild_id>", methods=["GET", "POST"])
async def channelContext(guild_id):
    try:
        username = session["user"]
        guild = sess.query(models.Guild).filter_by(id = int(guild_id)).first()
        if username == guild.username:
            if(not guild):
                return "Guild doesnt exist"
            if request.method == "GET":
                channels = await ipc_client.request("channels" , guild_id = guild.id)
                print(channels)
                return(await render_template("channelContext.html" , guild_id = guild_id, guild_name = guild.name, channels = channels[1:]))
            elif request.method == "POST":
                form = await request.form
                print("form")
                print(form)
                guild.context = form["context"]
                if bool(form['channel']) :
                    channel_id = int(form['channel'])
                else:
                    # "1" because it will be easy to handle than null value
                    channel_id = 1 
                # TODO: work on context names
                context = models.Context(guild_id = int(guild_id),channel_id = channel_id, name = "", para = form['context'])
                sess.add(context)
                sess.commit()
                return(await render_template("error.html",error="context changed for" + str(guild_id)))
        else:
            return(await render_template("error.html", error="You don't dont this server"))

    except Exception as e:
        return "You need to login first" + str(e)

@guild.route("/dashboard" , methods = ["GET"] )
async def dashboard():
    try:
        username = session["user"]
        guilds = sess.query(models.Guild).filter_by(username = username).all()
        return (await render_template("dashboard.html" , guilds = guilds))
    except:
        return(await render_template("error.html", error="You need to login first"))
