import datetime
import discord

from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# clear
@client.command()
@commands.has_role(CREATOR)
async def f_clear(ctx, amout):
    init(autoreset=True)
    now = datetime.datetime.now()
    # try:        
    #     await ctx.channel.purge( limit=int(amout) )
    #     await ctx.send(embed = discord.Embed(description = f':white_check_mark: удалено сообщений {amout} :white_check_mark:'))
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!clear'".format(ctx))
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} очистил сообщений '{1}' на канале '{0.channel}'".format(ctx, amout))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!clear'! Принимаются только числа.:no_entry:"))
    # except errors.MissingPermissions:
    #     await ctx.send(Embed = discord.Embed(description = f":no_entry: Недостаточно прав :no_entry:"))
    await ctx.channel.purge(limit=int(amout))
    await ctx.send(embed=discord.Embed(description=f':white_check_mark: удалено сообщений {amout} :white_check_mark:'))
    print(
        Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!clear'".format(ctx))
    print(Fore.YELLOW + now.strftime(
        '%d-%m-%Y %H:%M:%S') + " - " + "{0.author} очистил сообщений '{1}' на канале '{0.channel}'".format(ctx, amout))

    
