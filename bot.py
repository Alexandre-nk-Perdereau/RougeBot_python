# bot.py

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

print("Bot booting...")

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '!')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

bot.load_extension("commands.test")
bot.load_extension("commands.roll")
bot.load_extension('commands.hexa')


@bot.event
async def on_message(message):
    if 'mechant' in message.content:
        await message.channel.send('Attention, un méchant approche !')
    await bot.process_commands(message)

bot.run(DISCORD_BOT_TOKEN)
