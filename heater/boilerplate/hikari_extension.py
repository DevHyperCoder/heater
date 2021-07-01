import lightbulb


class Hello(lightbulb.Plugin):
    def __init__(self, bot: lightbulb.Bot):
        super().__init__()
        self.bot = bot

    @lightbulb.command()
    async def hello(self, ctx: lightbulb.Context):
        await ctx.respond("Hello there!")


def load(bot: lightbulb.Bot):
    bot.add_plugin(Hello(bot))
