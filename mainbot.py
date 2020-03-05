# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='')


@bot.command(name='gg')
async def on_gg(ctx):
    await ctx.send('gg')


@bot.command(name='wtf')
async def on_wtf(ctx):
    await ctx.send('wtf')


@bot.event
async def on_bog_event(message):
    lowermessage = message.lower()
    allbogs = ('bog', 'pog', 'poggers', 'b o g')
    for bog in allbogs:
        if bog == lowermessage:
            await message.channel.send('b o g')

bot.run(token)
