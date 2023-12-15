import discord
import os
import random
from discord.ext import commands
from model_test import cat_or_dog

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def image(ctx):
    if ctx.message.attachments:
        for x in ctx.message.attachments:
            name = x.filename
            await x.save(f"image/{name}")
            await ctx.send(cat_or_dog(f"image/{name}"))
        await ctx.send(f'Спасибо за файлы!')
        
    else:
        await ctx.send(f'Дай картинку ! :expressionless: ')

@bot.command()
async def photo(ctx):
    name = random.choice(os.listdir("image"))
    with open(f'image/{name}', 'rb') as file:
        picture = discord.File(file)
        await ctx.send(file=picture)


bot.run("")