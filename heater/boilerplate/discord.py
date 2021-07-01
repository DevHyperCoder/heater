from dotenv import load_dotenv
from discord.ext import commands

import os

load_dotenv()

bot = commands.Bot(command_prefix=os.environ["BOT_PREFIX"])


@bot.event
async def on_ready():
    print(f"I'm ready! Online as {str(bot.user)}")


# Loading cogs
for i in os.listdir("./cogs"):
    if i.endswith(".py"):  # Checking if it's a Python file
        bot.load_extension(f"cogs.{i[:-3]}")

# Running bot
bot.run(os.environ["BOT_TOKEN"])
