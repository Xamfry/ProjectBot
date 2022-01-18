"""
ВРЕМЕННО НЕ РАБОТАЕТ
"""
import discord
import random

from discord.ext import commands

from Spiski.config import CREATOR

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# random_password
@commands.has_role(CREATOR)
@client.command()
async def f_random_password(ctx, member: discord.Member):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    await ctx.send(embed=discord.Embed(
        description=f'Количество паролей?\n Не советую использовать много паролей, иначе сообщения будут иметь характер спама'))
    number = await client.wait_for('message', check=lambda message: message.author == ctx.author and message != "")
    number = int(number.content)
    await ctx.send(embed=discord.Embed(description=f'Длина пароля?\n Ограничение: 2000 символов'))
    length = await client.wait_for('message', check=lambda message: message.author == ctx.author and message != "")
    length = int(length.content)
    await ctx.channel.purge(limit=5)
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        await member.send(f"Ваш пароль: <---  {password}  --->")
