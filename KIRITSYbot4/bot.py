# -*- coding: utf-8 -*-
import datetime
import discord
import fnmatch
import os
import time
import random
import json
from colorama import init, Fore
from discord.ext import commands
# <-------------------------------------->
from Functions.admin.f_add_word import f_add_word
from Functions.admin.f_admin_panel import f_admin_panel
from Functions.admin.f_ban import f_ban
from Functions.admin.f_clear import f_clear
from Functions.admin.f_give_role import f_give_role
from Functions.admin.f_kick import f_kick
from Functions.admin.f_mute import f_mute
from Functions.admin.f_remove_role import f_remove_role
from Functions.admin.f_test import f_test
from Functions.admin.f_test2 import f_test2
from Functions.admin.f_unban import f_unban
from Functions.admin.f_unmute import f_unmute
from Functions.admin.f_user_info import f_user_info
# <-------------------------------------->
from Spiski.bad_words import *
from Spiski.coin_list import *
from Spiski.InfoCity_Ru import *
from Spiski.kurs_Info import *
from Spiski.random_question_list import *
from Spiski.rock_paper_scissors_output import *
from Spiski.config import *
from Spiski.white_list import *
from Spiski.translate_list import *

client = commands.Bot(intents=discord.Intents.all(), command_prefix='!')
client.remove_command("help")


