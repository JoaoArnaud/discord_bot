import hikari
import lightbulb
from dotenv import load_dotenv
import os

from src.commands.ping import setup as setup_ping
from src.commands.joke import setup as setup_joke

load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = hikari.GatewayBot(token)
client = lightbulb.client_from_app(bot)

bot.subscribe(hikari.StartingEvent, client.start)

setup_ping(client)
setup_joke(client)

bot.run()

