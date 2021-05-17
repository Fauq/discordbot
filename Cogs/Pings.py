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
    @commands.has_role("Staff") 
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def won(self, ctx, user: discord.Member):
        embed = discord.Embed(description = "<:uc_info:832732093238607939>** ➤ FOLLOW THE TIPS:**\n<:uc_dots:832735257152192522> Put our server on top of all servers\n<:uc_dots:832735257152192522> Go to the channel and react fast when we ping\n<:uc_dots:832735257152192522> Be sure to participate every time to get free Robux/Nitro!\n\n<:uc_info:832732093238607939>** ➤ EXTRA CLAIM TIMES AND LUCK:**\n<:uc_dots:832735257152192522> <#804401736194326618>" , color = 0xa222f2)
        embed.set_image(url = "https://media.discordapp.net/attachments/689638287429992469/841349132601917450/kek.png")
        await ctx.send(f"{user.mention} won the giveaway! Ask them if we are legit!", embed = embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Staff") 
    async def noreq(self, ctx):
        embed = discord.Embed(description = "<:uc_gift2:832737214224007188>** NO REQUIREMENT GIVEAWAY ! <:uc_gift2:832737214224007188>**\n\n<:uc_info:832732093238607939>** ➤ STEPS TO WIN:**\n<:uc_dots:832735257152192522> Click the :tada: reaction\n<:uc_dots:832735257152192522> Stay active so you won't miss the claim when you win\n<:uc_dots:832735257152192522> Put `discord.gg/bobux` in your status for +5s of claim time!" , color = 0xa222f2)
        embed.set_image(url = "https://media.discordapp.net/attachments/689638287429992469/841349132601917450/kek.png")
        await ctx.send(embed = embed)
        await ctx.message.delete()
    

    @commands.command()
    @commands.has_role("Owner") 
    async def closed(self, ctx):
        embed = discord.Embed(description = "<:uc_info:832732093238607939> **TICKETS ARE CURRENTLY CLOSED**\n\n<:uc_dots:832735257152192522> **Why?** \n Over 100 tickets have been made for the event, meaning I can not allow more users to claim.\n\n<:uc_dots:832735257152192522> **What if I didn't get a ticket?** \n You can always claim our permanent rewards in \n<#816809670848282624>\n\n<:uc_dots:832735257152192522> **When will tickets reopen for normal rewards?**\nWhen I finish paying out the current invite event." , color = 0xa222f2)
        embed.set_image(url = "https://media.discordapp.net/attachments/689638287429992469/841349132601917450/kek.png")
        await ctx.send(embed = embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_role("Admin")
    async def claimed(self, ctx, user: discord.Member, reward, *, how):
        channel = ctx.guild.get_channel(804402670940454973)
        emoji = 'LEGIT:834500768912113724'
        message = await channel.send("[{}] claimed `{}` from {}".format(user.mention, reward, how))
        await message.add_reaction(emoji="LEGIT:834500768912113724")
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
