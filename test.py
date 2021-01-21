import discord
from discord.ext import commands
from random import choice
from string import ascii_uppercase
import random

client = commands.Bot(command_prefix='.', self_bot=True)

@client.event
async def on_redy():
    print('log')


@client.command()
async def say(ctx, *, text):
    for i in range(0, int(text)):
        #test = ''.join(choice(ascii_uppercase) for i in range(10))
        #await ctx.send(embed=discord.Embed(description=test + " " + text))
        lines = open('gifer').read().splitlines()
        myline = random.choice(lines)
        print(myline)
        await ctx.send(embed=discord.Embed().set_image(url=myline))
        #await ctx.send(file=discord.File('giphy.gif'))

client.run("NDEyNjQ2MDExMDk4NDk3MDI0.YAW5oQ.B3EywcuejgCgremsupIuY3Erevk", bot=False)