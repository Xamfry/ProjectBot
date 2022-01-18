import discord
import random

from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# card
@client.command()
async def f_card(channel, author):
    await channel.send(embed=discord.Embed(description=f"Поиграем в 21? :smirk:\n"))
    count = 0
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(koloda)
    while True:
        await channel.send(embed=discord.Embed(description=f"Будете брать карту? y/n\n"))
        choice = await client.wait_for('message',
                                       check=lambda message: message.author == message.author and message != "")
        choice = choice.content
        if choice.lower() == 'y':
            current = koloda.pop()
            await channel.send(embed=discord.Embed(description=f'Вам попалась карта достоинством %d' % current))
            count += current
            if count > 21:
                await channel.send(embed=discord.Embed(description=f':coffin: Извините, но вы проиграли :coffin:'))
                break
            elif count == 21:
                await channel.send(embed=discord.Embed(description=f'Поздравляю, вы набрали 21!'))
                break
            else:
                await channel.send(embed=discord.Embed(description=f'У вас %d очков.' % count))
        elif choice.lower() == 'n':
            await channel.send(embed=discord.Embed(description=f'У вас %d очков и вы закончили игру.' % count))
            break
