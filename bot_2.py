import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def intro(ctx):
    await ctx.send(f'Hola, me presento, soy el {bot.user}! En qué te puedo ayudar hoy?')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTI1MDYzMjU5ODQ4MTI3Njk0OA.GxjHaK.ZwSjJ6c5rSDum4elqZ032vl4NSLPpQPOm3q2q8")
