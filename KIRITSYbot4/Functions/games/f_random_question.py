import discord
import random

from discord.ext import commands

from Spiski.config import RANDOM_QUESTION

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# random_question
@client.command()
async def f_random_question(ctx):
    channel = client.get_channel(RANDOM_QUESTION)
    await channel.send(embed=discord.Embed(description=f'Это небольшой тест'))
    await channel.send(embed=discord.Embed(description=f'Какого числа будет пасмурно?'))
    number = await client.wait_for('message', check=lambda message: message.author == ctx.author and message != "")
    number = number.content
    if number == '0':
        await channel.send(embed=discord.Embed(description=f'Такого числа нет в месяце!'))
        await channel.send(embed=discord.Embed(
            description=f'Варианты ответов:\nМой ответ - 0, так что работай программа (1); \n Вы не уточнили, что число именно в месяце,так что - 0 (2); \n Ладно, не прокатило (3)'))
        number_korona = await client.wait_for('message',
                                              check=lambda message: message.author == ctx.author and message != "")
        number_korona = number_korona.content
        if number_korona == '1':
            await channel.send(embed=discord.Embed(
                description=f'Не думала, что вы так далеко зайдете, поэтому прошу меня простить и принять билет в Италию.'))
            return
        elif number_korona == '2':
            await channel.send(embed=discord.Embed(
                description=f'Не думала, что вы так далеко зайдете, поэтому прошу меня простить и принять билет в Италию.'))
            return
        elif number_korona == '3':
            await f_random_question(ctx)
    if number > '31':
        await channel.send(embed=discord.Embed(
            description=f'Такого числа нет в месяце!\n Серьезно? Не ври, в месяце максимум 31 день, а не твое число. Либо вводишь нормальный день (1), либо в Италию (2). Выбирай.'))
        number_korona = await client.wait_for('message',
                                              check=lambda message: message.author == ctx.author and message != "")
        number_korona = number_korona.content
        if number_korona == '1':
            await f_random_question(ctx)
        elif number_korona == '2':
            await channel.send(embed=discord.Embed(description=f'В Италию, так в Италию...'))
            return
    if number < '1':
        await channel.send(embed=discord.Embed(
            description=f'Такого числа нет в месяце!\n Серьезно, ну откуда в мире такой день? Либо вводишь нормальный день (1), либо в США (2). Выбирай.'))
        number_korona = await client.wait_for('message',
                                              check=lambda message: message.author == ctx.author and message != "")
        number_korona = number_korona.content
        if number_korona == '1':
            await f_random_question(ctx)
        elif number_korona == '2':
            await channel.send(embed=discord.Embed(description=f'В США, так в США...'))
    for i in range(number):
        a = random.choice(list)
        list.remove(a)
        await channel.send(embed=discord.Embed(description=f'Вопрос: {a}'))
        questions = await client.wait_for('message',
                                          check=lambda message: message.author == ctx.author and message != "")
        questions = questions.content
        await channel.send(embed=discord.Embed(description=f'Ваш ответ: {questions}'))
    await channel.send(embed=discord.Embed(description=f'Еще раз (1) или все (2) ?'))
    rel = await client.wait_for('message', check=lambda message: message.author == ctx.author and message != "")
    rel = rel.content
    if rel == '1':
        await f_random_question(ctx)
    elif rel == '2':
        return
    else:
        return
