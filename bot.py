import discord
from discord.ext import commands 
import datetime
import asyncio
import random
import time
from discord.ext.commands import has_permissions, MissingPermissions



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
@has_permissions(administrator=True)  
async def won(ctx, arg1, arg2):
    await ctx.channel.send("╭ <:uc_gift1:832730994406719489> [ <@{}> ] won the `{}` drop! Ask them if we are legit!\n<:uc_dot:832731636063535124> <:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684> <:uc_dot:832731636063535124>\n<:uc_info:832732093238607939> **TIPS:**\n<:uc_dots:832735257152192522> Put our server above others to easily see pings!\n<:uc_dots:832735257152192522> Put `discord.gg/bobux` in your status for extra claim time!\n<:uc_dots:832735257152192522> Join all our drops to win `Nitro/Robux` easily!\n<:uc_dot:832731636063535124> <:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684> <:uc_dot:832731636063535124>\n╰ <a:vibecat:821107739245150218> **Stay active for more drops!**".format(arg1, arg2))
    await ctx.message.delete()

@client.command()
@has_permissions(administrator=True)
async def claimed(ctx, arg1, arg2, arg3):
    channel = client.get_channel(804402670940454973)
    await channel.send("[ <@{}> ] claimed `{}` from `{}`".format(arg1, arg2, arg3))
    await ctx.message.delete()

@client.command()
@commands.has_role("Staff")
@commands.cooldown(1, 300, commands.BucketType.guild)
async def drops(ctx):
    await ctx.send("<@&726842011075870754>")
    await ctx.message.delete()

@client.command()
@commands.has_role("Staff")
@commands.cooldown(1, 300, commands.BucketType.guild)
async def smallgiveaways(ctx):
    await ctx.send("<@&774841087231524905>")
    await ctx.message.delete()

@client.command()
@commands.has_role("Staff")
@commands.cooldown(1, 300, commands.BucketType.guild)
async def partner(ctx):
    await ctx.send("<@&660280585843114066>")
    await ctx.message.delete()

@client.command()
@commands.has_role("Staff")
@commands.cooldown(1, 300, commands.BucketType.guild)
async def gamenight(ctx):
    await ctx.send("<@&772899769966264341>")
    await ctx.message.delete()

@client.command()
@commands.has_role("Staff")
@commands.cooldown(1, 1800, commands.BucketType.guild)
async def revive(ctx):
    await ctx.send("<@&789928995055468574>")
    await ctx.message.delete()

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    return await ctx.send(f"{error}")
  raise


client.run("ODAyMzU0Mzg1MjE2MzM5OTk4.YAuAwA.Lywh6zXvGkW74EkcWjpTl-PCGLo")