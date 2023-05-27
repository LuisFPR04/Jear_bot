import discord
import os
from discord.ext import commands
from phrases import *

token = os.getenv("token.txt")
intents = discord.Intents.default()
intents.message_content = True

jearl = commands.Bot(command_prefix="!j", intents=intents)

def is_alive():
    return jearl.is_ready()

async def on_ready(self):
    print(f'Logged on as {self.user}!')

async def on_message(self, message):
    if message.author.id == self.user.id:
        print("on")

@jearl.command()
async def say_phrase(ctx, phrase_from:str):
    try:
        if phrase_from.lower() != "random":
            phrase = ran_phrase_from(phrase_from)
            await ctx.send(f'{phrase[0]}\n-{phrase[1]}, {phrase[2]}')

        if phrase_from.lower() == "random":
            phrase = random_phrase()
            await ctx.send(f'{phrase[0]}\n -{phrase[1]}, {phrase[2]}')
    except:
        await ctx.send(f'Try a valid command')


jearl.run(token)