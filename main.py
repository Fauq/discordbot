import discord
from discord.ext import commands 
from datetime import datetime
import asyncio
import random
import time
import os
import mee6_py_api
import aiohttp
import jishaku
import traceback
import sys
from mee6_py_api import API
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Webhook, AsyncWebhookAdapter

client = commands.Bot(command_prefix = ['fauqgay ', "{"], intents=discord.Intents.all())
client.remove_command("help")

client.load_extension("jishaku")

@client.event
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Fauqs smol pp"))
   

initial_extensions = [
'Cogs.Events',
'Cogs.Moderation',
'Cogs.Pings',
'Cogs.PublicCMDS'
]
                    
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension{extension}', file=sys.stderr)
            traceback.print_exc()


commands_table = [
    {"cmd":"Won", "desc":"announce winners"},
    {"cmd":"Claimed", "desc":"announce claimers"},
    {"cmd":"Drops", "desc":"pings drops"},
    {"cmd":"Smallgiveaway", "desc":"pings small giveaway"},
    {"cmd":"Partner", "desc":"pings partner pings"},
    {"cmd":"blacklist", "desc":"rewards blacklist user"},
    {"cmd":"nuke", "desc":"nukes a channel"},
    {"cmd":"Gamenight", "desc":"pings gamenight"},
    {"cmd":"Revive", "desc":"pings chat revive"},
    {"cmd":"lvlrole", "desc":"gives you a lvl role based off your mee6 lvl"},
    {"cmd":"setpoll", "desc":"makes a poll"},
    {"cmd":"ban", "desc":"bans user"},
    {"cmd":"unban", "desc":"unbans user"},
    {"cmd":"Dm", "desc":"admin + only"}
]

@client.command(aliases=["commands", "cmds"])
async def help(ctx):
    embed = discord.Embed(title="UC Bot all commands", color=discord.Colour.blue())
    for fauq_sucks in commands_table:
        name = fauq_sucks["cmd"]
        descriptions = fauq_sucks["desc"]
        embed.add_field(name=name, value=f"{descriptions}", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


    
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    return
  if isinstance(error, commands.CommandOnCooldown):
    return await ctx.send(f"{error}")
  raise error from error



client.run("ODAyMzU0Mzg1MjE2MzM5OTk4.YAuAwA.LOvyiP6juG5Qb3Pnun_f-R-mwlk")
