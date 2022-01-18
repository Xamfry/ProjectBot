import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# kurs_help
@client.command()
async def f_kurs_help(ctx):
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(
        title="Курс к рублю",
        colour=discord.Color.orange()
    )
    emb.add_field(
        name='Курс и номер{0}'.format(":"),
        value="Доллар - 1 \n Евро - 2"
    )
    await ctx.send(embed=emb)
