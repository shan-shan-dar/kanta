import discord
from discord.ext import commands

import os

import random
import asyncio

import helper as h

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="<@852217601895039068> ", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    ###

    print(f"({message.channel.name}) {message.author.nick}: {message.content}")

    ###

    if message.channel == bot.get_channel(h.speedrun):
        await asyncio.sleep(1)
        await bot.get_channel(h.speedrun).send(int(message.content) + 1)

    ###

    ###

    await bot.process_commands(message)


@bot.command()
async def say(ctx, arg1, argDosentMatterLmao="", arg2=""):
    if arg2 == "":
        channel = ctx.channel
    else:
        channel = bot.get_channel(h.Dict[arg2])
    await channel.send(arg1)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def hello(ctx):
    await ctx.reply(random.choice(h.hello), mention_author=True)


@bot.command()
async def spam(ctx, arg):
    for i in range(int(5 + (random.random() * 5))):
        await ctx.send(arg)


bot.run(os.getenv("TOKEN"))
