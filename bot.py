import discord
from discord.ext import commands 
import datetime
import asyncio
import random
import time
client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_guild_channel_create(channel):
    channel = client.get_channel(channel.id)
    embed = discord.Embed(title = '<:uc_gift2:832737214224007188> WELCOME TO YOUR INVITE REWARDS TICKET <:uc_gift2:832737214224007188>', description = 'Please follow the format below so we can ensure you get your reward fast and smooth\n\n ```Amount of invites:\nUB or ROBUX (30% less if robux):\nGamepass/Shirt link (if you chose Robux):\nScreenshot of how you got your invites:```', colour = 0xa823fb)
    embed_2 = discord.Embed(title = '<:uc_gift2:832737214224007188> WELCOME TO YOUR LEVEL REWARDS TICKET <:uc_gift2:832737214224007188>', description = 'Please follow the format below so we can ensure you get your reward fast and smooth\n\n ```Your level:\nProof of level (type !rank in chat)```', colour = 0xa823fb)
    embed_3 = discord.Embed(title = '<:uc_gift2:832737214224007188> WELCOME TO YOUR INVITE EVENT TICKET <:uc_gift2:832737214224007188>', description = 'Please follow the format below so we can ensure you get your reward fast and smooth\n\n ```Amount of invites:\nGamepass/Shirt link (if you are claiming robux):\nScreenshot of how you got your invites:```\n\nPlease remember that robux are paid `b/t` meaning we will not cover the 30% roblox tax, so your shirt/gamepass should be set to the exact amount as listed.', colour = 0xa823fb)
    await asyncio.sleep(2)  
    if channel.name.startswith('invite-rewards'):
        await channel.send(embed=embed)
    elif channel.name.startswith('level-rewards'):
        await channel.send(embed=embed_2)
    elif channel.name.startswith('invite-event'):
        await channel.send(embed=embed_3)   
    return 

@client.command()
async def won(ctx, arg1, arg2, arg3):
    await ctx.channel.send("╭ <:uc_gift1:832730994406719489> [ <@{}> ] won the **{}** drop! Go ask them if we are legit!\n<:uc_dot:832731636063535124> <:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096><:uc_line:832731415409197096> <:uc_dot:832731636063535124>".format(arg2, arg3))

@client.command()
async def claimed(ctx, arg1, arg2, arg3):
    channel = client.get_channel(804402670940454973)
    await channel.send("[ <@{}> ] claimed `{}` from `{}`".format(arg1, arg2, arg3))

client.run("ODAyMzU0Mzg1MjE2MzM5OTk4.YAuAwA.Lywh6zXvGkW74EkcWjpTl-PCGLo")