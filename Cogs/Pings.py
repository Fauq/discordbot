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
from mee6_py_api import API
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Webhook, AsyncWebhookAdapter




class Pings(commands.Cog, name="Pings"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("Giveaway Manager") 
    @commands.cooldown(1, 300, commands.BucketType.guild)
    async def won(self, ctx, arg1, arg2):
        await ctx.channel.send("╭ <:uc_gift1:832730994406719489> [ <@{}> ] won the `{}` drop! Ask them if we are legit!\n<:uc_dot:832731636063535124> <:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684> <:uc_dot:832731636063535124>\n<:uc_info:832732093238607939> **TIPS:**\n<:uc_dots:832735257152192522> Put our server above others to easily see pings!\n<:uc_dots:832735257152192522> Put `discord.gg/bobux` in your status for extra claim time!\n<:uc_dots:832735257152192522> Join all our drops to win `Nitro/Robux` easily!\n<:uc_dot:832731636063535124> <:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684><:uc_line:833093465943834684> <:uc_dot:832731636063535124>\n╰ <a:vibecat:821107739245150218> **Stay active for more drops!**".format(arg1, arg2))
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Admin")
    async def claimed(self, ctx, arg1, arg2, *, arg3):
        channel = ctx.guild.get_channel(804402670940454973)
        await channel.send("[ <@{}> ] claimed `{}` from {}".format(arg1, arg2, arg3))
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Staff")
    @commands.cooldown(1, 1500, commands.BucketType.guild)
    async def drops(self, ctx):
        await ctx.send("<@&726842011075870754>")
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Staff")
    @commands.cooldown(1, 300, commands.BucketType.guild)
    async def smallgiveaways(self, ctx):
        await ctx.send("<@&774841087231524905>")
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Staff")
    @commands.cooldown(1, 300, commands.BucketType.guild)
    async def partner(self, ctx):
        await ctx.send("<@&660280585843114066>")
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Staff")
    @commands.cooldown(1, 300, commands.BucketType.guild)
    async def gamenight(self, ctx):
        await ctx.send("<@&772899769966264341>")
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Staff")
    @commands.cooldown(1, 1800, commands.BucketType.guild)
    async def revive(self, ctx):
        await ctx.send("<@&789928995055468574>")
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Giveaway Manager")
    @commands.cooldown(1, 3600, commands.BucketType.guild)
    async def giveaway(self, ctx):
        await ctx.send("<@&655469786859438105>")
        await ctx.message.delete()



def setup(bot):
    bot.add_cog(Pings(bot))
    print("Pings Cog has successfully loaded")