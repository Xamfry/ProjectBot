import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# help
@client.command()
async def f_help(ctx):
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(title="Навигаця по коммандам(возможны недоработки)", colour=discord.Color.orange())
    emb.add_field(
        name='{0}math'.format("!"),
        value="Калькулятор"
    )
    emb.add_field(
        name='{0}CityRu_help'.format("!"),
        value="Номер города России"
    )
    emb.add_field(
        name='{0}CityRu (1 - 42)'.format("!"),
        value="Время в городе \n Советую ознакомиться с городами (!CityRu_help)"
    )
    emb.add_field(
        name='{0}kurs_help'.format("!"),
        value="Номер курса"
    )
    emb.add_field(
        name='{0}kurs (1 - 2)'.format("!"),
        value="Курс к рублю \n Советую ознакомиться курсами (!kurs_help)"
    )
    emb.add_field(
        name='{0}games'.format("!"),
        value="Мини-игры"
    )
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=emb)
