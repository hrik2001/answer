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

    @ipc.server.route()
    async def channels(self , data):
        print("get_list_guild called")
        result = []
        # print(data.guild_id)
        for guild in self.bot.guilds:
            if guild.id == data.guild_id:
                result.append(guild.name)
                for channel in guild.channels:
                    if channel.category:
                        channel_details = [channel.name , channel.id ,channel.category.name , channel.category.id, channel.type.name]
                        result.append(channel_details)

        return result
