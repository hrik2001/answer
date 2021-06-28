from quart import Quart
from discord.ext import ipc
from dotenv import load_dotenv
load_dotenv()
import os


app = Quart(__name__)
ipc_client = ipc.Client(secret_key = os.getenv("IPC_SECRET"))

@app.route("/")
async def index():
    guilds = await ipc_client.request("get_list_guild")
    print(type(guilds))
    return(str(guilds))

app.run()
