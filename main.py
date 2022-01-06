#lib
import discord
import decouple

#constants -> urls + sections
from constants import sections, sections_to_url

#config -> tokens, etc
from config import token

#text prompts
from text import helper, lead, root

# create client
client = discord.Client()




# on run
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for section in sections:
        if(message.content.startswith(f"!docs {section}")):
            await message.channel.send(f"{lead} {sections_to_url[section]}")
            return

    if message.content.startswith("!docs help"):
        await message.channel.send(helper)
        return

    if message.content.startswith("!docs"):
        await message.channel.send(root)



client.run(token)

