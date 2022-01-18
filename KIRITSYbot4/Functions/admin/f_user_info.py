import datetime
import discord

from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# user_info
@client.command()
@commands.has_role(CREATOR)
async def f_user_info(ctx, member: discord.Member):
    init(autoreset=True)
    now = datetime.datetime.now()
    # channel = client.get_channel()
    # try:
    #     roles = [role for role in member.roles]
    #     emb = discord.Embed(title = 'Информация о пользователе', color = 0x1e8704)
    #     emb.add_field(name='Когда присоеденился:',value=member.joined_at.strftime("{%d-%m-%Y %H:%M:%S} GMT"),inline=False)
    #     emb.add_field(name='Имя:',value=member.display_name,inline=False)
    #     emb.add_field(name='ID:',value=member.id,inline=False)
    #     emb.add_field(name='Аккаунт был создан:',value=member.created_at.strftime("{%d-%m-%Y %H:%M:%S} GMT"),inline=False)
    #     emb.add_field(name=f'Роли:',value=''.join(role.mention for role in roles),inline=False)
    #     emb.add_field(name='Основная роль:',value=member.top_role.mention,inline=False)
    #     emb.add_field(name='бот?',value=member.bot,inline=False)
    #     emb.set_thumbnail(url=member.avatar_url)
    #     await ctx.channel.purge( limit=1 )
    #     await ctx.channel.send(embed = emb)
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S')+ " - " + "{0.author} посмотрел информацию о юзере {1}".format(ctx, member))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!user_info'! Принимаются значения: ИМЯ.:no_entry:"))
    roles = [role for role in member.roles]
    emb = discord.Embed(
        title='Информация о пользователе',
        color=0x1e8704
    )
    emb.add_field(
        name='Когда присоеденился:',
        value=member.joined_at.strftime("%d-%m-%Y %H:%M:%S GMT"),
        inline=False
    )
    emb.add_field(
        name='Имя:',
        value=member.display_name,
        inline=False
    )
    emb.add_field(
        name='ID:',
        value=member.id,
        inline=False
    )
    emb.add_field(
        name='Аккаунт был создан:',
        value=member.created_at.strftime("%d-%m-%Y %H:%M:%S GMT"),
        inline=False
    )
    emb.add_field(
        name=f'Роли:',
        value=''.join(role.mention for role in roles),
        inline=False
    )
    emb.add_field(
        name='Основная роль:',
        value=member.top_role.mention,
        inline=False
    )
    emb.add_field(
        name='бот?',
        value=member.bot,
        inline=False
    )
    emb.set_thumbnail(url=member.avatar_url)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(embed=emb)
    print(
        Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} посмотрел информацию о юзере {1}".format(
            ctx, member))
