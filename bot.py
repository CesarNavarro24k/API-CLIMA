import discord
from discord.ext import commands

# Inicializar el bot
intents = discord.Intents.default()
intents.message_content = True  # Para leer mensajes
bot = commands.Bot(command_prefix="!", intents=intents)

# Manejador de comando !start
@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! Soy un bot que anuncia el pronóstico del tiempo.")

# Iniciar el bot
bot.run("YOUR_BOT_TOKEN")
