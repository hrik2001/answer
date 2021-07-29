import discord
from discord.ext import commands
from discord.ext.commands.core import command, has_permissions
from discord.ext.commands.errors import MissingPermissions

class ModerationCog(commands.cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Connected Modretion Cogs")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(slef, ctx, amount=5):
        try:
            await ctx.channel.purge(limit=amount)
            msg= await ctx.send(f"Deleted {amount} messages.")
            await msg.delete(delay=5)
        except MissingPermissions:
            await ctx.send("You don't have required permissions to take that action")
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="None"):
        try:
            await member.kick(reason=reason)
        except MissingPermissions:
            await ctx.send("You don't have required permissions to take that action")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason="None"):
        try:
            await member.ban(reason=reason)
        except MissingPermissions:
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
        except MissingPermissions:
            await ctx.send("You don't have required permissions to take that action")