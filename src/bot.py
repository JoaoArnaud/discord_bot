import hikari
import lightbulb
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("BOT_TOKEN")
server_id = int(os.getenv("SERVER_ID"))

bot = hikari.GatewayBot(token)
client = lightbulb.client_from_app(bot)

bot.subscribe(hikari.StartingEvent, client.start)

@client.register()
class Ping(
    lightbulb.SlashCommand,
    name="ping",
    description="checks the bot is alive",
):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond("Pong!")

bot.run()
