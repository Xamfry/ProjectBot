import datetime
import discord

from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# give_role
@client.command()
@commands.has_role(CREATOR)
async def f_give_role(ctx, member: discord.Member, role: discord.Role):
    init(autoreset=True)
    now = datetime.datetime.now()
    # channel = client.get_channel()
    # try:
    #     add_role = discord.utils.get(ctx.guild.roles, id = role.id)
    #     await ctx.channel.purge( limit=1 )
    #     await member.add_roles(add_role)
    #     await ctx.channel.send(embed = discord.Embed(description = f'{member.mention} выдана роль {role.mention}'))
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!give_role'".format(ctx))
    #     print(Fore.GREEN + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} выдал '{1}' роль {2} ".format(ctx, member, role))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!give_role'! Принимаются значения: ИМЯ, РОЛЬ.:no_entry:"))
    add_role = discord.utils.get(ctx.guild.roles, id=role.id)
    await ctx.channel.purge(limit=1)
    await member.add_roles(add_role)
    await ctx.channel.send(embed=discord.Embed(description=f'{member.mention} выдана роль {role.mention}'))
    print(
        Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!give_role'".format(
            ctx))
    print(
        Fore.GREEN + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} выдал '{1}' роль {2} ".format(ctx, member,
                                                                                                           role))
