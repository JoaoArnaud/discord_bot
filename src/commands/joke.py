import aiohttp
import lightbulb

async def get_joke() -> str:
    url = (
        "https://v2.jokeapi.dev/joke/Any"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            if data["type"] == "single":
                return data["joke"]
            return f'{data["setup"]}\n\n{data["delivery"]}'

def setup(client: lightbulb.Client) -> None:
    @client.register()
    class Joke(
        lightbulb.SlashCommand,
        name="joke",
        description="make a random joke",
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            try:
                joke = await get_joke()
            except Exception:
                joke = "Sorry i cant get any joke, maybe later..."

            await ctx.respond(joke)
