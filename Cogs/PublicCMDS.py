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
import discord_slash
from dadjokes import Dadjoke
from mee6_py_api import API
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Webhook, AsyncWebhookAdapter
from discord_slash import SlashCommand, cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType


mee6API = API(835347802661453855)

class PublicCMDS(commands.Cog, name="Public"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(description="Gets the amount of users in the server", aliases=["Members", "Membercount"])
    async def users(self, ctx, guild: discord.Guild = None): 
        guild = ctx.guild if not guild else guild
        embed = discord.Embed(title=f"Member count for: {guild}", color=discord.Colour.greyple())
        embed.add_field(name="Total Members:", value=f'{guild.member_count}')
        embed.set_thumbnail(url=guild.icon_url)
        await ctx.send(embed=embed)



    @commands.command(description="Get a level role based on your Mee6 Level!")
    async def lvlrole(self, ctx):
        check_level = await mee6API.levels.get_user_level(ctx.message.author.id)

        embed = discord.Embed(title="✅ Success! ✅", color=discord.Color.blurple())

        embed_error = discord.Embed(title="❌ Error! ❌", color=discord.Color.blurple())
        
        role = get(ctx.guild.roles, name="[10+] Active")

        role2 = get(ctx.guild.roles, name="[20+] Dedicated") 
        
        role3 = get(ctx.guild.roles, name="[30+] Insane") 
        
        role4 = get(ctx.guild.roles, name="[40+] Addicted")

        role5 = get(ctx.guild.roles, name="[50+] Discord is My Life") 
        
        role6 = get(ctx.author.roles, name="[10+] Active")

        role7 = get(ctx.author.roles, name="[20+] Dedicated") 
        
        role8 = get(ctx.author.roles, name="[30+] Insane") 
        
        role9 = get(ctx.author.roles, name="[40+] Addicted")

        role10 = get(ctx.author.roles, name="[50+] Discord is My Life") 
        

        
        if check_level > 9 and check_level < 20:
            if role6:
                embed_error.description=f"You already have the role"
                await ctx.send(embed=embed_error) 
            else:
                embed.description=f"I have given you the role!"
                await ctx.author.add_roles(role)
                await ctx.send(embed=embed)

        elif check_level > 19 and check_level < 30:
            if role6 and role7:
                embed_error.description=f"You already have the role"
                await ctx.send(embed=embed_error) 
            else:
                embed.description=f"I have given you the role(s)!"
                await ctx.author.add_roles(role2, role)
                await ctx.send(embed=embed)

        elif check_level > 29 and check_level < 40:
            if role6 and role7 and role8:
                embed_error.description=f"You already have the role"
                await ctx.send(embed=embed_error) 
            else:
                embed.description=f"I have given you the role(s)!"
                await ctx.author.add_roles(role3, role2, role)
                await ctx.send(embed=embed)

        elif check_level >= 39 and check_level < 50:
            if role6 and role7 and role8 and role9:
                embed_error.description=f"You already have the role"
                await ctx.send(embed=embed_error) 
            else:
                embed.description=f"I have given you the role(s)!"
                await ctx.author.add_roles(role4, role3, role2, role)
                await ctx.send(embed=embed)
        elif check_level >= 50:
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


def setup(bot):
    bot.add_cog(PublicCMDS(bot))
    print("PunlicCMDS Cog has successfully loaded")
