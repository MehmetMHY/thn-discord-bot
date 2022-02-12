import os
import re
import discord
from discord.ext import tasks
from dotenv import load_dotenv

# custom packages
import util
import thn_api as thnapi

import json

with open("./config.json") as configfile:
    config = json.load(configfile)

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
    main_channel_id = discord.utils.find(lambda c: c.name == "all-news", client.get_all_channels())

    recent_urls = await get_recent_msg(main_channel_id, 100)

    data = thnapi.get_thn_data()

    new_data = [x for x in data if x["url"] not in recent_urls]
    new_data.reverse()

    if(new_data):

        filter_words = util.get_filter_words()

        channels = {}
        for key in filter_words:
            channels[key] = []

        for article in new_data:
            await main_channel_id.send(article["url"])

            article_words = article["title"].split() + article["details"].split()
            article_words = [x.lower() for x in article_words]

            for key in filter_words:
                if list(set(article_words) & set(filter_words[key])):
                    channels[key].append(article["url"])

        for key in channels:
            channel_ld = discord.utils.find(lambda c: c.name == f'{key}-news', client.get_all_channels())

            for url in channels[key]:
                await channel_ld.send(url)


        


client.run(TOKEN)



