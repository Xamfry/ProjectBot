import datetime
import discord
from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# admin_panel
@client.command()
@commands.has_role(CREATOR)
async def f_admin_panel(ctx):
    init(autoreset=True)
    now = datetime.datetime.now()
    # try:
    #     emb = discord.Embed( title = "Навигаця по коммандам админа", colour = discord.Color.orange())
    #     emb.add_field( name = '{0}clear'.format( "!" ), value = "Очистка чата")
    #     emb.add_field( name = '{0}mute'.format( "!" ), value = "Мут")
    #     emb.add_field( name = '{0}unmute'.format( "!" ), value = "Размут")
    #     emb.add_field( name = '{0}kick'.format( "!" ), value = "Кик")
    #     emb.add_field( name = '{0}ban'.format( "!" ), value = "Бан")
    #     emb.add_field( name = '{0}unban'.format( "!" ), value = "Разбан(не работает)")
    #     emb.add_field( name = '{0}user_info'.format( "!" ), value = "Инфа о юзере")
    #     emb.add_field( name = '{0}give_role'.format( "!" ), value = "Дать роль")
    #     emb.add_field( name = '{0}remove_role'.format( "!" ), value = "Забрать роль")
    #     emb.add_field( name = '{0}random_password'.format( "!" ), value = "Дать рандомный пароль в личку")
    #     await ctx.channel.purge( limit=1 )
    #     await ctx.send( embed = emb)
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!admin_panel'".format(ctx))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!admin_panel'! Принимаются только команда без чисел и лишних знаков.:no_entry:"))
    emb = discord.Embed(
        title="Навигаця по коммандам админа",
        colour=discord.Color.orange()
    )
    emb.add_field(
        name='{0}clear'.format("!"),
        value="Очистка чата"
    )
    emb.add_field(
        name='{0}mute'.format("!"),
        value="Мут"
    )
    emb.add_field(
        name='{0}unmute'.format("!"),
        value="Размут"
    )
    emb.add_field(
        name='{0}kick'.format("!"),
        value="Кик"
    )
    emb.add_field(
        name='{0}ban'.format("!"),
        value="Бан"
    )
    emb.add_field(
        name='{0}unban'.format("!"),
        value="Разбан(не работает)"
    )
    emb.add_field(
        name='{0}user_info'.format("!"),
        value="Инфа о юзере"
    )
    emb.add_field(
        name='{0}give_role'.format("!"),
        value="Дать роль"
    )
    emb.add_field(
        name='{0}remove_role'.format("!"),
        value="Забрать роль"
    )
    emb.add_field(
        name='{0}random_password'.format("!"),
        value="Дать рандомный пароль в личку"
    )
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=emb)
    print(Fore.YELLOW + now.strftime(
        '%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!admin_panel'".format(ctx))
