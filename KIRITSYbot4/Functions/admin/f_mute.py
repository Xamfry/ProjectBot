import asyncio
import datetime
import discord

from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR, ADMIN, MUTE

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# mute
@client.command()
@commands.has_role(CREATOR)
async def f_mute(ctx, member: discord.Member, time, permission, reason):
    init(autoreset=True)
    now = datetime.datetime.now()
    # channel = client.get_channel()
    # try:
    #     admin_remove = discord.utils.get(ctx.guild.roles, id=ADMIN)
    #     muterole_add = discord.utils.get(ctx.guild.roles, id=MUTE)
    #     emb = discord.Embed( title = "Юзер замучен", colour = discord.Color.red())
    #     emb.add_field(name ='Администратор',value=ctx.message.author.mention,inline=False)
    #     emb.add_field(name ='Замученный',value=member.mention,inline=False)
    #     emb.add_field(name ='Причина',value=reason,inline=False)
    #     emb.add_field(name ='Время(мин)',value=time,inline=False)
    #     if permission == 0:
    #         emb.add_field(name ='Роль админа вернется?',value='Нет',inline=False)
    #     if permission == 1:
    #         emb.add_field(name ='Роль админа вернется?',value='Да',inline=False)
    #     await ctx.channel.purge( limit=1 )
    #     await member.remove_roles(admin_remove)
    #     await member.add_roles(muterole_add)
    #     await ctx.channel.send(embed = emb)
    #     if time == 1:
    #         if permission == 0:
    #             print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!mute'".format(ctx))
    #             print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} дал мут '{1}' на '{2} минуту', Причина: {3}, роль админа не вернется!.".format(ctx, member, time, reason, permission))
    #         if permission == 1:
    #             print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!mute'".format(ctx))
    #             print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} дал мут '{1}' на '{2} минуту', Причина: {3}, роль админа вернется.".format(ctx, member, time, reason, permission))
    #     if time == 2 or time == 3 or time == 4:
    #         if permission == 0:
    #             print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!mute'".format(ctx))
    #             print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} дал мут '{1}' на '{2} минуты', Причина: {3}, роль админа не вернется.".format(ctx, member, time, reason, permission))
    #         if permission == 1:
    #             print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!mute'".format(ctx))
    #             print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} дал мут '{1}' на '{2} минуты', Причина: {3}, роль админа вернется.".format(ctx, member, time, reason, permission))
    #     if time > 4:
    #         if permission == 0:
    #             print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!mute'".format(ctx))
    #             print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} дал мут '{1}' на '{2} минут', Причина: {3}, роль админа не вернется.".format(ctx, member, time, reason, permission))
    #         if permission == 1:
    #             print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!mute'".format(ctx))
    #             print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} дал мут '{1}' на '{2} минуты', Причина: {3}, роль админа вернется.".format(ctx, member, time, reason, permission))
    #     await asyncio.sleep(time*60)
    #     await member.remove_roles(muterole_add)
    #     if permission == 1:
    #         await member.add_roles(admin_remove)
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!mute'! Принимаются значения: ИМЯ, ВРЕМЯ, ПРИЧИНА, РОЛЬ АДМИНА.:no_entry:"))
    admin_remove = discord.utils.get(ctx.guild.roles, id=ADMIN)
    muterole_add = discord.utils.get(ctx.guild.roles, id=MUTE)
    emb = discord.Embed(title="Юзер замучен", colour=discord.Color.red())
    emb.add_field(
        name='Администратор',
        value=ctx.message.author.mention,
        inline=False
    )
    emb.add_field(
        name='Замученный',
        value=member.mention,
        inline=False
    )
    emb.add_field(
        name='Причина',
        value=reason,
        inline=False
    )
    emb.add_field(
        name='Время(мин)',
        value=time,
        inline=False
    )
    if permission == 0:
        emb.add_field(
            name='Роль админа вернется?',
            value='Нет',
            inline=False
        )
    if permission == 1:
        emb.add_field(
            name='Роль админа вернется?',
            value='Да',
            inline=False
        )
    await ctx.channel.purge(limit=1)
    await member.remove_roles(admin_remove)
    await member.add_roles(muterole_add)
    await ctx.channel.send(embed=emb)
    if time == 1:
        if permission == 0:
            print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} использовал команду '!mute'".format(ctx))
            print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} дал мут '{1}' на '{2} минуту', Причина: {3}, роль админа не вернется!.".format(ctx,
                                                                                                               member,
                                                                                                               time,
                                                                                                               reason,
                                                                                                               permission))
        if permission == 1:
            print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} использовал команду '!mute'".format(ctx))
            print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} дал мут '{1}' на '{2} минуту', Причина: {3}, роль админа вернется.".format(ctx, member,
                                                                                                           time, reason,
                                                                                                           permission))
    if time == 2 or time == 3 or time == 4:
        if permission == 0:
            print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} использовал команду '!mute'".format(ctx))
            print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} дал мут '{1}' на '{2} минуты', Причина: {3}, роль админа не вернется.".format(ctx,
                                                                                                              member,
                                                                                                              time,
                                                                                                              reason,
                                                                                                              permission))
        if permission == 1:
            print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} использовал команду '!mute'".format(ctx))
            print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} дал мут '{1}' на '{2} минуты', Причина: {3}, роль админа вернется.".format(ctx, member,
                                                                                                           time, reason,
                                                                                                           permission))
    if time > 4:
        if permission == 0:
            print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} использовал команду '!mute'".format(ctx))
            print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} дал мут '{1}' на '{2} минут', Причина: {3}, роль админа не вернется.".format(ctx,
                                                                                                             member,
                                                                                                             time,
                                                                                                             reason,
                                                                                                             permission))
        if permission == 1:
            print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} использовал команду '!mute'".format(ctx))
            print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " \
                  + "{0.author} дал мут '{1}' на '{2} минуты', Причина: {3}, роль админа вернется.".format(ctx, member,
                                                                                                           time, reason,
                                                                                                           permission))
    await asyncio.sleep(time * 60)
    await member.remove_roles(muterole_add)
    if permission == 1:
        await member.add_roles(admin_remove)
