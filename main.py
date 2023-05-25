import discord
from discord.ext import commands
from phrases import ran_phrase

token_arch = open("token.txt", "r")
token = token_arch.readline()
intents = discord.Intents.default()
intents.message_content = True

jearl = commands.Bot(command_prefix="!j", intents=intents)

async def on_ready(self):
    print(f'Logged on as {self.user}!')

async def on_message(self, message):
    if message.author.id == self.user.id:
        print("Funciona")

@jearl.command()
async def say_phrase(ctx, phrase_from:str):
    phrase = ran_phrase(phrase_from)
    await ctx.send(f'{phrase[0]} was said by {phrase[1]}')


jearl.run(token)