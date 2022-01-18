import datetime
import discord

from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# unban
@client.command()
@commands.has_role(CREATOR)
async def f_unban(ctx, member: discord.Member):
    init(autoreset=True)
    now = datetime.datetime.now()
    # channel = client.get_channel()
    # try:
    #     emb = discord.Embed( title = "Юзер разбанен", colour = discord.Color.red())
    #     emb.add_field(name ='Администратор',value=ctx.message.author.mention,inline=False)
    #     emb.add_field(name ='Разбаненный',value=member.mention,inline=False)
    #     await ctx.channel.purge( limit=1 )
    #     await ctx.channel.send (embed = emb)
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!unban'".format(ctx))
    #     print(Fore.GREEN + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} разбанил '{1}'".format(ctx, member))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!unban'! Принимаются значения: ИМЯ.:no_entry:"))
    emb = discord.Embed(
        title="Юзер разбанен",
        colour=discord.Color.red()
    )
    emb.add_field(
        name='Администратор',
        value=ctx.message.author.mention,
        inline=False
    )
    emb.add_field(
        name='Разбаненный',
        value=member.mention,
        inline=False
    )
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(embed=emb)
    print(
        Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!unban'".format(ctx))
    print(Fore.GREEN + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} разбанил '{1}'".format(ctx, member))
