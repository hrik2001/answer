from discord.ext import commands, ipc

class IPCCog(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @ipc.server.route()
    async def get_list_guild(self , data):
        print("get_list_guild called")
        return bot.guilds
