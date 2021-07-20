import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('Bot is online')

@client.command()
@commands.is_owner()
async def clear(ctx, amount, month=None, day=None, year=None):
    if amount == "-":
        amount = None
    else:
        amount = int(amount) + 1
    if month == None or day == None or year == None:
        date = None
    else:
        date = datetime.datetime(int(year), int(month), int(day))

    await ctx.channel.purge(limit=amount, after=date)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission.")


@client.command()
@commands.is_owner()
async def kick(ctx, member: discord.Member, *, reason):
    await member.kick(reason=reason)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission to use this command.")


@client.command()
@commands.is_owner()
async def ban(ctx, member: discord.Member, *, reason):
    await member.ban(reason=reason)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission to use this command.")





client.run('TOKEN')
