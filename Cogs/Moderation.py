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





class Moderation(commands.Cog, name="Mod"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Admin+")
    @commands.has_permissions(administrator=True)
    async def banalt(self, ctx):
        res = []
        time = datetime.now()
        for mem in ctx.guild.members:
            if (time - mem.created_at).total_seconds() <= 604800:
                res.append(mem.id)
                await mem.kick(reason='alt')

        await ctx.send(res)


    @commands.command(description="Admin+")
    @commands.has_role("Admin")
    async def dm(self, ctx, member: discord.Member, *, message):
        dm = await member.create_dm()
        await dm.send(message)
        await ctx.send("sent")

    
    @commands.command(description="Makes a poll", aliases=["makepoll", "poll"])
    @commands.has_permissions(manage_messages=True)
    async def setpoll(self, ctx, *, message):
        em=discord.Embed(title="Server Poll", description=f"{message}", color=discord.Color.greyple())
        msg=await ctx.channel.send(embed=em)
        await ctx.message.delete()
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')


    @commands.command(description="Bans a specific member")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        async with aiohttp.ClientSession() as session:
            channelID = 786735734626713600
            channel = ctx.guild.get_channel(channelID)
            reason = "No Reason Provided"
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

            if user == self.bot.user:
                await ctx.send("You motherfucker, don't even try")
            elif user.guild_permissions.ban_members:
                await ctx.send(f"Bro, {user} has ban perms, you are sped")
            else:
                await user.send(embed=user_embed)
                await ctx.send(embed=embed)
                await channel.send(embed=log_embed)
                await webhook.send(embed=log_embed)
                await user.ban(reason=reason)


    @commands.command(description="Unbans a user")
    @commands.has_role("Admin")
    async def unban(self, ctx, id: int):
        channelID = 786735734626713600
        channel = ctx.guild.get_channel(channelID)
        user = await self.bot.fetch_user(id)
        embed = discord.Embed(description=f"***{user} was unbanned!***", color=discord.Color.green())

        log_embed = discord.Embed(color=discord.Color.red(), timestamp=datetime.now())
        log_embed.add_field(name=f"User:", value=f"{user.mention}")
        log_embed.add_field(name="Moderator:", value=f"{ctx.author.mention}")
        log_embed.set_author(name=f"Unban | {user}", icon_url=user.avatar_url)
        log_embed.set_footer(text=f"ID: {user.id}")

        await ctx.guild.unban(user)
        await ctx.send(embed=embed)
        await channel.send(embed=log_embed)

        
        

    @commands.command(description="Kicks Specified member.")
    @commands.has_any_role('Moderator', 'Head Moderator', "Admin")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):  

        channelID = 786735734626713600
        channel = ctx.guild.get_channel(channelID)
        reason = "No Reason Provided"

        embed=discord.Embed(title="Kicked", description=f"*{member} was kicked* | {reason}", color=discord.Color.red())
        user_embed = discord.Embed(title="Kicked!", description=f"You were kick from **{member.guild}** for **{reason}**.", color=discord.Color.blue())
    
        log_embed = discord.Embed(color=discord.Color.purple(), timestamp=datetime.now())
        log_embed.add_field(name=f"User:", value=f"{member.mention}")
        log_embed.add_field(name="Moderator:", value=f"{ctx.author.mention}")
        log_embed.add_field(name="Reason:", value=f"{reason}")
        log_embed.set_author(name=f"Kicked | {member}", icon_url=member.avatar_url)
        log_embed.set_footer(text=f"ID: {member.id}")

        if member.guild_permissions.kick_members:
            await ctx.send("That user is a Mod or higher bruh")
        else:
            await member.send(embed=user_embed)
            await member.kick(reason=reason)
            await ctx.send(embed=embed)
            await channel.send(embed=log_embed)
     
    @commands.command(description="Nukes the Drops channel")
    @commands.has_any_role("Giveaways", "Owner", "Community Manager", "Co Owner", "Giveaway Manager")
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        def confirm(messages):
            return messages.author == ctx.author

        nuke_channel = get(ctx.guild.text_channels, name="・🎉୧。fast-drops")

        confirmation_embed = discord.Embed(title="❗ Confirmation ❗", description=f"Are you sure you want to nuke the quick-drops channel, {ctx.author.mention}? (y/n)", color=discord.Colour.greyple())
        success_embed = discord.Embed(title="✅ Channel Nuked! ✅", description=f"Channel was nuked by {ctx.author.mention}", color=discord.Color.greyple())
        cancelled_embed = discord.Embed(title="❌ Cancelled ❌", description="Nuking cancelled!", color=discord.Color.greyple())
        invalid_embed = discord.Embed(title="❕ Invalid ❕", description="The response you entered is invalid.", color=discord.Color.greyple())

        await ctx.send(embed=confirmation_embed)
        answer = await self.bot.wait_for('message', timeout=60, check=confirm)
        
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


    @commands.command(description="Rewards blacklist a user", aliases=["rewardsblacklist", "rewards_blacklist", "blacklist"])
    @commands.has_role("Staff")
    async def rblacklist(self, ctx, user: discord.Member, *, reason = "No reason provided"):
        if not user:
            await ctx.send("please provide a valid user")

        role = get(ctx.guild.roles, name="Rewards Blacklisted")
        channelID = 837356438544187402
        channel = ctx.guild.get_channel(channelID)
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





def setup(bot):
    bot.add_cog(Moderation(bot))
    print("Moderation Cog has successfully loaded")
