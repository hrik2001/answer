from quart import Quart , session
from discord.ext import ipc
from dotenv import load_dotenv
load_dotenv()
import os
from src import auth, guild
from sqlalchemy import create_engine
from src import models


app = Quart(__name__)
app.config['SECRET_KEY'] = os.getenv("QUART_SECRET_KEY")
# app.config["db"] = create_engine("sqlite:///data.db")
# models.create(app.config["db"])
app.register_blueprint(auth.auth)
app.register_blueprint(guild.guild)
ipc_client = ipc.Client(secret_key = os.getenv("IPC_SECRET"))

#merely for testing purpose
@app.route("/servers")
async def servers():
    guilds = await ipc_client.request("get_list_guild")
    return(str(guilds))

@app.route("/")
async def index():
    return("welcome to !answer")

app.run()
