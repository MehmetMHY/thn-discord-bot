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
    channel = discord.utils.find(lambda c: c.name == "all-news", client.get_all_channels())

    recent_urls = await get_recent_msg(channel, 100)

    data = thnapi.get_thn_data()

    new_data = [x for x in data if x["url"] not in recent_urls]
    new_data.reverse()

    if(new_data):
        f = open("./filter_words/stop_words.txt") # words that we don't care about
        stop_words = f.readlines()
        f.close()
        stop_words = [x.lower().strip() for x in stop_words]

        for article in new_data:
            words = article["title"].split() + article["details"].split()
            words = [x.lower() for x in words]

            keywords = []
            for word in words:
                if word not in stop_words:
                    keywords.append(word)
            print(keywords)

def filter_by_keywords(articles, keywords):
    for article in articles:
        words = article["title"].split() + article["details"].split()

def load_filter_words():
    files = get_file_names_regex("./filter_words", "*.txt")
    words = []
    for file in files:
        f = open(file)
        words += f.readlines()
        f.close()
    return words

def get_file_names_regex(directory, pattern):
    file_names = []
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            pattern = re.compile(pattern)
            if pattern.match(file):
                file_names.append(file)
    return file_names

client.run(TOKEN)



