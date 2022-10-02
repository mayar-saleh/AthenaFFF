import discord
from discord.utils import get
from discord.ext import commands
import os
from keep_alive import keep_alive

token = "MTAyNTQyNzk2MzczNjQ5ODI5OA.Gvsc-_.YYtMPRyz-Q6zVU2R1-NNUpVkVcYdoJueDvU6Mw"
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='#', intents=intents)
client = discord.Client(intents=intents)
token = os.environ.get("token")


@client.event
async def on_ready():
  print("Bot is ready")


@client.event
async def on_raw_reaction_add(payload):

  channel = client.get_channel(payload.channel_id)

  await channel.send(f'{payload.member} reacted {payload.emoji}')

  message = await channel.fetch_message(payload.message_id)
  reaction = get(message.reactions, emoji=payload.emoji.name)

  if reaction.count >= 5 and str(payload.emoji) == "☣️":

    await channel.send("=================")
    await channel.send("=================")
    await channel.send("=================")
    await channel.send("#####CODE-RED#####")
    await channel.send("=================")
    await channel.send("=================")
    await channel.send("=================")

    for member in payload.member.guild.members:

      try:

        await member.send("https://discord.gg/dxMXpQxP")
        await channel.send(f'{member} recieved invite.')

      except:

        await channel.send(f'{member} did NOT recieved invite.')


@client.event
async def on_message(ctx):

  if str(ctx.content) == "#####CODE-RED#####":
    await ctx.channel.send("ACTIVATING CODE RED.")

    print(str(ctx.content))

keep_alive()
client.run(token)
