import discord
import random

from discord.ext import commands

from Spiski.coin_list import coin_list
from Spiski.config import COIN

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# coin
@client.command()
async def f_coin(ctx):
    channel = client.get_channel(COIN)
    await channel.send(embed=discord.Embed(description=f'орёл или решка?\n Соблюдайте регистр'))
    number = await client.wait_for('message', check=lambda message: message.author == ctx.author and message != "")
    number = number.content
    random_number = random.choice(coin_list)
    if number == 'орёл':
        if number == random_number:
            await channel.send(embed=discord.Embed(description=f'Поздравляю, вы выиграли'))
        else:
            await channel.send(embed=discord.Embed(description=f'Сожалею, но вы проиграли'))
    if number == 'решка':
        if number == random_number:
            await channel.send(embed=discord.Embed(description=f'Поздравляю, вы выиграли'))
        else:
            await channel.send(embed=discord.Embed(description=f'Сожалею, но вы проиграли'))
