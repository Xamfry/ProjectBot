import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
from Spiski.config import CROSS_ZERO

client.remove_command("help")


# cross_zero
@client.command()
async def f_cross_zero(ctx):
    channel = client.get_channel(CROSS_ZERO)
    await channel.send(embed=discord.Embed(description=f'Игра Крестики-нолики для двух игроков(с самим с собой)'))

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
            player_answer = await client.wait_for('message',
                                                  check=lambda message: message.author == ctx.author and message != "")
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
                    await channel.send(f"{ctx.author.name} выйграл")
                    win = True
                    break
            if counter == 9:
                await channel.send("Ничья!")
                break
        await draw_board(board)

    await main(list)
