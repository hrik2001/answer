from discord.ext import commands, ipc

class IPCCog(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @ipc.server.route()
    async def get_list_guild(self , data):
        print("get_list_guild called")
        # result = list(self.bot.guilds)
        result = []
        for guild in self.bot.guilds:
            result.append([guild.id , guild.name, guild.member_count])
        print(result)
        return result
