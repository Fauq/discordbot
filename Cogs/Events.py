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



class Events(commands.Cog, name="Events"):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        channel = channel.guild.get_channel(channel.id)
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


    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        supporter = discord.utils.get(after.guild.roles, name="Supporter")
        if supporter is None:
            return
        if "gg/bobux" in str(after.activity):
            if supporter not in after.roles:
                await after.add_roles(supporter, reason="Added gg/bobux to status")
        elif "gg/bobux" not in str(after.activity) and after.status != discord.Status.offline:
            if supporter in after.roles:
                await after.remove_roles(supporter, reason="Removed gg/bobux from status")

        
        

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        msg_channel = 689638287429992469
        channel = self.bot.get_channel(msg_channel)
        if message.guild is None and not message.author.bot:
            if match("@everyone", message.content) is not None:
                print(message.content)
                pass
            else:
                await channel.send(f'Message: **{message.content}** sent by: **{message.author}**')


    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(description ="**・Welcome to Universal\n\nlearn about us ➤ <#761628440247533578>\nget some roles ➤ <#650355016728838164>\ncome chat with us ➤ <#836019395808854016>")
        await self.bot.get_channel(841360219782119434).send(f"{member.mention} greetings!", embed = embed)


def setup(bot):
    bot.add_cog(Events(bot))
    print("Events Cog has successfully loaded!")
