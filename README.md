# Discord Bot

Discord bot in Python focused on simple slash commands, with a modular structure for easy growth.

## Initial features
- `/ping` command to check the bot is alive.
- `/joke` command to fetch a random joke via JokeAPI.
- Commands organized in `src/commands`.
- Token loading from `.env` using `python-dotenv`.

## Commands

| Command | Description | Response |
| --- | --- | --- |
| `/ping` | Checks if the bot is online | `Pong!` |
| `/joke` | Returns a random joke | Joke text (single or setup + delivery) |

## Stack and dependencies
- Python 3.x
- `hikari` + `hikari-lightbulb` (bot and slash commands)
- `aiohttp` (async HTTP)
- `python-dotenv` (environment variables)

## Quick install
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration
Create a `.env` file at the project root:
```env
BOT_TOKEN=your_token_here
```

## Running
```bash
python src/bot.py
```

## Project structure
```
src/
  bot.py
  commands/
    ping.py
    joke.py
```

## Notes
- The `/joke` command requires internet access to call the JokeAPI.
- If the API fails, the bot returns a default error message.

## Next steps (ideas)
- Help command listing available commands.
- Better logging and error handling.
- Guild-specific configuration and permissions.
