import hikari
import lightbulb
from dotenv import load_dotenv
import os
import aiohttp

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

async def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?lang=pt"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            if data["type"] == "single":
                return data["joke"]
            else:
                return f'{data["setup"]}\n\n{data["delivery"]}'
@client.register()
class Joke(
    lightbulb.SlashCommand,
    name="joke",
    description="make a random joke in portuguese-br",
):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context)-> None:
        joke = await get_joke()
        await ctx.respond(joke)

bot.run()
