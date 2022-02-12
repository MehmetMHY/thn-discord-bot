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

async def get_recent_msg(channel, mlimit):
    recent_urls = []
    async for message in channel.history(limit=mlimit):
        recent_urls.append(message.content)
    return recent_urls

@tasks.loop(hours=1)
async def update():
    channel = discord.utils.find(lambda c: c.name == "all-news", client.get_all_channels())
    
    recent_urls = await get_recent_msg(channel, 100)

    data = thnapi.get_thn_data()

    new_data = [x for x in data if x["url"] not in recent_urls]
    new_data.reverse()

    if(new_data):
        for item in new_data:
            await channel.send(item["url"])
    
client.run(TOKEN)



