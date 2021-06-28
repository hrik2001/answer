import discord
from dotenv import load_dotenv
import os
from ai import ask
from discord.ext import commands, ipc
from cogs import answer
from cogs import ipc as IPC
from sqlalchemy import create_engine

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

class MyBot(commands.Bot):
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.ipc = ipc.Server(self , secret_key=os.getenv("IPC_SECRET"))

    async def on_ipc_ready(self):
        print("IPC server up and running")

    async def on_ipc_error(self , endpoint, error):
        print(endpoint , error)


# bot = commands.Bot(command_prefix="!")
bot = MyBot(command_prefix="!")
bot.add_cog(answer.AnswerCog(bot , ask))
bot.add_cog(IPC.IPCCog(bot))

bot.ipc.start()
bot.run(token)
