import discord
from discord.utils import get
from discord.ext import commands
import os
from keep_alive import keep_alive

#token = ""
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='#', intents=intents)
client = discord.Client(intents=intents)
token = os.environ.get("token")


@client.event
async def on_ready():
  print("Bot is ready")

@client.event
async def on_message(ctx):

  if str(ctx.content) == "Hello Athena":
    await ctx.channel.send("Yo!")

    print(str(ctx.content))

keep_alive()
client.run(token)
