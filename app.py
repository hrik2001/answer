from quart import render_template, Quart , session , send_from_directory , redirect
from dotenv import load_dotenv
load_dotenv()
import os
from src import auth, guild
from sqlalchemy import create_engine
from src import models


app = Quart(__name__ , template_folder="src/templates/" , static_folder=None) #static_folder None to be safe
app.config['SECRET_KEY'] = os.getenv("QUART_SECRET_KEY")

@app.route("/res/<path:filename>")
def resources(filename):
    return send_from_directory("src/templates/res" , filename)

@app.route("/css/<path:filename>")
def css(filename):
    return send_from_directory("src/templates/css" , filename)

@app.route("/js/<path:filename>")
def js(filename):
    return send_from_directory("src/templates/js" , filename)
# app.config["db"] = create_engine("sqlite:///data.db")
# models.create(app.config["db"])
app.register_blueprint(auth.auth)
app.register_blueprint(guild.guild)
# ipc_client = ipc.Client(secret_key = os.getenv("IPC_SECRET"))

async def channels(gid):
    channels = await ipc_client.request("channels" , guild_id = gid) 
    return channels

#merely for testing purpose
@app.route("/channels/<int:gid>")
async def servers(gid):
    # guilds = await ipc_client.request("channels" , guild_id = 860087871049564170)
    # guilds = await ipc_client.request("channels" , guild_id = gid)
    guilds = "test"
    return(str(guilds))

@app.route("/")
async def index():
    try:
        username = session["username"]
        return(redirect("/dashboard"))
    except:
        return await render_template("home.html")

app.run()
