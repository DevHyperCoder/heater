from discord.ext import commands


class Hello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("Hello there!")


def setup(bot: commands.Bot):
    bot.add_cog(Hello(bot))
