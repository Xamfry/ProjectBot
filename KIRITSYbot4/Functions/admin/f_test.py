import datetime
import discord

from colorama import init, Fore
from discord.ext import commands
from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# test
@client.command()
@commands.has_role(CREATOR)
async def f_test(ctx):
    init(autoreset=True)
    now = datetime.datetime.now()
    # try:
    #     await ctx.channel.purge( limit=1 )
    #     await ctx.send(embed = discord.Embed(description = f'Бот запущен'))
    #     print(Fore.YELLOW + now.strftime(STRFTIME) + " - " +"{0.author} использовал команду '!test'".format(ctx))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!test'! Принимаются только команда без чисел и лишних знаков.:no_entry:"))
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=discord.Embed(description=f'Бот запущен', colour=discord.Color.green()))
    print(
        Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!test'".format(ctx))
