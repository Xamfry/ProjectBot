import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# CityRu_help
@client.command()
async def f_CityRu_help(ctx):
    emb = discord.Embed(
        title="Время в городах России",
        colour=discord.Color.orange()
    )
    emb.add_field(
        name='Город и номер{0}'.format(":"),
        value="Москва - 1 \n Астрахань - 2 \n Барнаул - 3 \n Брянск - 4 \n \
            Владивосток - 5 \n Волгоград - 6 \n Воронеж - 7 \n Екатеринбург - 8 \n \
            Иваново - 9 \n Ижевск - 10 \n Иркутск - 11 \n Казань - 12 \n \
            Калининград - 13 \n Кемерово - 14 \n Киров - 15 \n Краснодар - 16 \n \
            Красноярск - 17 \n Липецк - 18 \n Махачкала - 19 \n Набережные Челны - 20 \n \
            Нижний Новгород - 21 \n Новокузнецк - 22 \n Новосибирск - 23 \n Омск - 24 \n \
            Оренбург - 25 \n Пенза - 26 \n Пермь - 27 \n Ростов-на-Дону - 28 \n \
            Рязань - 29 \n Самара - 30 \n Санкт-Петербург - 31 \n Саратов - 32 \n \
            Тольятти - 33 \n Томск - 34 \n Тула - 35 \n Тюмень - 36 \n Ульяновск - 37 \n \
            Уфа - 38 \n Хабаровск - 39 \n Чебоксары - 40 \n Челябинск - 41 \n Ярославль - 42"
    )
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=emb)
