import discord, os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')



@bot.command()
async def mem_programación(ctx):
    imagenes = random.choice(os.listdir('images'))
    with open(f'images/{imagenes}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
@bot.command()
async def mem_animals(ctx):
    animals = random.choice(os.listdir('animals_memes'))
    with open(f'animals_memes/{animals}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        a_picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=a_picture)


bot.run("MTIxODU4OTU0MTk2Nzg1OTkzMw.GHP9Bb.u7aGFoi01920tzppBRYnGadWD13HHFPbgbz12Y")
