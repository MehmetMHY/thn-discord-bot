# THE-HACKER-NEWS DISCORD BOT

<p align="center">
  <img width="400" alt="profile" src="./assets/imgs/server-icon.png">
</p>

## About:
- The thn-discord-bot (tdb), is a Discord bot that scrapes the latest news articles posted on [The Hacker News](https://thehackernews.com/). Then, posts any new articles (urls) to a discord server.
- The bot also filters articles based on the following topics: "apple-news", "google-news", "linux-news", & "microsoft-news".
- Currently, the bot's source of cyber security rleated articles is from [The Hacker News](https://thehackernews.com/). We are hoping to expend our sources moving forward.

## General Discord Server Layout (channels):
- **Main-News** :
    - **_all-news_** : 
      - A channel that will contain all cyber security related articles. No posts will be filtered here.
- **Sub-News** :
    - **_apple-news_** :
      - A channel that will ONLY contain cyber security related articles related to all APPLE products (software & hardware).
    - **_google-news_** :
      - A channel that will ONLY contain cyber security related articles related to all GOOGLE products (software & hardware).
    - **_linux-news_** :
      - A channel that will ONLY contain cyber security related articles related to all LINUX-BASED products (software & hardware).
    - **_microsoft-news_** :
      - A channel that will ONLY contain cyber security related articles related to all MICROSOFT products (software & hardware).

## Requirements:
- python3:
    - pip install beautifulsoup4
    - pip install requests
    - pip install discord.py
    - pip install python-dotenv
- api requires:
    - website: https://thehackernews.com/

## Project's Scripts:
- background.py : script used to check if discord bot is running and if not, the script re-runs the bot script.
- config.json : config file containing all key variable values/settings.
- filter_words/ : directory of text files of filter words for the "Sub-News" channels.
- bot.py : main script for the discord bot.
- thn_api.py : script used to get/scrape articles from The-Hacker-News website.
- util.py : utility script containing key functions used thoughout other scripts.

## Sources:
- https://thehackernews.com/
- https://realpython.com/beautiful-soup-web-scraper-python/
- https://discordpy.readthedocs.io/en/stable/
- https://github.com/MehmetMHY/daudio-ubuntu
- <em>Project's icon is a grouping of muliple Google images that were editied</em>.
  - <em>We can't provide a source but it was made with images gathered from Google-Images</em>.
