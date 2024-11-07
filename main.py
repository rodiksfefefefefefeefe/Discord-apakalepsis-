import discord
from discord.ext import commands
import random
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(f'Мы вошли как {bot.user}')
@bot.command(name='температура', help='2,6—4,8 °C')
async def temperature(ctx):
    baseline_temp = 15
    warming_factor = random.uniform(0.5, 2.0)
    current_temp = baseline_temp + warming_factor
    await ctx.send(f'🌍 Глобальная температура с учетом потепления: примерно {current_temp:.2f} °C.')
    bot.run("")

