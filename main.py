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
    main_channel_id = discord.utils.find(
        lambda c: c.name == f'all{config["channel_suffix"]}', 
        client.get_all_channels())

    recent_urls = await get_recent_messages(main_channel_id, 100)

    data = thnapi.get_thn_data()
    new_data = reversed([x for x in data if x["url"] not in recent_urls])

    if(new_data):
        keywords = util.get_filter_words()

        for article in new_data:
            await main_channel_id.send(article["url"])

            article_words = (article["title"] + ' ' + article["details"]).lower().split()

            for channel in keywords:
                channel_ld = discord.utils.find(
                    lambda c: c.name == f'{channel}{config["channel_suffix"]}', 
                    client.get_all_channels())

                if util.list_intersection(article_words, keywords[channel]):
                    await channel_ld.send(article["url"])

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)



