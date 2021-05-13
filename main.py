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
from discord.ext import commands
from ub import Bot as UBBot
from aiohttp import ClientResponseError

client = commands.Bot(command_prefix=['*', "fauqhomo "], owner_ids={262077793528053761, 0xA5457C667C000AA}, intents=discord.Intents(messages=True, guilds=True, presences=True, members=True))
client.remove_command("help")

client.load_extension("jishaku")

@client.event
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".gg/bobux in status for free robux"))
   

initial_extensions = [
'Cogs.Events',
'Cogs.Moderation',
'Cogs.Pings',
'Cogs.PublicCMDS',
'Cogs.Errors'
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
    {"cmd":"kick", "desc":"kicks user"},
    {"cmd":"Dm", "desc":"admin + only"}
]


OWNERID = 306206611054133249
OWNER2 = 262077793528053761


@client.command(aliases=["commands", "cmds"])
async def help(ctx):
    embed = discord.Embed(title="UC Bot all commands", color=discord.Colour.blue())
    for fauq_sucks in commands_table:
        name = fauq_sucks["cmd"]
        descriptions = fauq_sucks["desc"]
        embed.add_field(name=name, value=f"{descriptions}", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command(name = "reload", aliases=['refresh'], description="Reloads a cog (Bot owner only)")
async def reload_(ctx, extension):
    embed = discord.Embed(title="Success!", description=f"I have successfully reloaded the Cog `{extension}`", color=discord.Color.blue())
    if ctx.author.id == OWNERID or ctx.author.id == OWNER2:
        client.reload_extension(f'Cogs.{extension}')
        await ctx.send(embed=embed) 
    else:
        await ctx.send(f"Only the bot owner can use this command")
    

tfile = open("tokens.txt")
read = tfile.read().splitlines()
tfile.close()
ub_token = read[0]
ub_bot = UBBot(ub_token)
client.ub = ub_bot
current_games = {}
ub_bot.current_games = current_games


@client.check
async def is_uc(ctx):
    return ctx.guild and ctx.guild.id == 650354577828216853


@client.event
async def on_ready():
    print("ready")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        error = error.original
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.BadArgument):
        em = discord.Embed(title=None, description=f"Bad Argument: {error}", color=discord.Color.red())
        await ctx.send(embed=em)
    elif isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=None, description=f"Missing Required Argument: {error}", color=discord.Color.red())
        await ctx.send(embed=em)
    else:
        await ctx.send(f"Unhandled Error: {error.__class__.__name__}: {error}")


async def do_flip():
    options = ["heads", "tails"]

    choices = {"heads": "https://media.discordapp.net/attachments/830621813146517514/83088723831318"
                        "1184/bf9914565db17cd2a91ffc589c0dedb7.gif?width=230&height=177",
               "tails": "https://media.discordapp.net/attachments/830621813146517514/8308876742680904"
                        "29/6140d38e3818e4b7bc96c8d9fa9b7db9.gif?width=201&height=174"}
    res = random.choice(options)
    embed = discord.Embed(title=res, description=res, color=discord.Color.blue())
    embed.set_image(url=choices[res])
    return res, embed


@client.group(aliases=['conflip'], invoke_without_command=True, ignore_extra=False)
async def cf(ctx):
    await ctx.send("Must provide a mode (start/join)")


@cf.command(name="start")
@commands.guild_only()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cf_start(ctx, guess, bet: int = 1):
    if ctx.channel.id != 830621813146517514:
        return await ctx.reply("You can only gamble in <#830621813146517514>")
    guess = guess.lower()
    if guess not in ("heads", "tails"):
        return await ctx.reply("Invalid guess - must be `heads` or `tails`")

    if current_games.get(ctx.channel.id) is None:
        if not (1 <= bet <= 250):
            return await ctx.reply("Bet must be in between 1 and 250")
        now = datetime.utcnow()
        current_games[ctx.channel.id] = {ctx.author.id: [bet, guess, now, False]}
        before = await ub_bot.get_bal(ctx.guild.id, ctx.author.id)
        if before.cash < bet:
            current_games.pop(ctx.channel.id, None)
            return await ctx.reply(f"You can't afford that: you only have {before.cash} cash | cancelling game...")
        current_games[ctx.channel.id][ctx.author.id][3] = True
        await ctx.send(f"Started: Waiting for 1 more player... to join, write {ctx.prefix}cf join")
        await asyncio.sleep(60)
        get = current_games.get(ctx.channel.id)
        if get and list(get.values())[0][2] == now:
            current_games.pop(ctx.channel.id, None)
            await ctx.send(f"The coin-flip match expired due to inactivity.")
        return
    await ctx.send("There is already a coin-flip game going on in this channel. write `$cf join`")


@cf.command(name="join")
@commands.guild_only()
@commands.cooldown(1, 1, commands.BucketType.channel)
async def cf_join(ctx):
    game = current_games.get(ctx.channel.id)
    if game is None:
        return await ctx.send(f"There's no game going on. Start one with {ctx.prefix}cf start <guess> <bet>")
    if len(game) > 1:
        return await ctx.send(
            "The maximum number of people in a game is 2. Please wait for the current game to finish and start a new one")
    other_player = next(iter(game.keys()))
    if other_player == ctx.author.id:
        return await ctx.reply("You can't play against yourself... you really have no friends?")
    bet, other_guess, time, validated = game[other_player]
    if not validated:
        return await ctx.reply("The current game isn't validated yet. Please wait a bit and retry")
    guess = "tails" if other_guess == "heads" else "heads"
    game[ctx.author.id] = [bet, guess, datetime.utcnow(), False]
    before = await ub_bot.get_bal(ctx.guild.id, ctx.author.id)
    if before.cash < bet:
        try:
            game.pop(ctx.author.id)
        except:
            pass
        return await ctx.reply(f"You can't afford that: you only have {before.cash} cash")

    res, embed = await do_flip()
    winner = ctx.author.id if res == guess else other_player
    loser = other_player if res == guess else ctx.author.id
    embed.description = f"**<@{winner}> won!**"
    await ub_bot.increment_bal(ctx.guild.id, loser, "cash", -bet, reason="CoinFlip")
    try:
        await ub_bot.increment_bal(ctx.guild.id, winner, "cash", bet, reason="CoinFlip")
    except ClientResponseError as exc:
        if exc.status == 400:
            embed.description += " They had max money though, so no money was awarded. Don't gamble at max tards."
        else:
            raise

    await ctx.send(embed=embed)
    current_games.pop(ctx.channel.id, None)


@cf.command(name="cancel")
@commands.guild_only()
async def cf_cancel(ctx):
    game = current_games.get(ctx.channel.id)
    if game is None:
        return await ctx.send(f"There's no game going on.")
    if game.get(ctx.author.id) is None:
        return await ctx.send("You arent part of that game")
    current_games.pop(ctx.channel.id)
    await ctx.send("Done")


@cf.command(name="current")
@commands.guild_only()
async def cf_current(ctx):
    game = current_games.get(ctx.channel.id)
    if game is None:
        return await ctx.send(f"There's no game going on.")
    key = list(game.keys())[0]
    bet, guess, when, validated = game[key]
    await ctx.reply(f"creator: {key} | bet: {bet} | guess: {guess} | validated: {validated} | "
                    f"when: {when.strftime('%H:%M:%S GMT')}")



client.run("ODAyMzU0Mzg1MjE2MzM5OTk4.YAuAwA.LOvyiP6juG5Qb3Pnun_f-R-mwlk")