@client.event
async def on_message(message):
    init(autoreset=True)
    now = datetime.datetime.now()
    await client.process_commands(message)
    if message.author.name in white_list:
        with open('users.json', 'r', encoding='UTF-8') as file:
            users = json.load(file)

            async def update_user_data(users, user):
                if not user in users:
                    users[user] = {}
                    users[user] = {}
                    users[user]["a - name"] = {}
                    users[user]["a - name"]["a - name"] = message.author.name
                    users[user]["a - name"]["b - admin"] = True
                    users[user]["b - messeges"] = 0
                    users[user]["c - swore"] = 0
                    users[user]["d - user_info"] = 0
                    users[user]["e - admin_panel"] = 0
                    users[user]["f - ban"] = 0
                    users[user]["g - clear"] = 0
                    users[user]["h - give_role"] = 0
                    users[user]["i - kick"] = 0
                    users[user]["j - mute"] = 0
                    users[user]["k - remove_role"] = 0
                    users[user]["l - test"] = 0
                    users[user]["m - unban"] = 0
                    users[user]["n - unmute"] = 0
                    users[user]["o - _test"] = 0

                if not "a - name" in users[user]:
                    users[user]["a - name"] = {}
                    users[user]["a - name"]["a - name"] = message.author.name
                    users[user]["a - name"]["b - admin"] = True

                if not "a - name" in users[user]["a - name"]:
                    users[user]["a - name"]["a - name"] = message.author.name

                if not "b - admin" in users[user]["a - name"]:
                    users[user]["a - name"]["b - admin"] = True

                if not "b - messeges" in users[user]:
                    users[user]["b - messeges"] = 0

                if not "c - swore" in users[user]:
                    users[user]["c - swore"] = 0

                if not "d - user_info" in users[user]:
                    users[user]["d - user_info"] = 0

                if not "e - admin_panel" in users[user]:
                    users[user]["e - admin_panel"] = 0

                if not "f - ban" in users[user]:
                    users[user]["f - ban"] = 0

                if not "g - clear" in users[user]:
                    users[user]["g - clear"] = 0

                if not "h - give_role" in users[user]:
                    users[user]["h - give_role"] = 0

                if not "i - kick" in users[user]:
                    users[user]["i - kick"] = 0

                if not "j - mute" in users[user]:
                    users[user]["j - mute"] = 0

                if not "k - remove_role" in users[user]:
                    users[user]["k - remove_role"] = 0

                if not "l - test" in users[user]:
                    users[user]["l - test"] = 0

                if not "m - unban" in users[user]:
                    users[user]["m - unban"] = 0

                if not "n - unmute" in users[user]:
                    users[user]["n - unmute"] = 0

                if not "o - _test" in users[user]:
                    users[user]["o - _test"] = 0

                users[user]["b - messeges"] += 1

            await update_user_data(users, str(message.author.id))
            with open('users.json', 'w', encoding='UTF-8') as file:
                json.dump(users, file, indent=4, sort_keys=True)

        with open('game.json', 'r', encoding='UTF-8') as file:
            users = json.load(file)
    else:
        with open('users.json', 'r', encoding='UTF-8') as file:
            users = json.load(file)

            async def update_user_data(users, user):
                if not user in users:
                    users[user] = {}
                    users[user]["a - name"] = {}
                    users[user]["a - name"]["a - name"] = message.author.name
                    users[user]["a - name"]["b - admin"] = False
                    users[user]["b - messeges"] = 0 
                    users[user]["c - swore"] = 0
                    

                if not "a - name" in users[user]:
                    users[user]["a - name"] = {}
                    users[user]["a - name"]["a - name"] = message.author.name
                    users[user]["a - name"]["b - admin"] = False

                if not "a - name" in users[user]["a - name"]:
                    users[user]["a - name"]["name"] = message.author.name

                if not "b - admin" in users[user]["a - name"]:
                    users[user]["a - name"]["b - admin"] = False

                if not "b - messeges" in users[user]:
                    users[user]["b - messeges"] = 0

                if not "c - swore" in users[user]:
                    users[user]["c - swore"] = 0

                users[user]["b - messeges"] += 1

            await update_user_data(users, str(message.author.id))
            with open('users.json', 'w', encoding='UTF-8') as file:
                json.dump(users, file, indent=4, sort_keys=True)

        with open('game.json', 'r', encoding='UTF-8') as file:
            users = json.load(file)


    async def update_game_data(users, user):
        if not user in users:
            users[user] = {}
            users[user]["_a - name"] = message.author.name
            users[user]["_coin"] = {}
            users[user]["_coin"]["use"] = 0
            users[user]["_coin"] = {}
            users[user]["_coin"]["win"] = {}
            users[user]["_coin"]["win"]["all"] = {}
            users[user]["_coin"]["win"]["all"]["a_count"] = 0
            users[user]["_coin"]["win"]["all"]["O"] = 0
            users[user]["_coin"]["win"]["all"]["R"] = 0
            users[user]["_coin"]["lose"] = {}
            users[user]["_coin"]["lose"]["all"] = {}
            users[user]["_coin"]["lose"]["all"]["a_count"] = 0
            users[user]["_coin"]["lose"]["all"]["O"] = 0
            users[user]["_coin"]["lose"]["all"]["R"] = 0
            users[user]["_card"] = {}
            users[user]["_card"]["use"] = 0
            users[user]["_card"]["win"] = 0
            users[user]["_card"]["lose"] = 0
            users[user]["_card"]["exit"] = 0
            users[user]["_random_question"] = 0  # отдельно, сколько вопросов \use
            users[user]["_cross_zero"] = 0  # отдельно для победы/поражения \use
            users[user]["_rock_paper_scissors"] = {}
            users[user]["_rock_paper_scissors"]["use"] = 0
            users[user]["_rock_paper_scissors"] = {}
            users[user]["_rock_paper_scissors"]["win"] = {}
            users[user]["_rock_paper_scissors"]["win"]["all"] = {}
            users[user]["_rock_paper_scissors"]["win"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["r/s"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["s/p"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["p/r"] = 0
            users[user]["_rock_paper_scissors"]["lose"] = {}
            users[user]["_rock_paper_scissors"]["lose"]["all"] = {}
            users[user]["_rock_paper_scissors"]["lose"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["r/p"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["s/r"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["p/s"] = 0
            users[user]["_rock_paper_scissors"]["nothing"] = {}
            users[user]["_rock_paper_scissors"]["nothing"]["all"] = {}
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["r/r"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["s/s"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["p/p"] = 0

        if not "_a - name" in users[user]:
            users[user]["_a - name"] = message.author.name

        if not "_coin" in users[user]:
            users[user]["_coin"] = {}
            users[user]["_coin"]["use"] = 0
            users[user]["_coin"] = {}
            users[user]["_coin"]["win"] = {}
            users[user]["_coin"]["win"]["all"] = {}
            users[user]["_coin"]["win"]["all"]["a_count"] = 0
            users[user]["_coin"]["win"]["all"]["O"] = 0
            users[user]["_coin"]["win"]["all"]["R"] = 0
            users[user]["_coin"]["lose"] = {}
            users[user]["_coin"]["lose"]["all"] = {}
            users[user]["_coin"]["lose"]["all"]["a_count"] = 0
            users[user]["_coin"]["lose"]["all"]["O"] = 0
            users[user]["_coin"]["lose"]["all"]["R"] = 0

        if not "use" in users[user]["_coin"]:
            users[user]["_coin"]["use"] = 0

        if not "win" in users[user]["_coin"]:
            users[user]["_coin"]["win"] = {}
            users[user]["_coin"]["win"]["all"] = {}
            users[user]["_coin"]["win"]["all"]["a_count"] = 0
            users[user]["_coin"]["win"]["all"]["O"] = 0
            users[user]["_coin"]["win"]["all"]["R"] = 0

        if not "all" in users[user]["_coin"]["win"]:
            users[user]["_coin"]["win"]["all"] = {}
            users[user]["_coin"]["win"]["all"]["a_count"] = 0
            users[user]["_coin"]["win"]["all"]["O"] = 0
            users[user]["_coin"]["win"]["all"]["R"] = 0

        if not "a_count" in users[user]["_coin"]["win"]["all"]:
            users[user]["_coin"]["win"]["all"]["a_count"] = 0

        if not "O" in users[user]["_coin"]["win"]["all"]:
            users[user]["_coin"]["win"]["all"]["O"] = 0

        if not "R" in users[user]["_coin"]["win"]["all"]:
            users[user]["_coin"]["win"]["all"]["R"] = 0

        if not "lose" in users[user]["_coin"]:
            users[user]["_coin"]["lose"] = {}
            users[user]["_coin"]["lose"]["all"] = {}
            users[user]["_coin"]["lose"]["all"]["a_count"] = 0
            users[user]["_coin"]["lose"]["all"]["O"] = 0
            users[user]["_coin"]["lose"]["all"]["R"] = 0

        if not "all" in users[user]["_coin"]["lose"]:
            users[user]["_coin"]["lose"]["all"] = {}
            users[user]["_coin"]["lose"]["all"]["a_count"] = 0
            users[user]["_coin"]["lose"]["all"]["O"] = 0
            users[user]["_coin"]["lose"]["all"]["R"] = 0

        if not "a_count" in users[user]["_coin"]["lose"]["all"]:
            users[user]["_coin"]["lose"]["all"]["a_count"] = 0

        if not "O" in users[user]["_coin"]["lose"]["all"]:
            users[user]["_coin"]["lose"]["all"]["O"] = 0

        if not "R" in users[user]["_coin"]["lose"]["all"]:
            users[user]["_coin"]["lose"]["all"]["R"] = 0

        if not "_card" in users[user]:
            users[user]["_card"] = {}
            users[user]["_card"]["use"] = 0
            users[user]["_card"]["win"] = 0
            users[user]["_card"]["lose"] = 0
            users[user]["_card"]["exit"] = 0

        if not "use" in users[user]["_card"]:
            users[user]["_card"]["use"] = 0

        if not "win" in users[user]["_card"]:
            users[user]["_card"]["win"] = 0

        if not "lose" in users[user]["_card"]:
            users[user]["_card"]["lose"] = 0

        if not "exit" in users[user]["_card"]:
            users[user]["_card"]["exit"] = 0

        if not "_random_question" in users[user]:
            users[user]["_random_question"] = 0

        if not "_cross_zero" in users[user]:
            users[user]["_cross_zero"] = 0

        if not "_rock_paper_scissors" in users[user]:
            users[user]["_rock_paper_scissors"] = {}
            users[user]["_rock_paper_scissors"]["use"] = 0
            users[user]["_rock_paper_scissors"] = {}
            users[user]["_rock_paper_scissors"]["win"] = {}
            users[user]["_rock_paper_scissors"]["win"]["all"] = {}
            users[user]["_rock_paper_scissors"]["win"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["r/s"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["s/p"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["p/r"] = 0
            users[user]["_rock_paper_scissors"]["lose"] = {}
            users[user]["_rock_paper_scissors"]["lose"]["all"] = {}
            users[user]["_rock_paper_scissors"]["lose"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["r/p"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["s/r"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["p/s"] = 0
            users[user]["_rock_paper_scissors"]["nothing"] = {}
            users[user]["_rock_paper_scissors"]["nothing"]["all"] = {}
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["r/r"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["s/s"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["p/p"] = 0

        if not "use" in users[user]["_rock_paper_scissors"]:
            users[user]["_rock_paper_scissors"]["use"] = 0

        if not "win" in users[user]["_rock_paper_scissors"]:
            users[user]["_rock_paper_scissors"]["win"] = {}
            users[user]["_rock_paper_scissors"]["win"]["all"] = {}
            users[user]["_rock_paper_scissors"]["win"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["r/s"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["s/p"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["p/r"] = 0

        if not "all" in users[user]["_rock_paper_scissors"]["win"]:
            users[user]["_rock_paper_scissors"]["win"]["all"] = {}
            users[user]["_rock_paper_scissors"]["win"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["r/s"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["s/p"] = 0
            users[user]["_rock_paper_scissors"]["win"]["all"]["p/r"] = 0

        if not "count" in users[user]["_rock_paper_scissors"]["win"]["all"]:
            users[user]["_rock_paper_scissors"]["win"]["all"]["count"] = 0

        if not "r/s" in users[user]["_rock_paper_scissors"]["win"]["all"]:
            users[user]["_rock_paper_scissors"]["win"]["all"]["r/s"] = 0

        if not "s/p" in users[user]["_rock_paper_scissors"]["win"]["all"]:
            users[user]["_rock_paper_scissors"]["win"]["all"]["s/p"] = 0

        if not "p/r" in users[user]["_rock_paper_scissors"]["win"]["all"]:
            users[user]["_rock_paper_scissors"]["win"]["all"]["p/r"] = 0

        if not "lose" in users[user]["_rock_paper_scissors"]:
            users[user]["_rock_paper_scissors"]["lose"] = {}
            users[user]["_rock_paper_scissors"]["lose"]["all"] = {}
            users[user]["_rock_paper_scissors"]["lose"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["r/p"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["s/r"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["p/s"] = 0

        if not "all" in users[user]["_rock_paper_scissors"]["lose"]:
            users[user]["_rock_paper_scissors"]["lose"]["all"] = {}
            users[user]["_rock_paper_scissors"]["lose"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["r/p"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["s/r"] = 0
            users[user]["_rock_paper_scissors"]["lose"]["all"]["p/s"] = 0

        if not "count" in users[user]["_rock_paper_scissors"]["lose"]["all"]:
            users[user]["_rock_paper_scissors"]["lose"]["all"]["count"] = 0

        if not "r/p" in users[user]["_rock_paper_scissors"]["lose"]["all"]:
            users[user]["_rock_paper_scissors"]["lose"]["all"]["r/p"] = 0

        if not "s/r" in users[user]["_rock_paper_scissors"]["lose"]["all"]:
            users[user]["_rock_paper_scissors"]["lose"]["all"]["s/r"] = 0

        if not "p/s" in users[user]["_rock_paper_scissors"]["lose"]["all"]:
            users[user]["_rock_paper_scissors"]["lose"]["all"]["p/s"] = 0

        if not "nothing" in users[user]["_rock_paper_scissors"]:
            users[user]["_rock_paper_scissors"]["nothing"] = {}
            users[user]["_rock_paper_scissors"]["nothing"]["all"] = {}
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["r/r"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["s/s"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["p/p"] = 0

        if not "all" in users[user]["_rock_paper_scissors"]["nothing"]:
            users[user]["_rock_paper_scissors"]["nothing"]["all"] = {}
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["count"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["r/r"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["s/s"] = 0
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["p/p"] = 0

        if not "count" in users[user]["_rock_paper_scissors"]["nothing"]["all"]:
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["count"] = 0

        if not "r/r" in users[user]["_rock_paper_scissors"]["nothing"]["all"]:
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["r/r"] = 0

        if not "s/s" in users[user]["_rock_paper_scissors"]["nothing"]["all"]:
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["s/s"] = 0

        if not "p/p" in users[user]["_rock_paper_scissors"]["nothing"]["all"]:
            users[user]["_rock_paper_scissors"]["nothing"]["all"]["p/p"] = 0

    await update_game_data(users, str(message.author.id))
    with open('game.json', 'w', encoding='UTF-8') as file:
        json.dump(users, file, indent=4, sort_keys=True)

    if message.author.id != BOT:
        print(now.strftime(
            "%d-%m-%Y %H:%M:%S") + " - " + "Сообщение на канале '{0.channel}' от {0.author}: {0.content}".format(
            message))

    msg = message.content.lower()
    banned_list = msg.split(" ")
    if message.author.name not in white_list:
        for item in banned_list:
            if item in bad_words:
                await message.delete()
                await message.channel.send(f"@{message.author.name} не выражайся")
                with open('users.json', 'r', encoding='UTF-8') as file:
                    users = json.load(file)

                    async def update_data(users, user):
                        users[user]["c - swore"] += 1

                    await update_data(users, str(message.author.id))
                    with open('users.json', 'w', encoding='UTF-8') as file:
                        json.dump(users, file, indent=4, sort_keys=True)
                print(Fore.RED + now.strftime(
                    "%d-%m-%Y %H:%M:%S") + " - " + "{0.author} ругнулся на канале! '{0.channel}'".format(message))

    # test
    """
    if message.content.startswith(list):
        print('такой команды нет или она недоступна в этом канале')
    """
    if message.channel.id == TEST:
        if message.content.startswith('_test'):
            # channel = message.channel
            # author = message.author.name
            await f_test2(message, channel=message.channel, author=message.author.name)
            with open('users.json', 'r', encoding='UTF-8') as file:
                users = json.load(file)

                async def update_data(users, user):
                    users[user]["o - _test"] += 1

                await update_data(users, str(message.author.id))
                with open('users.json', 'w', encoding='UTF-8') as file:
                    json.dump(users, file, indent=4, sort_keys=True)

    # <------------парсеры--------------->
    # время-температура
    # переводчик
    # курс
    # <------------парсеры--------------->

    # <----------games channel----------->
    # card21
    if message.channel.id == CARD_21:
        if message.content.startswith('_card'):
            async def card():
                channel = message.channel
                await channel.send(embed=discord.Embed(description=f"Поиграем в 21? :smirk:\n"))
                count = 0
                koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
                random.shuffle(koloda)
                while True:
                    await channel.send(embed=discord.Embed(description=f"Будете брать карту? y/n\n"))
                    choice = await client.wait_for('message', check=lambda
                        message: message.author == message.author and message != "")
                    choice = choice.content
                    if choice.lower() == 'y':
                        current = koloda.pop()
                        await channel.send(
                            embed=discord.Embed(description=f'Вам попалась карта достоинством %d' % current))
                        count += current
                        if count > 21:
                            await channel.send(
                                embed=discord.Embed(description=f':coffin: Извините, но вы проиграли :coffin:'))
                            with open('game.json', 'r', encoding='UTF-8') as file:
                                users = json.load(file)

                                async def update_data(users, user):
                                    users[user]["_card"]["use"] += 1
                                    users[user]["_card"]["lose"] += 1

                                await update_data(users, str(message.author.id))
                                with open('game.json', 'w', encoding='UTF-8') as file:
                                    json.dump(users, file, indent=4, sort_keys=True)
                            break
                        elif count == 21:
                            await channel.send(embed=discord.Embed(description=f'Поздравляю, вы набрали 21!'))
                            with open('game.json', 'r', encoding='UTF-8') as file:
                                users = json.load(file)

                                async def update_data(users, user):
                                    users[user]["_card"]["use"] += 1
                                    users[user]["_card"]["win"] += 1

                                await update_data(users, str(message.author.id))
                                with open('game.json', 'w', encoding='UTF-8') as file:
                                    json.dump(users, file, indent=4, sort_keys=True)
                            break
                        else:
                            await channel.send(embed=discord.Embed(description=f'У вас %d очков.' % count))
                            with open('game.json', 'r', encoding='UTF-8') as file:
                                users = json.load(file)

                                async def update_data(users, user):
                                    users[user]["_card"]["use"] += 1

                                await update_data(users, str(message.author.id))
                                with open('game.json', 'w', encoding='UTF-8') as file:
                                    json.dump(users, file, indent=4, sort_keys=True)
                    elif choice.lower() == 'n':
                        await channel.send(
                            embed=discord.Embed(description=f'У вас %d очков и вы закончили игру.' % count))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_card"]["exit"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                        break

            await card()

    # coin
    if message.channel.id == COIN:
        if message.content.startswith('_coin'):
            async def coin():
                channel = message.channel
                await channel.send(embed=discord.Embed(description=f'орёл или решка?\n Соблюдайте регистр'))
                number = await client.wait_for('message',
                                               check=lambda message: message.author == message.author and message != "")
                number = number.content
                random_number = random.choice(coin_list)
                if number == 'орёл':
                    if number == random_number:
                        await channel.send(embed=discord.Embed(description=f'Поздравляю, вы выиграли'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_coin"]["use"] += 1
                                users[user]["_coin"]["win"]["all"]["a_count"] += 1
                                users[user]["_coin"]["win"]["all"]["O"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                    else:
                        await channel.send(embed=discord.Embed(description=f'Сожалею, но вы проиграли'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_coin"]["use"] += 1
                                users[user]["_coin"]["lose"]["all"]["a_count"] += 1
                                users[user]["_coin"]["lose"]["all"]["O"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                if number == 'решка':
                    if number == random_number:
                        await channel.send(embed=discord.Embed(description=f'Поздравляю, вы выиграли'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_coin"]["use"] += 1
                                users[user]["_coin"]["win"]["all"]["a_count"] += 1
                                users[user]["_coin"]["win"]["all"]["R"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                    else:
                        await channel.send(embed=discord.Embed(description=f'Сожалею, но вы проиграли'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_coin"]["use"] += 1
                                users[user]["_coin"]["lose"]["all"]["a_count"] += 1
                                users[user]["_coin"]["lose"]["all"]["R"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                        pass

            await coin()

    # random-question
    if message.channel.id == RANDOM_QUESTION:
        if message.content.startswith('_random_question'):
            async def random_question(message):
                channel = message.channel
                await channel.send(embed=discord.Embed(description=f'Это небольшой тест'))
                await channel.send(embed=discord.Embed(description=f'Какого числа будет пасмурно?'))
                number = await client.wait_for('message',
                                               check=lambda message: message.author == message.author and message != "")
                number = number.content
                if number == '0':
                    await channel.send(embed=discord.Embed(description=f'Такого числа нет в месяце!'))
                    await channel.send(embed=discord.Embed(
                        description=f'Варианты ответов:\nМой ответ - 0, так что работай программа (1); \n Вы не уточнили, что число именно в месяце,так что - 0 (2); \n Ладно, не прокатило (3)'))
                    number_korona = await client.wait_for('message', check=lambda
                        message: message.author == message.author and message != "")
                    number_korona = number_korona.content
                    if number_korona == '1':
                        await channel.send(embed=discord.Embed(
                            description=f'Не думала, что вы так далеко зайдете, поэтому прошу меня простить и принять билет в Италию.'))
                        return
                    elif number_korona == '2':
                        await channel.send(embed=discord.Embed(
                            description=f'Не думала, что вы так далеко зайдете, поэтому прошу меня простить и принять билет в Италию.'))
                        return
                    elif number_korona >= '4' or number_korona <= '0':
                        await channel.send(embed=discord.Embed(
                            description=f'Не думала, что вы так далеко зайдете, поэтому прошу меня простить и принять билет в Италию.'))
                        return
                    elif number_korona == '3':
                        await random_question(message)
                if number > '31':
                    await channel.send(embed=discord.Embed(
                        description=f'Такого числа нет в месяце!\n Серьезно? Не ври, в месяце максимум 31 день, а не твое число. Либо вводишь нормальный день (1), либо в Италию (2). Выбирай.'))
                    number_korona = await client.wait_for('message', check=lambda
                        message: message.author == message.author and message != "")
                    number_korona = number_korona.content
                    if number_korona == '1':
                        await random_question(message)
                    elif number_korona == '2':
                        await channel.send(embed=discord.Embed(description=f'В Италию, так в Италию...'))
                        return
                if number < '1':
                    await channel.send(embed=discord.Embed(
                        description=f'Такого числа нет в месяце!\n Серьезно, ну откуда в мире такой день? Либо вводишь нормальный день (1), либо в США (2). Выбирай.'))
                    number_korona = await client.wait_for('message', check=lambda
                        message: message.author == message.author and message != "")
                    number_korona = number_korona.content
                    if number_korona == '1':
                        await random_question(message)
                    elif number_korona == '2':
                        await channel.send(embed=discord.Embed(description=f'В США, так в США...'))
                for i in range(int(number)):
                    a = random.choice(list)
                    list.remove(a)
                    await channel.send(embed=discord.Embed(description=f'Вопрос: {a}'))
                    questions = await client.wait_for('message', check=lambda
                        message: message.author == message.author and message != "")
                    questions = questions.content
                    await channel.send(embed=discord.Embed(description=f'Ваш ответ: {questions}'))
                await channel.send(embed=discord.Embed(description=f'Еще раз (1) или все (2) ?'))
                rel = await client.wait_for('message',
                                            check=lambda message: message.author == message.author and message != "")
                rel = rel.content
                if rel == '1':
                    await random_question(message)
                elif rel == '2':
                    return
                else:
                    return
                with open('game.json', 'r', encoding='UTF-8') as file:
                    users = json.load(file)

                    async def update_data(users, user):
                        users[user]["_random_question"] += 1

                    await update_data(users, str(message.author.id))
                    with open('game.json', 'w', encoding='UTF-8') as file:
                        json.dump(users, file, indent=4, sort_keys=True)

            await random_question(message)

    # cross_zero
    if message.channel.id == CROSS_ZERO:
        if message.content.startswith('_cross_zero'):
            async def cross_zero():
                channel = message.channel
                await channel.send(
                    embed=discord.Embed(description=f'Игра Крестики-нолики для двух игроков(с самим с собой)'))

                list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

                async def draw_board(board):
                    await channel.send("-" * 15)
                    for i in range(3):
                        await channel.send(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
                        await channel.send("-" * 15)

                async def take_input(player_token):
                    valid = False
                    while not valid:
                        await channel.send("Куда поставим " + player_token + "? ")
                        player_answer = await client.wait_for('message', check=lambda
                            message: message.author == message.author and message != "")
                        player_answer = player_answer.content
                        try:
                            player_answer = int(player_answer)
                        except:
                            await channel.send("Некорректный ввод. Вы уверены, что ввели число?")
                            continue
                        if player_answer >= 1 and player_answer <= 9:
                            if (str(list[player_answer - 1]) not in "XO"):
                                list[player_answer - 1] = player_token
                                valid = True
                            else:
                                await channel.send("Эта клетка уже занята!")
                        else:
                            await channel.send("Некорректный ввод. Введите число от 1 до 9.")

                async def check_win(board):
                    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
                    for each in win_coord:
                        if board[each[0]] == board[each[1]] == board[each[2]]:
                            return board[each[0]]
                    return False

                async def main(board):
                    counter = 0
                    win = False
                    while not win:
                        await draw_board(board)
                        if counter % 2 == 0:
                            await take_input("❌")
                        else:
                            await take_input("⭕")
                        counter += 1
                        if counter > 4:
                            tmp = check_win(board)
                            if tmp:
                                await channel.send(f"{message.author.name} выйграл")
                                win = True
                                break
                        if counter == 9:
                            await channel.send("Ничья!")
                            break
                    await draw_board(board)

                await main(list)
                with open('game.json', 'r', encoding='UTF-8') as file:
                    users = json.load(file)

                    async def update_data(users, user):
                        users[user]["_cross_zero"] += 1

                    await update_data(users, str(message.author.id))
                    with open('game.json', 'w', encoding='UTF-8') as file:
                        json.dump(users, file, indent=4, sort_keys=True)

            await cross_zero()

    # rock-paper-scissors
    if message.channel.id == ROCK_PAPER_SCISSORS:
        if message.content.startswith('_rock_paper_scissors'):
            async def rock_paper_scissors():
                channel = message.channel
                await channel.send(
                    embed=discord.Embed(description=f'камень-ножницы-бумага с ботом\n Соблюдайте нижний регистр'))
                number = await client.wait_for('message',
                                               check=lambda message: message.author == message.author and message != "")
                number = number.content
                # await message.channel.purge( limit=3 )
                random_number = random.choice(rock_paper_scissors_list)
                if number == 'камень':
                    if random_number == 1:
                        await channel.send(embed=discord.Embed(
                            description=f'Камень не бьет камень, ведь камень камню камень! Ничья, братья камни! \n Ничья!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["nothing"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["nothing"]["all"]["r/r"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                    if random_number == 2:
                        await channel.send(embed=discord.Embed(
                            description=f'Камень побил ножницы и ему за это ничего не будет, он ведь белорусский омоновец! Блистательная победа над народом! \n Камень победил ножницы!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["win"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["win"]["all"]["r/s"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                    if random_number == 3:
                        await channel.send(embed=discord.Embed(
                            description=f'Мнонеуважаемый господин камень был обёрнут бумагой, как лохня и законно проиграл от недостатка мощности его дубинки! Это проигрыш он запомнит на всю свою жизнь, ведь такого поражения он явно не ожидал! \n Камень проиграл бумаге!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["lose"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["lose"]["all"]["r/p"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)

                if number == 'ножницы':
                    if random_number == 1:
                        await channel.send(embed=discord.Embed(
                            description=f'Увы, господа ножницы не побили многоуважаемых каменных омоновцив и заслуженно пошли за решётку! Жыве беларусь! \n Ножницы проиграли камню!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["lose"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["lose"]["all"]["s/r"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                    if random_number == 2:
                        await channel.send(embed=discord.Embed(
                            description=f'Ножницы не посмеют ударить своих активистов, ибо каждый голос - сила(где то в мире смеется один Лукашенко)! Определённо ничья! \n Ничья!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["nothing"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["nothing"]["all"]["s/s"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                    if random_number == 3:
                        await channel.send(embed=discord.Embed(
                            description=f'А мы что, мы ничего, так, собираем митинки, воюем, ничего не обычного. В смысле есть святые мощи лукашенко, которое спасают от ковида? а что нас не позвали? А ну бегом в церкви. С тех пор их больше никто не видел \n Ножницы победили бумагу!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["win"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["win"]["all"]["s/p"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)

                if number == 'бумага':
                    if random_number == 1:
                        await channel.send(embed=discord.Embed(
                            description=f'Бумага обернула господов омоновцев, ведь против РПЦ никакая резиновая сила не устоит. А проиграли, потому что РПЦ явно не с тем приводом приус купили! Это растянувшаяся битва даст жару любой вечеринке, на которой ты обязан побывать! \n Бумага победила камень!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["win"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["win"]["all"]["p/r"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                    if random_number == 2:
                        await channel.send(embed=discord.Embed(
                            description=f'Опять вы? Да как вы выжили то? Так, у нас акция, две свечки по цене одной; Генерал, надеюсь, что вы сказали, что это свечки в 5 точку? Ааа, да, кнш, не парьтесь. \n Бумага проиграла ножницам!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["lose"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["lose"]["all"]["p/s"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)
                    if random_number == 3:
                        await channel.send(embed=discord.Embed(
                            description=f'Внимание, начались массовые беспорядки кадилов. Внимание, РПЦ, этот мел мы пустим на лекарства, а вам дадим кристалы. Забористые такие, с персиком, покрытым сливками или клубникой в шоколадке \n Ничья!'))
                        with open('game.json', 'r', encoding='UTF-8') as file:
                            users = json.load(file)

                            async def update_data(users, user):
                                users[user]["_rock_paper_scissors"]["use"] += 1
                                users[user]["_rock_paper_scissors"]["nothing"]["all"]["count"] += 1
                                users[user]["_rock_paper_scissors"]["nothing"]["all"]["p/p"] += 1

                            await update_data(users, str(message.author.id))
                            with open('game.json', 'w', encoding='UTF-8') as file:
                                json.dump(users, file, indent=4, sort_keys=True)

            await rock_paper_scissors()
    # <----------games channel----------->


@client.event
async def on_ready():
    init(autoreset=True)
    tic1_1 = time.perf_counter()
    now = datetime.datetime.now()
    print(Fore.GREEN + now.strftime("%d-%m-%Y %H:%M:%S") + f' Бот готов:)')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!help'))
    tic1_2 = time.perf_counter()
    print(Fore.GREEN + f"Загрузка бота заняла {tic1_2 - tic1_1:0.4f} секунд\n")

    for file in os.listdir("Functions/admin"):
        if fnmatch.fnmatch(file, '*.py'):
            print(Fore.GREEN + f'Функция {file} загружена')
            time.sleep(0.01)
    print(Fore.GREEN + f"Загрузка функций админа закончена\n")

    tic1_3 = time.perf_counter()
    print(Fore.GREEN + f"Загрузка функций и бота заняла {tic1_3 - tic1_1:0.4f} секунд\n")

    print(Fore.YELLOW + f'<------Список участников:------>\n|')
    for guild in client.guilds:
        for member in guild.members:
            print(Fore.YELLOW + f'{member}')
        print(Fore.YELLOW + f'|\n<------Конец------>\n')


@client.event
async def on_command_error(ctx, error):
    # Основные ошибки:
    # commands.MissingRequiredArgument - отсутствие аргумента
    # commands.MissingPermissions - отсутствие нужных прав
    # commands.CommandNotFound - отсутствие команды
    pass


@client.command()
@commands.has_role(CREATOR)
async def add_word(ctx, word):
    await f_add_word(ctx, word)


@client.command()
@commands.has_role(CREATOR)
async def admin_panel(ctx):
    await f_admin_panel(ctx)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["e - admin_panel"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@client.command()
@commands.has_role(CREATOR)
async def ban(ctx, member: discord.Member, *, reason):
    await f_ban(ctx, member, reason)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["e - admin_panel"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@ban.error
async def aban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, нужны аргументы')


@client.command()
@commands.has_role(CREATOR)
async def clear(ctx, amout):
    await f_clear(ctx, amout)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["g - clear"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, нужен аргумент')

    # if isinstance(error, commands.MissingPermissions):
    #     await ctx.send(f'{ctx.author.name}, недостаточно прав')

    # if isinstance(error, commands.CommandNotFound):
    #     await ctx.send(f'{ctx.author.name}, команда не обнаружена, или вы не правильно её ввели')


@client.command()
@commands.has_role(CREATOR)
async def give_role(ctx, member: discord.Member, role: discord.Role):
    await f_give_role(ctx, member, role)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["h - give_role"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@give_role.error
async def give_role_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, нужны аргументы')


@client.command()
@commands.has_role(CREATOR)
async def kick(ctx, member: discord.Member, *, reason):
    await f_kick(ctx, member, reason)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["i - kick"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, нужны аргументы')


@client.command()
@commands.has_role(CREATOR)
async def mute(ctx, member: discord.Member, time: int, permission: int, *, reason):
    await f_mute(ctx, member, time, permission, reason)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["j - mute"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, нужны аргументы')


@commands.has_role(CREATOR)
@client.command()
async def random_password(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(embed=discord.Embed(description=f'Функция временно недоступна', colour=discord.Color.red()))
    # await f_random_password(ctx, member)


@client.command()
@commands.has_role(CREATOR)
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    await f_remove_role(ctx, member, role)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["k - remove_role"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@remove_role.error
async def remove_role_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, нужны аргументы')


@client.command()
@commands.has_role(CREATOR)
async def test(ctx):
    # async def on_message(self, message):
    #     channel = message.channel
    await f_test(ctx)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["l - test"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


# @client.command()
# @commands.has_role(CREATOR)
# async def test2(ctx):
#     await f_test2(ctx)


@client.command()
@commands.has_role(CREATOR)
async def unban(ctx, member: discord.Member):
    await f_unban(ctx, member)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["m - unban"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, нужен аргумент')


@client.command()
@commands.has_role(CREATOR)
async def unmute(ctx, member: discord.Member):
    await f_unmute(ctx, member)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["n - unmute"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


@client.command()
@commands.has_role(CREATOR)
async def user_info(ctx, member: discord.Member):
    await f_user_info(ctx, member)
    with open('users.json', 'r', encoding='UTF-8') as file:
        users = json.load(file)

        async def update_data(users, user):
            users[user]["d - user_info"] += 1

        await update_data(users, str(ctx.author.id))
        with open('users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, sort_keys=True)


if __name__ == __name__:
    client.run(TOKEN)
