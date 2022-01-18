import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

from Spiski.InfoCity_Ru import InfoCity_Ru
from Spiski.config import TIME_GRADUS

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# CityRu
@client.command()
async def f_CityRu(ctx, limit):
    channel = client.get_channel(TIME_GRADUS)
    # try:
    #     #timeserver
    #     emb = discord.Embed( title = InfoCity_Ru[int(limit)][3], color = discord.Colour.orange(), url = InfoCity_Ru[int(limit)][2])
    #     emb.set_author(name = client.user.name, icon_url= client.user.avatar_url)
    #     emb.set_footer(text = ctx.author.name, icon_url= ctx.author.avatar_url)
    #     InfoCity_Link_1 = InfoCity_Ru[int(limit)][2]
    #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.154'}
    #     full_page_1 = requests.get(InfoCity_Link_1, headers = headers)
    #     soup = BeautifulSoup(full_page_1.content, 'html.parser')
    #     convert_hours = soup.findAll("span", {"class": "hours"})
    #     convert_minutes = soup.findAll("span", {"class": "minutes"})
    #     convert_second = soup.findAll("span", {"class": "seconds"})

    #     #yandex
    #     InfoCity_Link_2 = InfoCity_Ru[int(limit)][4]
    #     full_page_2 = requests.get(InfoCity_Link_2, headers = headers)
    #     soup = BeautifulSoup(full_page_2.content, 'html.parser')
    #     convert_condition = soup.findAll("div", {"class": "link__condition day-anchor i-bem"})#Пасмурно
    #     convert_term_value = soup.findAll("div", {"class": "term__value"})#93%
    #     convert_icon_fact_pressure = soup.findAll("div", {"class": "term term_orient_v fact__pressure"})#
    #     InfoCity_Link_3 = InfoCity_Ru[int(limit)][5]

    #     #weather.com
    #     full_page_3 = requests.get(InfoCity_Link_3, headers = headers)
    #     soup = BeautifulSoup(full_page_3.content, 'html.parser')
    #     convert_temperatur = soup.findAll("span", {"class": "CurrentConditions--tempValue--3KcTQ"})# +6°

    #     emb.add_field(name = "Время в " + InfoCity_Ru[int(limit)][1] + " : ", value = f"{convert_hours[0].text} : {convert_minutes[0].text} : {convert_second[0].text}")
    #     emb.add_field(name = 'Температура: ', value = f"{convert_temperatur[0].text}\n{convert_condition[0].text}\nВлажность: {convert_term_value[0].text}\nДавление: {convert_icon_fact_pressure[0].text}")
    #     await ctx.channel.purge( limit=1 )
    #     await ctx.send( embed = emb)
    # except Exception:
    #     emb = discord.Embed( title = "Неверный формат комманды 'CityRu'! Принимаются только числа.", colour = discord.Color.orange())
    #     await ctx.channel.purge( limit=1 )
    #     await ctx.send(embed = emb)

    # timeserver
    emb = discord.Embed(
        title=InfoCity_Ru[int(limit)][3],
        color=discord.Colour.orange(),
        url=InfoCity_Ru[int(limit)][2]
    )
    # emb.set_author(name = client.user.name, icon_url= client.user.avatar_url)
    # emb.set_footer(text = ctx.author.name, icon_url= ctx.author.avatar_url)
    InfoCity_Link_1 = InfoCity_Ru[int(limit)][2]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.154'}
    full_page_1 = requests.get(InfoCity_Link_1, headers=headers)
    soup = BeautifulSoup(full_page_1.content, 'html.parser')
    convert_hours = soup.findAll("span", {"class": "hours"})
    convert_minutes = soup.findAll("span", {"class": "minutes"})
    convert_second = soup.findAll("span", {"class": "seconds"})

    # yandex
    InfoCity_Link_2 = InfoCity_Ru[int(limit)][4]
    full_page_2 = requests.get(InfoCity_Link_2, headers=headers)
    soup = BeautifulSoup(full_page_2.content, 'html.parser')
    convert_condition = soup.findAll("div", {"class": "link__condition day-anchor i-bem"})  # Пасмурно
    convert_term_value = soup.findAll("div", {"class": "term__value"})  # 93%
    convert_icon_fact_pressure = soup.findAll("div", {"class": "term term_orient_v fact__pressure"})  #
    InfoCity_Link_3 = InfoCity_Ru[int(limit)][5]

    # weather.com
    full_page_3 = requests.get(InfoCity_Link_3, headers=headers)
    soup = BeautifulSoup(full_page_3.content, 'html.parser')
    convert_temperatur = soup.findAll("span", {"class": "CurrentConditions--tempValue--3KcTQ"})  # +6°

    emb.add_field(
        name="Время в " + InfoCity_Ru[int(limit)][1] + " : ",
        value=f"{convert_hours[0].text} : {convert_minutes[0].text} : {convert_second[0].text}")
    emb.add_field(
        name='Температура: ',
        value=f"{convert_temperatur[0].text}\n{convert_condition[0].text}\n \
            Влажность: {convert_term_value[0].text}\n \
            Давление: {convert_icon_fact_pressure[0].text}")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=emb)
