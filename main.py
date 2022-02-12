from email import message
import json
import time
import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv

# custom packages
import util
import thn_api as thnapi

# MAIN FUNCTION CALLS:

pre_data = []

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    update.start()    

@tasks.loop(hours=1)
async def update():
    channel = client.get_channel(941375372556120120)

    
    data = thnapi.get_thn_data()
    new_data = [x for x in data if x not in pre_data]

    if len(new_data) > 0:
        for i in new_data:
            pre_data.append(i)
    
            await channel.send(i["url"])

client.run(TOKEN)



