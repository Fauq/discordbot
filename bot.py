'''import discord
from discord.ext import commands 
import asyncio
import random
import time
import os
import mee6_py_api
import aiohttp
import jishaku
import datetime 
from datetime import datetime
from mee6_py_api import API
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Webhook, AsyncWebhookAdapter

client = commands.Bot(command_prefix = ['*', "succyfauqy "], intents=discord.Intents.all())
client.remove_command("help")

mee6API = API(650354577828216853)
client.load_extension("jishaku")

@client.event
async def on_ready():
    print('Bot is ready.')
   

@client.event
async def on_guild_channel_create(channel):
    channel = client.get_channel(channel.id)
    embed = discord.Embed(title = '<:uc_gift2:832737214224007188> WELCOME TO YOUR INVITE REWARDS TICKET <:uc_gift2:832737214224007188>', description = 'Please follow the format below so we can ensure you get your reward fast and smooth\n\n ```Amount of invites:\nUB or ROBUX (25% less if robux):\nGamepass/Shirt link (if you chose Robux):\nScreenshot of how you got your invites:```', colour = 0xa823fb)
    embed_2 = discord.Embed(title = '<:uc_gift2:832737214224007188> WELCOME TO YOUR LEVEL REWARDS TICKET <:uc_gift2:832737214224007188>', description = 'Please follow the format below so we can ensure you get your reward fast and smooth\n\n ```Your level:\nProof of level (type !rank in chat)```', colour = 0xa823fb)
    embed_3 = discord.Embed(title = '<:uc_gift2:832737214224007188> WELCOME TO YOUR INVITE EVENT TICKET <:uc_gift2:832737214224007188>', description = 'Please follow the format below so we can ensure you get your reward fast and smooth\n\n ```Amount of invites:\nGamepass/Shirt link (if you are claiming robux):\nScreenshot of how you got your invites:```\nPlease remember that robux are paid `b/t` meaning we will not cover the 30% roblox tax, so your shirt/gamepass should be set to the exact amount as listed.', colour = 0xa823fb)
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
    {"cmd":"nuke", "desc":"nukes a channel"},
    {"cmd":"Gamenight", "desc":"pings gamenight"},
    {"cmd":"Revive", "desc":"pings chat revive"},
    {"cmd":"lvlrole", "desc":"gives you a lvl role based off your mee6 lvl"},
    {"cmd":"setpoll", "desc":"makes a poll"},
    {"cmd":"ban", "desc":"bans user"},
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

@client.command()
@commands.has_permissions(administrator=True)
async def banalt(ctx):
    res = []
    time = datetime.now()
    for mem in ctx.guild.members:
        if (time - mem.created_at).total_seconds() <= 604800:
            res.append(mem.id)
            await mem.kick(reason='alt')
             # I DONT DO THIS YET JUST TO MAKE SURE ALL ARE ALT BEFORE U RUN


    await ctx.send(res)
        
           


    

@client.command(aliases=["rewardsblacklist", "rewards_blacklist", "blacklist"])
@commands.has_role("Staff")
async def rblacklist(ctx, user: discord.Member, *, reason = "No reason provided"):
    if not user:
        await ctx.send("please provide a valid user")

    role = get(ctx.guild.roles, name="Rewards Blacklisted")
    channelID = 837356438544187402
    channel = client.get_channel(channelID)
    user_embed = discord.Embed(title="Blacklisted!", 
                               description=f"You have been **rewards backlisted** by {ctx.author} for **{reason}**. If you believe this is false, go ahead and appeal.", 
                               color=discord.Color.red(), timestamp=datetime.now())
    user_embed.add_field(name="Appeal Server:", value="https://discord.gg/dkaBMKsWEy", inline=False)

    user_embed.set_footer(text="\u200b")

    success_embed = discord.Embed(title="✅ Success! ✅", 
                               description=f"User: {user.mention} ({user.id}) has been rewards blacklisted successfully!", 
                               color=discord.Color.blue(), timestamp=datetime.now())
    success_embed.set_footer(text="\u200b")
    
    log_embed = discord.Embed(title="❌ Rewards Blacklist ❌", color=discord.Color.greyple(), timestamp=datetime.now())
    log_embed.add_field(name=f"User:", value=f"{user.mention}")
    log_embed.add_field(name="Moderator:", value=f"{ctx.author.mention}")
    log_embed.add_field(name="Reason:", value=f"{reason}")
    log_embed.set_footer(text="\u200b")

    await user.send(embed=user_embed)
    await user.add_roles(role)
    await ctx.send(embed=success_embed)
    await channel.send(embed=log_embed)


@client.command()
async def lvlrole(ctx):
    check_level = await mee6API.levels.get_user_level(ctx.message.author.id)

    embed = discord.Embed(title="✅ Success! ✅", color=discord.Color.blurple())

    embed_error = discord.Embed(title="❌ Error! ❌", color=discord.Color.blurple())
    
    role = get(ctx.guild.roles, name="Active | Lvl 10+")

    role2 = get(ctx.guild.roles, name="Dedicated | Lvl 20+") 
    
    role3 = get(ctx.guild.roles, name="Godly | Lvl 30+") 
    
    role4 = get(ctx.guild.roles, name="Insane | Lvl 40+")

    role5 = get(ctx.guild.roles, name="No Life | Lvl 50+") 
    
    role6 = get(ctx.author.roles, name="Active | Lvl 10+")

    role7 = get(ctx.author.roles, name="Dedicated | Lvl 20+") 
    
    role8 = get(ctx.author.roles, name="Godly | Lvl 30+") 
    
    role9 = get(ctx.author.roles, name="Insane | Lvl 40+")

    role10 = get(ctx.author.roles, name="No Life | Lvl 50+") 
    

    
    if check_level >= 9 and check_level < 19:
        if role6:
            embed_error.description=f"You already have the role"
            await ctx.send(embed=embed_error) 
        else:
            embed.description=f"I have given you the role!"
            await ctx.author.add_roles(role)
            await ctx.send(embed=embed)

    elif check_level >= 19 and check_level < 29:
        if role6 and role7:
            embed_error.description=f"You already have the role"
            await ctx.send(embed=embed_error) 
        else:
            embed.description=f"I have given you the role(s)!"
            await ctx.author.add_roles(role2, role)
            await ctx.send(embed=embed)

    elif check_level >= 29 and check_level < 39:
        if role6 and role7 and role8:
            embed_error.description=f"You already have the role"
            await ctx.send(embed=embed_error) 
        else:
            embed.description=f"I have given you the role(s)!"
            await ctx.author.add_roles(role3, role2, role)
            await ctx.send(embed=embed)

    elif check_level >= 39 and check_level < 49:
        if role6 and role7 and role8 and role9:
            embed_error.description=f"You already have the role"
            await ctx.send(embed=embed_error) 
        else:
            embed.description=f"I have given you the role(s)!"
            await ctx.author.add_roles(role4, role3, role2, role)
            await ctx.send(embed=embed)
    elif check_level >= 49:
        if role6 and role7 and role8 and role9 and role10:
            embed_error.description=f"You already have the role"
            await ctx.send(embed=embed_error) 
        else:
            embed.description=f"I have given you the role(s)!"
            await ctx.author.add_roles(role5, role4, role3, role2, role)
            await ctx.send(embed=embed)
    else:
        await ctx.send("You need to be 10+ to use this command.")
        return
    

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="No Reason Provided."):
    async with aiohttp.ClientSession() as session:
        channelID = 786735734626713600
        channel = client.get_channel(channelID)
        webhook = Webhook.from_url('https://discord.com/api/webhooks/839170018142847008/h2bdEgBozIheGZehzYBlMb_tMwHWg3dbI-bT7cnC441XO8iUDNhKNFaHLMDGywAd3PvF', adapter=AsyncWebhookAdapter(session))
        embed = discord.Embed(description=f"***{user} was banned*** | {reason}", color=discord.Color.blue())
        user_embed = discord.Embed(title="Banned!", description=f"You were banned in **{user.guild}** for **{reason}**.", color=discord.Color.blue())
        user_embed.add_field(name="Appeal Server: ", value="https://discord.gg/dkaBMKsWEy")

            
        log_embed = discord.Embed(color=discord.Color.greyple(), timestamp=datetime.now())
        log_embed.add_field(name=f"User:", value=f"{user.mention}")
        log_embed.add_field(name="Moderator:", value=f"{ctx.author.mention}")
        log_embed.add_field(name="Reason:", value=f"{reason}")
        log_embed.set_author(name=f"Ban | {user}", icon_url=user.avatar_url)
        log_embed.set_footer(text=f"ID: {user.id}")

        if user == client.user:
            await ctx.send("You motherfucker, don't even try")
        elif user.guild_permissions.ban_members:
            await ctx.send(f"Bro, {user} has ban perms, you are sped")
        else:
            await user.send(embed=user_embed)
            await ctx.send(embed=embed)
            await channel.send(embed=log_embed)
            await webhook.send(embed=log_embed)
            await user.ban(reason=reason)

        
    
@client.command(aliases=["makepoll", "poll"])
@commands.has_permissions(manage_messages=True)
async def setpoll(ctx, *, message):
    em=discord.Embed(title="Server Poll", description=f"{message}", color=discord.Color.greyple())
    msg=await ctx.channel.send(embed=em)
    await ctx.message.delete()
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

@client.event
async def on_member_update(before, after):
    supporter = discord.utils.get(after.guild.roles, name="Supporter")
    if supporter is None:
        return
    if "gg/bobux" in str(after.activity):
        if supporter not in after.roles:
            await after.add_roles(supporter, reason="Added gg/bobux to status")
    elif "gg/bobux" not in str(after.activity) and after.status != discord.Status.offline:
        if supporter in after.roles:
            await after.remove_roles(supporter, reason="Removed gg/bobux from status")
    
   
@client.command()
@commands.has_any_role("Admin", "Head Admin", "Owner", "Community Manager", "Co Owner", "Giveaway Manager")
async def nuke(ctx, channel: discord.TextChannel = None):
    def confirm(messages):
        return messages.author == ctx.author

    nuke_channel = ctx.channel

    confirmation_embed = discord.Embed(title="❗ Confirmation ❗", description=f"Are you sure you want to nuke this channel, {ctx.author.mention}? (y/n)", color=discord.Colour.greyple())
    success_embed = discord.Embed(title="✅ Channel Nuked! ✅", description=f"Channel was nuked by {ctx.author.mention}", color=discord.Color.greyple())
    cancelled_embed = discord.Embed(title="❌ Cancelled ❌", description="Nuking cancelled!", color=discord.Color.greyple())
    invalid_embed = discord.Embed(title="❕ Invalid ❕", description="The response you entered is invalid.", color=discord.Color.greyple())

    await ctx.send(embed=confirmation_embed)
    answer = await client.wait_for('message', timeout=60, check=confirm)
    
    answer = answer.content
    low = answer.lower()

    if low in ('yes', 'y'):
        answer.lower()
        new_channel = await nuke_channel.clone(reason=f"{ctx.author} nuked the channel")
        await nuke_channel.delete()
        await new_channel.edit(position=nuke_channel.position)
        await new_channel.send(embed=success_embed)
    elif low in ('no', 'n'):
        answer.lower()
        await ctx.send(embed=cancelled_embed)
    else:
        await ctx.send(embed=invalid_embed)
        
@client.command(aliases=["Members", "Membercount"])
async def users(ctx, guild: discord.Guild = None): 
    guild = ctx.guild if not guild else guild
    embed = discord.Embed(title=f"Member count for: {guild}", color=discord.Colour.greyple())
    embed.add_field(name="Total Members:", value=f'{guild.member_count}')
    embed.set_thumbnail(url=guild.icon_url)
    await ctx.send(embed=embed)
    
    
@client.command()
@commands.has_role("Giveaway Manager") 
@commands.cooldown(1, 300, commands.BucketType.guild)
async def won(ctx, arg1, arg2):
    await ctx.channel.send("╭ <:uc_gift1:832730994406719489> [ <@{}> ] won the `{}` drop! Ask them if we are legit!\n<:uc_dot:832731636063535124> <:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684> <:uc_dot:832731636063535124>\n<:uc_info:832732093238607939> **TIPS:**\n<:uc_dots:832735257152192522> Put our server above others to easily see pings!\n<:uc_dots:832735257152192522> Put `discord.gg/bobux` in your status for extra claim time!\n<:uc_dots:832735257152192522> Join all our drops to win `Nitro/Robux` easily!\n<:uc_dot:832731636063535124> <:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684> <:uc_dot:832731636063535124>\n╰ <a:vibecat:821107739245150218> **Stay active for more drops!**".format(arg1, arg2))
    await ctx.message.delete()

@client.command()
@commands.has_role("Admin")
async def claimed(ctx, arg1, arg2, *, arg3):
    channel = client.get_channel(804402670940454973)
    await channel.send("[ <@{}> ] claimed `{}` from {}".format(arg1, arg2, arg3))
    await ctx.message.delete()

@client.command()
@commands.has_role("Staff")
@commands.cooldown(1, 1500, commands.BucketType.guild)
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
@commands.cooldown(1, 3600, commands.BucketType.guild)
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
    msg_channel = 689638287429992469
    channel = client.get_channel(msg_channel)
    if message.guild is None and not message.author.bot:
        print(message.content)
        await channel.send(f'Message: **{message.content}** sent by: **{message.author}**')
    await client.process_commands(message)

client.run("ODAyMzU0Mzg1MjE2MzM5OTk4.YAuAwA.LOvyiP6juG5Qb3Pnun_f-R-mwlk")'''
