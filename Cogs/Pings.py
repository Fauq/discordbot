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
    async def won(self, ctx, user: discord.Member):
        embed = discord.Embed(description = "<:uc_info:832732093238607939>** ➤ FOLLOW THE TIPS:**\n<:uc_dots:832735257152192522> Put our server on top of all servers\n<:uc_dots:832735257152192522> Go to the channel and react fast when we ping\n<:uc_dots:832735257152192522> Be sure to participate every time to get free Robux/Nitro!\n\n<:uc_info:832732093238607939>** ➤ EXTRA CLAIM TIMES AND LUCK:**\n<:uc_dots:832735257152192522> <#804401736194326618>" , color = 0xa222f2)
        embed.set_image(url = "https://media.discordapp.net/attachments/689638287429992469/841349132601917450/kek.png")
        await ctx.send("{user.mention} won the giveaway! Ask them if we are legit!")
        await ctx.send(embed = embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Admin")
    async def claimed(self, ctx, arg1, arg2, *, arg3):
        channel = ctx.guild.get_channel(804402670940454973)
        await channel.send("[ <@{}> ] claimed `{}` from {}".format(arg1, arg2, arg3))
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Admin")
    async def end(self, ctx):
        embed = discord.Embed(title = "<:uc_info:832732093238607939> **Event Ended!**" , description = "\n<:uc_dots:832735257152192522> We will be paying those who opened a ticket on time.\n<:uc_dots:832735257152192522> Proof will be posted and logged in <#804402670940454973>\n<:uc_dots:832735257152192522> If you didn't get a ticket, you can always claim <#816809670848282624>\n<:uc_dots:832735257152192522> Be sure to participate every time to get free Robux/Nitro!" , color = 0xf6beb7)
        embed.set_image(url = "https://media.discordapp.net/attachments/832668988072394812/833858193888641135/invite-event.png?width=960&height=257")
        await ctx.send(embed = embed)
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