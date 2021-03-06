import discord
from discord.ext import commands
from discord.ext.commands.core import command, has_permissions
from discord.ext.commands.errors import MissingPermissions

class ModerationCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Connected Moderation Cogs")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        amount = int(amount)
        try:
            await ctx.channel.purge(limit=amount)
            msg= await ctx.send(f"Deleted {amount} messages.")
            await msg.delete(delay=5)
        except:
            await ctx.send("Something went wrong, please check my permissions")

    @clear.error
    async def clear_error(self , ctx , error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have required permissions to take that action")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="None"):
        try:
            await member.kick(reason=reason)
            msg= await ctx.send("Kicked Successfully")
            await msg.delete(delay=5)
        except:
            await ctx.send("Something went wrong, please check my permissions")

    @kick.error
    async def kick_error(self , ctx , error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have required permissions to take that action")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self , ctx, member: discord.Member, *, reason="None"):
        try:
            await member.ban(reason=reason)
            msg= await ctx.send("banned Successfully")
            await msg.delete(delay=5)
        except:
            await ctx.send("Something went wrong, please check my permissions")

    @ban.error
    async def ban_error(self , ctx , error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have required permissions to take that action")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator= member.split('#')

            for ban_entry in banned_users:
                user=ban_entry.user

                if(user.name, user.discriminator)==(member_name,member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'unbanned {user.mention}')
        except:
            await ctx.send("Something went wrong, please check my permissions")

    @unban.error
    async def unban_error(self , ctx , error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have required permissions to take that action")
