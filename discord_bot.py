"""Simple test discord bot using py-cord and random fox api"""
import json
import logging
import requests
import discord
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot()


@bot.event
async def on_ready():
    """Prints a message to console when bot has logged in"""
    print(f'We have logged in as {bot.user}')


@bot.slash_command(guild_ids=[1081343021775339610])
async def hello(ctx):
    """Respond to the hello command in a friendly manner"""
    await ctx.respond(f"OwO Hello {str(ctx.author)[:-5:]}!")


@bot.slash_command(guild_ids=[1081343021775339610])
async def random_fox(ctx):
    """Respond with a random image of a fox taken from the random fox api"""
    req = requests.get("https://randomfox.ca/floof")
    image = req.json()['image']
    await ctx.respond(image)


with open('key.json') as f:
    data = json.load(f)
    bot.run(data['key'])
