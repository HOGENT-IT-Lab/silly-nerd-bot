import discord
import os
from dotenv import load_dotenv

load_dotenv()

class SillyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if 'silly' in message.author.nick.lower():
            print(f"silly detected: {message.author.nick} at {message.created_at}")
            await message.add_reaction(discord.PartialEmoji(name="nerd", id=1300766941828481025))


intents = discord.Intents.default()

client = SillyBot(intents=intents)
client.run(os.environ.get('DISCORD_TOKEN'))
