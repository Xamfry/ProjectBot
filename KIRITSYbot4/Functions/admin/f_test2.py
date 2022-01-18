import datetime
import discord
import json
from colorama import init, Fore


async def f_test2(ctx):
    init(autoreset=True)
    now = datetime.datetime.now()
    # try:
    #     await ctx.channel.purge( limit=1 )
    #     await ctx.send(embed = discord.Embed(description = f'Бот запущен'))
    #     print(Fore.YELLOW + now.strftime(STRFTIME) + " - " +"{0.author} использовал команду '!test'".format(ctx))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!test'! Принимаются только команда без чисел и лишних знаков.:no_entry:"))
    await ctx.purge(limit=1)
    await ctx.send(embed=discord.Embed(description=f'Бот запущен', colour=discord.Color.green()))
    print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + f"{ctx.author.name} использовал команду '_test'")
