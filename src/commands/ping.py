import lightbulb

def setup(client: lightbulb.Client) -> None:
    @client.register()
    class Ping(
        lightbulb.SlashCommand,
        name="ping",
        description="checks the bot is alive",
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await ctx.respond("Pong!")