from asyncio import events
from types import CellType
import discord
import decouple

# create client
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!docs help"):
        await message.channel.send("This bot helps you easily access FRC documentation. It was created by Bharadwaj Duggaraju in 2022.")
        return

    if message.content.startswith("!docs"):
        await message.channel.send("FRC Documentation: https://docs.wpilib.org/en/stable/")

token = decouple.config("TOKEN")

client.run(token)

