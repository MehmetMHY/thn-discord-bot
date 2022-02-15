# The-Hacker-News Discord Bot README

<p align="center">
  <img width="400" alt="profile" src="https://user-images.githubusercontent.com/15916367/154154660-dccf0534-a1f3-49a5-9664-f082fbcdb05e.png">
</p>

## About:
- The thn-discord-bot (tdb), is a Discord bot that scrapes the latest news articles posted on [The Hacker News](https://thehackernews.com/). Then, posts any new articles (urls) to a discord server.
- The bot also filters articles based on the following topics: "apple-news", "google-news", "linux-news", & "microsoft-news".
- Currently, the bot's source of cyber security rleated articles is from [The Hacker News](https://thehackernews.com/). We are hoping to expend our sources moving forward.

## General Discord Server Layout (channels):
- Main-News:
    - all-news  = A channel that will contain all cyber security related articles. No posts will be filtered here.
- Sub-News:
    - apple-news = A channel that will ONLY contain cyber security related articles related to all APPLE products (software & hardware).
    - google-news = A channel that will ONLY contain cyber security related articles related to all GOOGLE products (software & hardware).
    - linux-news = A channel that will ONLY contain cyber security related articles related to all LINUX-BASED products (software & hardware).
    - microsoft-news = A channel that will ONLY contain cyber security related articles related to all MICROSOFT products (software & hardware).

## Requirements:
- python3:
    - pip install beautifulsoup4
    - pip install requests
    - pip install discord.py
    - pip install python-dotenv
- api requires:
    - website: https://thehackernews.com/

## Sources:
- https://thehackernews.com/
- https://realpython.com/beautiful-soup-web-scraper-python/
- https://discordpy.readthedocs.io/en/stable/
- <em>Project's icon is a grouping of muliple Google images that were editied</em>.
  - <em>We can't provide a source but its based from Google Images</em>.
