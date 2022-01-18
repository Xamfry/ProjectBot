from Spiski.kurs_Info import kurs_Info
from bs4 import BeautifulSoup
import requests, discord
from discord.ext import commands
from Spiski.config import VALUTA

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# kurs
@client.command()
async def f_kurs(ctx, limit):
    channel = client.get_channel(VALUTA)
    # try:
    emb = discord.Embed(
        title=kurs_Info[int(limit)][1],
        color=discord.Colour.orange(),
        url=kurs_Info[int(limit)][2]
    )
    emb.set_author(
        name=client.user.name,
        icon_url=client.user.avatar_url
    )
    emb.set_footer(
        text=ctx.author.name,
        icon_url=ctx.author.avatar_url
    )
    kurs_link = kurs_Info[int(limit)][2]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.154'}
    full_page_1 = requests.get(kurs_link, headers=headers)
    soup = BeautifulSoup(full_page_1.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
    emb.add_field(name="Курс " + kurs_Info[int(limit)][3] + " к рублю" + ": ", value=f"{convert[0].text}")
    await ctx.channel.purge(limit=1)
    await channel.send(embed=emb)
    # except Exception:
    # await channel.send(embed = discord.Embed(description = f"Неверный формат комманды 'kurs'! Принимаются только числа."))
