import datetime
import discord
from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


@client.command()
@commands.has_role(CREATOR)
async def f_add_word(ctx, word):
    init(autoreset=True)
    now = datetime.datetime.now()
    with open('Spiski\\bad_word.txt', 'a') as f:
        f.write(word + '\n')
    await ctx.send(embed=discord.Embed(description=f'Слово "{word}" добавлено в список'))
    print(
        Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} добавил слово '{1}' в список мата".format(
            ctx, word))
