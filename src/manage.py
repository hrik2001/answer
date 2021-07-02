from discord.ext import commands

class ManageCog(commands.Cog):
    def __init__(self , bot, ask):
        self.bot = bot



    @commands.Cog.listener()
    async def on_connect(self):
        print("Connected!")

    # @commands.command()
    # async def answer(self , ctx , * , arg):
        # await ctx.send(self.ask(arg , "PClub is a club in UIET Panjab University. Panjab University is a decent university. PSOC mentees are cool. PSOC mentors are coolest."))

