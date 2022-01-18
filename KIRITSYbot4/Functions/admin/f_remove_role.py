import datetime
import discord

from colorama import init, Fore
from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# remove_role
@client.command()
@commands.has_role(CREATOR)
async def f_remove_role(ctx, member: discord.Member, role: discord.Role):
    init(autoreset=True)
    now = datetime.datetime.now()
    # channel = client.get_channel()
    # try:
    #     remove_role = discord.utils.get(ctx.guild.roles, id = role.id)
    #     await ctx.channel.purge( limit=1 )
    #     await member.remove_roles(remove_role)
    #     await ctx.channel.send(embed = discord.Embed(description = f'У {member.mention} забрали роль {role.mention}'))
    #     print(Fore.YELLOW + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!remove_role'".format(ctx))
    #     print(Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} забрал у '{1}' роль {2} ".format(ctx, member, role))
    # except Exception:
    #     await ctx.send(embed = discord.Embed(description = f":no_entry: Неверный формат комманды '!remove_role'! Принимаются значения: ИМЯ, РОЛЬ.:no_entry:"))
    remove_role = discord.utils.get(ctx.guild.roles, id=role.id)
    await ctx.channel.purge(limit=1)
    await member.remove_roles(remove_role)
    await ctx.channel.send(embed=discord.Embed(description=f'У {member.mention} забрали роль {role.mention}'))
    print(Fore.YELLOW + now.strftime(
        '%d-%m-%Y %H:%M:%S') + " - " + "{0.author} использовал команду '!remove_role'".format(ctx))
    print(
        Fore.RED + now.strftime('%d-%m-%Y %H:%M:%S') + " - " + "{0.author} забрал у '{1}' роль {2} ".format(ctx, member,
                                                                                                            role))
