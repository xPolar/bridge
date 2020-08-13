import discord
from discord.ext import commands
import Config
from colorama import init

init()

bot = commands.Bot(command_prefix = "!", case_insensitive=True)

@bot.event
async def on_message(message):
    if message.author.bot == False and message.content != "":
        Config.CLUSTER["bridge"]["messages"].insert_one({"_id": message.id, "content": message.content, "author": message.author.name})

@bot.event
async def on_ready():
    print(f"\033[1;32;40m[Success]\033[1;0;4m Discord Bot has started!")

# Starts bot
bot.run(Config.TOKEN2)