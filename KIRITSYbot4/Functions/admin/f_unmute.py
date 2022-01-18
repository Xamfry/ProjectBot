import datetime
import discord

from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR, MUTE

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# unmute
@client.command()
@commands.has_role(CREATOR)
async def f_unmute(ctx, member: discord.Member):
    init(autoreset=True)
    now = datetime.datetime.now()
    # channel = client.get_channel()
    # try:
    #     muterole = discord.utils.get(ctx.guild.roles, id=MUTE)
    #     emb = discord.Embed( title = "Юзер размучен", colour = discord.Color.green())
    #     emb.add_field(name ='Администратор',value=ctx.message.author.mention,inline=False)
    #     emb.add_field(name ='Размученный',value=member.mention,inline=False)   
    #     await ctx.channel.purge( limit=1 )
    #     await ctx.channel.send(embed = emb)
    #     await member.remove_roles(muterole)
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!unmute'".format(ctx))
    #     print(Fore.GREEN + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} принудительно размутил '{1}'.".format(ctx, member))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!unmute'! Принимаются значения: ИМЯ.:no_entry:"))
    muterole = discord.utils.get(ctx.guild.roles, id=MUTE)
    emb = discord.Embed(
        title="Юзер размучен",
        colour=discord.Color.green()
    )
    emb.add_field(
        name='Администратор',
        value=ctx.message.author.mention,
        inline=False
    )
    emb.add_field(
        name='Размученный',
        value=member.mention,
        inline=False
    )
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(embed=emb)
    await member.remove_roles(muterole)
    print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!unmute'".format(
        ctx))
    print(
        Fore.GREEN + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} принудительно размутил '{1}'.".format(ctx,
                                                                                                                   member))
