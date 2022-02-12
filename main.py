from email import message
from itertools import count
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
    # channel = client.get_channel(941375372556120120)

    channel = discord.utils.find(lambda c: c.name == "all-news", client.get_all_channels())
    
    recent_urls = []
    async for message in channel.history(limit=100):
        recent_urls.append(message.content)

    data = thnapi.get_thn_data()
    new_data = [x for x in data if x["url"] not in recent_urls]

    if(new_data):
        for item in new_data:
            await channel.send(item["url"])
    
client.run(TOKEN)



