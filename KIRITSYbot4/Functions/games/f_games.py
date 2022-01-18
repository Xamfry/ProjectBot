import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# games
@client.command()
async def f_games(ctx):
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(
        title="Навигаця по играм(возможны недоработки)",
        colour=discord.Color.orange()
    )
    emb.add_field(
        name='{0}card'.format("!"),
        value="Игра очко (21)"
    )
    emb.add_field(
        name='{0}coin'.format("!"),
        value="Монетка"
    )
    emb.add_field(
        name='{0}random_question'.format("!"),
        value="КоронОчка(не робiт)"
    )
    emb.add_field(
        name='{0}cross_zero'.format("!"),
        value="Крестики-нолики(не робiт)"
    )
    emb.add_field(
        name='{0}rock_paper_scissors'.format("!"),
        value="камень-ножницы-бумага"
    )
    await ctx.send(embed=emb)
