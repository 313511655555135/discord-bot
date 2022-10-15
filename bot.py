import discord
from discord.ext import commands
import json
with open('config.json', "r", encoding = "utf8") as file:
    data = json.load(file)

bot = commands.Bot(command_prefix = 'c/', intents = discord.Intents().all())

@bot.event
async def on_ready():
    print("Ready!")

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'延遲：{round(bot.latency*1000)}毫秒')

@bot.command()
async def test(ctx):
    url.get('https://od.moi.gov.tw/MOI/v1/pbs')

bot.run(data['token'])
