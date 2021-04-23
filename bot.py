import discord
from discord.ext import commands 
import datetime
import asyncio
import random
import time
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions



client = commands.Bot(command_prefix = '*')
client.remove_command("help")

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

commands_table = [
    {"cmd":"Won", "desc":"announce winners"},
    {"cmd":"Claimed", "desc":"announce claimers"},
    {"cmd":"Drops", "desc":"pings drops"},
    {"cmd":"Smallgiveaway", "desc":"pings small giveaway"},
    {"cmd":"Partner", "desc":"pings partner pings"},
    {"cmd":"blacklist", "desc":"rewards blacklist user"},
    {"cmd":"Gamenight", "desc":"pings gamenight"},
    {"cmd":"Revive", "desc":"pings chat revive"},
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
    

@client.command(aliases=["rewardsblacklist", "rewards_blacklist", "blacklist"])
@commands.has_role("Staff")
async def rblacklist(ctx, user: discord.Member, *, reason = "No reason provided"):
    if not user:
        await ctx.send("please provide a valid user")

    role = get(ctx.guild.roles, name="Rewards Blacklisted")
    channelID = 786735734626713600
    channel = client.get_channel(channelID)
    user_embed = discord.Embed(title="Blacklisted!", 
                               description=f"You have been **rewards backlisted** by {ctx.author} for {reason}. If you believe this is false, go ahead and appeal.", 
                               color=discord.Color.red(), timestamp=datetime.datetime.utcnow())

    user_embed.set_footer(text="Blacklisted: ")

    success_embed = discord.Embed(title="✔️ Success! ✔️", 
                               description=f"User: {user.mention} ({user.id}) has been rewards blacklisted successfully!", 
                               color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
    success_embed.set_footer(text="\u200b")
    
    log_embed = discord.Embed(title="❌ Rewards Blacklist ❌", 
                               description=f"User: {user.mention} ({user.id}) has been rewards blacklisted by {ctx.author.mention} ({ctx.author.id}) for {reason}.", 
                               color=discord.Color.greyple(), timestamp=datetime.datetime.utcnow())
    log_embed.set_footer(text="\u200b")

    await user.send(embed=user_embed)
    await user.add_roles(role)
    await ctx.send(embed=success_embed)
    await channel.send(embed=log_embed)
    
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

@client.command()
@commands.has_role("Giveaway Manager")
@commands.cooldown(1, 300, commands.BucketType.guild)
async def giveaway(ctx):
    await ctx.send("<@&655469786859438105>")
    await ctx.message.delete()

@client.command()
@commands.has_role("Admin")
async def dm(ctx, member: discord.Member, *, message):
    dm = await member.create_dm()
    await dm.send(message)
    await ctx.send("sent")

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    return
  if isinstance(error, commands.CommandOnCooldown):
    return await ctx.send(f"{error}")
  raise error from error


@client.event
async def on_message(message: discord.Message):
    msg_channel = 832668988072394812
    channel = client.get_channel(msg_channel)
    if message.guild is None and not message.author.bot:
        print(message.content)
        await channel.send(f'Message: **{message.content}** sent by: **{message.author}**')
    await client.process_commands(message)


client.run("ODAyMzU0Mzg1MjE2MzM5OTk4.YAuAwA.Lywh6zXvGkW74EkcWjpTl-PCGLo")
