"""
ВРЕМЕННО НЕ РАБОТАЕТ
"""

import asyncio
import discord

from discord.ext import commands

from Spiski.config import CREATOR
from Spiski.rainbow_roles import roles

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# rainbow
@client.command()
@commands.has_role(CREATOR)
async def f_rainbow(ctx, member: discord.Member):
    x = 0
    while x != 1:
        for role in roles:
            add_role = discord.utils.get(ctx.guild.roles, id=role)
            await member.add_roles(add_role)
            await asyncio.sleep(1.5)
            await member.remove_roles(add_role)
