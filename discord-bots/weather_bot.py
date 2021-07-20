import discord
from discord.ext import commands
import requests
import json
import os
 
client = commands.Bot(command_prefix=".")
 
 
os.chdir(r'C:\Users\Gagandeep Singh\Desktop\bot')
 
with open('data/api_key.json', 'r') as f:
    api_key = json.load(f)
 
@client.command()
@commands.cooldown(2, 1, commands.BucketType.default)
async def weather(ctx, city, country = None):
 
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=imperial&appid={api_key['api_key']}")
    json_data = r.json()
 
    weather = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    icon = "http://openweathermap.org/img/wn/" + json_data['weather'][0]['icon'] + "@2x.png"
 
    print(weather, description, temp)
 
    embed = discord.Embed(
        title="Current Weather",
        description=f"{city.upper()}",
        color=discord.Color.dark_blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name=weather, value=description, inline=False)
    embed.add_field(name="Temperature", value=f"{temp}\u2109", inline=False)
 
    await ctx.send(embed=embed)
 
 
@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("That is not a valid city or country code.")
 

@client.event
async def on_ready():
    print('Bot is online')
    
client.run('TOKEN')
