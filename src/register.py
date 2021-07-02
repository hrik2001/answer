from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from discord.ext import commands
from . import models
engine = create_engine("sqlite:///data.db")
models.create(engine)

sess = Session(engine)

class RegisterCog(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_message(self , message):
        # print("someone sent something")



    @commands.command()
    async def register(self , ctx , * , arg):
        new_verify = sess.query(models.Verify).filter_by(otp = arg).first()
        if new_verify:
            new_guild = models.Guild(id = int(ctx.guild.id) , name = ctx.guild.name , member_count = int(ctx.guild.member_count), context = "rik is cool" , username = new_verify.username)
            sess.add(new_guild)
            sess.delete(new_verify)
            sess.commit()
            await ctx.send("thanks for registering " + new_verify.username)
        else:
            await ctx.send("Wrong OTP")
        await ctx.send(str(ctx.guild.id))


