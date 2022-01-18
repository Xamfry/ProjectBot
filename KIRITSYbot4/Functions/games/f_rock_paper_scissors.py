import discord
import random

from discord.ext import commands

from Spiski.config import ROCK_PAPER_SCISSORS
from Spiski.rock_paper_scissors_output import rock_paper_scissors_list

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# rock_paper_scissors
@client.command()
async def f_rock_paper_scissors(ctx):
    channel = client.get_channel(ROCK_PAPER_SCISSORS)
    await channel.send(embed=discord.Embed(description=f'камень-ножницы-бумага с ботом\n Соблюдайте нижний регистр'))
    number = await client.wait_for('message', check=lambda message: message.author == ctx.author and message != "")
    number = number.content
    await ctx.channel.purge(limit=3)
    random_number = random.choice(rock_paper_scissors_list)
    if number == 'камень':
        if random_number == 1:
            await channel.send(embed=discord.Embed(
                description=f'Камень не бьет камень, ведь камень камню камень! Ничья, братья камни! \n Ничья!'))
        if random_number == 2:
            await channel.send(embed=discord.Embed(
                description=f'Камень побил ножницы и ему за это ничего не будет, он ведь белорусский омоновец! Блистательная победа над народом! \n Камень победил ножницы!'))
        if random_number == 3:
            await channel.send(embed=discord.Embed(
                description=f'Мнонеуважаемый господин камень был обёрнут бумагой, как лохня и законно проиграл от недостатка мощности его дубинки! Это проигрыш он запомнит на всю свою жизнь, ведь такого поражения он явно не ожидал! \n Камень проиграл бумаге!'))

    if number == 'ножницы':
        if random_number == 1:
            await channel.send(embed=discord.Embed(
                description=f'Увы, господа ножницы не побили многоуважаемых каменных омоновцив и заслуженно пошли за решётку! Жыве беларусь! \n Ножницы проиграли камню!'))
        if random_number == 2:
            await channel.send(embed=discord.Embed(
                description=f'Ножницы не посмеют ударить своих активистов, ибо каждый голос - сила(где то в мире смеется один Лукашенко)! Определённо ничья! \n Ничья!'))
        if random_number == 3:
            await channel.send(embed=discord.Embed(
                description=f'А мы что, мы ничего, так, собираем митинки, воюем, ничего не обычного. В смысле есть святые мощи лукашенко, которое спасают от ковида? а что нас не позвали? А ну бегом в церкви. С тех пор их больше никто не видел \n Ножницы победили бумагу!'))

    if number == 'бумага':
        if random_number == 1:
            await channel.send(embed=discord.Embed(
                description=f'Бумага обернула господов омоновцев, ведь против РПЦ никакая резиновая сила не устоит. А проиграли, потому что РПЦ явно не с тем приводом приус купили! Это растянувшаяся битва даст жару любой вечеринке, на которой ты обязан побывать! \n Бумага победила камень!'))
        if random_number == 2:
            await channel.send(embed=discord.Embed(
                description=f'Опять вы? Да как вы выжили то? Так, у нас акция, две свечки по цене одной; Генерал, надеюсь, что вы сказали, что это свечки в 5 точку? Ааа, да, кнш, не парьтесь. \n Бумага проиграла ножницам!'))
        if random_number == 3:
            await channel.send(embed=discord.Embed(
                description=f'Внимание, начались массовые беспорядки кадилов. Внимание, РПЦ, этот мел мы пустим на лекарства, а вам дадим кристалы. Забористые такие, с персиком, покрытым сливками или клубникой в шоколадке \n Ничья!'))
