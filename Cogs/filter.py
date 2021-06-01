import discord
from discord.ext import commands 
from datetime import datetime
import asyncio
import random
import time
import os
import mee6_py_api
import aiohttp
from re import match
from discord.utils import get

from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import tasks
from discord import Webhook, AsyncWebhookAdapter

   

class Events(commands.Cog, name="Events"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        async with aiohttp.ClientSession() as session:
            log_channel = 786735734626713600
            filter_list = ["nigga", "nigger", "n1gga", "nigg3r", "n!gg3r"]
            channel = self.bot.get_channel(log_channel)

            webhook = Webhook.from_url('https://discord.com/api/webhooks/839170018142847008/h2bdEgBozIheGZehzYBlMb_tMwHWg3dbI-bT7cnC441XO8iUDNhKNFaHLMDGywAd3PvF', adapter=AsyncWebhookAdapter(session))

            user_embed = discord.Embed(title="Banned!", 
                                    description=f"You have been **Banned** from Universal Central for saying the N word. If you wish to appeal, join the server below.", 
                                    color=discord.Color.red(), timestamp=datetime.now())
            user_embed.add_field(name="Appeal Server:", value="https://discord.gg/dkaBMKsWEy", inline=False)

            user_embed.set_footer(text="\u200b")
                    
            log_embed = discord.Embed(color=discord.Color.greyple(), timestamp=datetime.now())
            log_embed.add_field(name=f"User:", value=f"{message.author.mention}")
            log_embed.add_field(name="Reason:", value=f"User has said the N word")
            log_embed.set_author(name=f"Ban | {message.author.name}", icon_url=message.author.avatar_url)
            log_embed.set_footer(text=f"ID: {message.author.id}")

            if any(word in message.content.lower() for word in filter_list):
                try:
                    await message.delete()
                    await message.author.send(embed=user_embed)
                    await message.author.ban(reason="Said the N word")
                    await channel.send(embed=log_embed)
                    await webhook.send(embed=log_embed)
                except:
                    await message.delete()
                    await message.author.ban(reason="Said the N word")
                    await channel.send(embed=log_embed)
                    await webhook.send(embed=log_embed)





def setup(bot):
    bot.add_cog(Events(bot))
    print("Events Cog has successfully loaded!")
