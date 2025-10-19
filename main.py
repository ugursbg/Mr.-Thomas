import os
import discord
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(names)s: %(message)s"))

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command(name="test", description="tesing shi")
async def test(ctx: discord.ApplicationContext, name="test", description="Tesintg"):
    await ctx.respond(f"HEYAAA {name}!")

bot.run(os.getenv("BotToken"))