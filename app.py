from quart import Quart , session
from discord.ext import ipc
from dotenv import load_dotenv
load_dotenv()
import os
from src import auth


app = Quart(__name__)
app.config['SECRET_KEY'] = os.getenv("QUART_SECRET_KEY")
app.register_blueprint(auth.auth)
ipc_client = ipc.Client(secret_key = os.getenv("IPC_SECRET"))

#merely for testing purpose
@app.route("/servers")
async def servers():
    guilds = await ipc_client.request("get_list_guild")
    print(type(guilds))
    return(str(guilds))

@app.route("/")
async def index():
    # session["test"]="hello"
    return("!answer")

app.run()
