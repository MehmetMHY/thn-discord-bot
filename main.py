from distutils.debug import DEBUG
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import json
import logging
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
    logging.info(f'{config["log_msg_prefix"]} connected to discord as {client.user}')
    update.start()

async def get_recent_messages(channel, num):
    messages = []
    async for message in channel.history(limit=num):
        messages.append(message.content)
    return messages

@tasks.loop(hours=1)
async def update():
    logging.info('{config["log_msg_prefix"]} running update()')

    main_channel_id = discord.utils.find(
        lambda c: c.name == f'all{config["channel_suffix"]}', 
        client.get_all_channels())

    recent_urls = await get_recent_messages(main_channel_id, 100)

    data = thnapi.get_thn_data()
    new_data = list(reversed([x for x in data if x["url"] not in recent_urls]))

    logging.info(f'{len(new_data)} new articles found')

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

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')

    logging.basicConfig(
        filename='logs/bot.log',
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client.run(TOKEN)



