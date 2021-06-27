import discord
from discord.ext import commands



class Errors(commands.Cog, name="Error"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        embed=discord.Embed(title="Error with executed command: ", description=f"`{error}`")

        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CommandOnCoolDown)::
            await ctx.reply(f'You can use this command again in: {round(error.retry_after, 2)} seconds')
        else:
            await ctx.send(embed=embed)
           


def setup(bot):
    bot.add_cog(Errors(bot))
    print("Error handler is ready!")
