import discord
from dotenv import load_dotenv
import os
from ai import ask
from discord.ext import commands
from cogs import answer

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix="!")
bot.add_cog(answer.AnswerCog(bot , ask))

bot.run(token)
