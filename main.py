import json
import os
import platform
import random
import sys
from keep_alive import keep_alive
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.ext import commands
from dislash import SlashClient, SelectMenu, SelectOption
import platform
import random
import asyncio
import json
import aiohttp
import discord
import os
import os.path
from discord import message
from discord.ext import commands
from replit import db
from datetime import datetime
import pytz
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
import convertapi

intents = discord.Intents.default()

bot = Bot(command_prefix="!", intents=intents)
slash = SlashClient(bot)

# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    status_task.start()


# Setup the game status task of the bot
@tasks.loop(minutes=1.0)
async def status_task():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="TVRQC Server!"))


# Removes the default help command of discord.py to be able to create our custom help command.
bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith("s.py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_message(message):
    if discord.utils.get(message.author.roles, name="BOT") or discord.utils.get(message.author.roles, name="bot"):
        return
    if message.author == bot.user or message.author.bot:
        return
    msg = message.content
    channel = bot.get_channel(890168057392140298)
    if message.content.startswith('!'):
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        curr_clock=datetime_ist.strftime('%H:%M:%S')
        embed1 = discord.Embed(
        title="Command Used",
        description=f"```{msg}```",
        color=0x42F56C
        )
        embed1.set_footer(
            text=f"Used by {message.author} at {curr_clock}."
        )
        await channel.send(embed=embed1)
    channel1 = bot.get_channel(890174783906533376)
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    curr_clock=datetime_ist.strftime('%H:%M:%S')
    embed2 = discord.Embed(
    title="",
    description=f"```{msg}```",
    color=0x42F56C
    )
    embed2.set_footer(
        text=f"Sent by {message.author} in {message.channel} at {curr_clock}."
    )
    if not message.content.startswith('!'):
        await channel1.send(embed=embed2)
    await bot.process_commands(message)

@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="Error!",
            description=str(error).capitalize(),
            color=0xE02B2B
        )
        await context.channel.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24
        embed = discord.Embed(
            title="Hey, please slow down!",
            description=f"You can use this command again in {f'{round(hours)} hours' if round(hours) > 0 else ''} {f'{round(minutes)} minutes' if round(minutes) > 0 else ''} {f'{round(seconds)} seconds' if round(seconds) > 0 else ''}.",
            color=0xE02B2B
        )
        await context.channel.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Error!",
            description="You are missing the permission `" + ", ".join(
                error.missing_perms) + "` to execute this command!",
            color=0xE02B2B
        )
        await context.channel.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Error!",
            description=str(error).capitalize(),
            color=0xE02B2B
        )
        await context.channel.send(embed=embed)
    raise error


@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

keep_alive()
my_secret = os.environ['token']
bot.run(my_secret)

