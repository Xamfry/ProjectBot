import datetime
import discord

from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# кик
@client.command()
@commands.has_role(CREATOR)
async def f_kick(ctx, member: discord.Member, reason):
    init(autoreset=True)
    now = datetime.datetime.now()
    # channel = client.get_channel()
    # try:
    #     emb = discord.Embed( title = "Юзер кикнут", colour = discord.Color.red())
    #     emb.add_field(name ='Администратор',
    #     value=ctx.message.author.mention,inline=False)
    #     emb.add_field(name ='Кикнутый',value=member.mention,inline=False)
    #     emb.add_field(name ='Причина',value=reason,inline=False)
    #     emb.set_author( name = member.name, icon_url = member.avatar_url)
    #     await ctx.channel.purge( limit=1 )
    #     await member.kick()
    #     await ctx.channel.send (embed = emb)
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!kick'".format(ctx))
    #     print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} кикнул '{1}', Причина: {2} ".format(ctx, member, reason))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!kick'! Принимаются только числа.:no_entry:"))
    emb = discord.Embed(
        title="Юзер кикнут",
        colour=discord.Color.red()
    )
    emb.add_field(
        name='Администратор',
        value=ctx.message.author.mention,
        inline=False
    )
    emb.add_field(
        name='Кикнутый',
        value=member.mention,
        inline=False
    )
    emb.add_field(
        name='Причина',
        value=reason,
        inline=False
    )
    emb.set_author(
        name=member.name,
        icon_url=member.avatar_url
    )
    await ctx.channel.purge(limit=1)
    await member.kick()
    await ctx.channel.send(embed=emb)
    print(
        Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!kick'".format(ctx))
    print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} кикнул '{1}', Причина: {2} ".format(ctx,
                                                                                                                 member,
                                                                                                                 reason))
