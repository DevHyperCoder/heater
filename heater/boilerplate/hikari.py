from dotenv import load_dotenv

import lightbulb
import hikari
import os

load_dotenv()

bot = lightbulb.Bot(token=os.environ["BOT_TOKEN"], prefix=os.environ["BOT_PREFIX"])


@bot.listen(hikari.StartedEvent)
async def on_ready(event: hikari.StartedEvent):
    print(f"I'm ready! Online as {str(bot.me)}")


# Loading cogs
for i in os.listdir("./plugins"):
    if i.endswith(".py"):  # Checking if it's a Python file
        bot.load_extension(f"plugins.{i[:-3]}")

# Running bot
bot.run()
