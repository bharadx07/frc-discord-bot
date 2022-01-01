import discord
import decouple

# create client
client = discord.Client()

#constants
sections = ["intro", "control systems", "programming", "api", "software", "advanced", "examples", "hardware", "romi", "networking", "contributing", "issues"]
sections_to_url = {
    "intro": "https://docs.wpilib.org/en/stable/docs/zero-to-robot/introduction.html", 
    "control systems": "https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html", 
    "programming": "https://docs.wpilib.org/en/stable/docs/software/what-is-wpilib.html", 
    "api": "https://first.wpi.edu/wpilib/allwpilib/docs/release/java/index.html", 
    "software": "https://docs.wpilib.org/en/stable/docs/software/driverstation/index.html", 
    "advanced": "https://docs.wpilib.org/en/stable/docs/software/vision-processing/index.html", 
    "examples": "https://docs.wpilib.org/en/stable/docs/software/examples-tutorials/wpilib-examples.html", 
    "hardware": "https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/index.html#", 
    "romi": "https://docs.wpilib.org/en/stable/docs/romi-robot/index.html#", 
    "networking": "https://docs.wpilib.org/en/stable/docs/networking/networking-introduction/index.html", 
    "contributing": "https://docs.wpilib.org/en/stable/docs/contributing/frc-docs/index.html", 
    "issues": "https://github.com/wpilibsuite/frc-docs/issues"
}

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
            await message.channel.send(f"The docs for that section can be found here: {sections_to_url[section]}")
            return

    if message.content.startswith("!docs help"):
        await message.channel.send("This bot helps you easily access FRC documentation. It was created by Bharadwaj Duggaraju in 2022. Run '!docs' to access the docs. Run '!docs section' - (replace section with the actual section) to recive the docs for a certain section of the docs. Sections are: Intro, Control Systems, Programming, API, Software, Advanced, Examples, Hardware, ROMI, Networking, Contributing and Issues.")
        return

    if message.content.startswith("!docs"):
        await message.channel.send("FRC Documentation: https://docs.wpilib.org/en/stable/")

token = decouple.config("TOKEN")

client.run(token)

