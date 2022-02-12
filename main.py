import discord
from discord.ext import tasks
from dotenv import load_dotenv
import json
import os

# custom packages
import util
import thn_api as thnapi

with open("./config.json") as configfile:
    config = json.load(configfile)

# MAIN FUNCTION CALLS:

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    update.start()

async def get_recent_messages(channel, num):
    messages = []
    async for message in channel.history(limit=num):
        messages.append(message.content)
    return messages

@tasks.loop(hours=1)
async def update():
    main_channel_id = discord.utils.find(lambda c: c.name == "all-news", client.get_all_channels())

    recent_urls = await get_recent_messages(main_channel_id, 100)

    data = thnapi.get_thn_data()
    new_data = [x for x in data if x["url"] not in recent_urls].reverse()

    if(new_data):

        filter_words = util.get_filter_words()
        channel_dict = {}
        for channel in filter_words:
            channel_dict[channel] = []

        for article in new_data:
            article_words = article["title"].split() + article["details"].split()
            article_words = [x.lower() for x in article_words]

            for channel in filter_words:
                if util.list_intersection(article_words, filter_words):
                    channel_dict[channel].append(article["url"])

        for channel in channel_dict:
            channel_ld = discord.utils.find(lambda c: c.name == f'{channel}{config["channel_suffix"]}', client.get_all_channels())

            for url in channel_dict[channel]:
                await main_channel_id.send(url)
                await channel_ld.send(url)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)



