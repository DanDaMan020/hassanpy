# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = discord.Bot()


@bot.event
async def on_message(message):
    lowermessage = message.lower()
    if message.author == bot.user:
        return
    if lowermessage.content == 'gg':
        response = 'gg'
        await message.channel.send(response)
    elif message.content == 'wtf':
        response = 'wtf'
        await message.channel.send(response)

bot.run(token)
