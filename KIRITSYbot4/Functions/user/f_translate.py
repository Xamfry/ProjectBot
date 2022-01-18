from Spiski.translate_list import translate_list
from googletrans import Translator
import discord
from discord.ext import commands
from Spiski.config import TRANSLATE

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# translate
@client.command()
async def f_translate(ctx, src, dest):
    channel = client.get_channel(TRANSLATE)
    if src and dest not in translate_list:
        await channel.send(embed=discord.Embed(
            description=f':warning: Неверный формат ввода.\n Правильный формат "!tanslate <язык текста> <язык, который захотите>" \n Для ознакомления со списком языков используйте "!tanslate_help" :warning:'))
    else:
        translator = Translator()
        await channel.send(embed=discord.Embed(
            description=f'Введите предложение. Соблюдайте пунктуацию и проверяйте текст на ошибки: '))
        sentence = await client.wait_for('message',
                                         check=lambda message: message.author == ctx.author and message != "")
        sentence = sentence.content
        result = translator.translate(sentence, src=src, dest=dest)
        await channel.send(embed=discord.Embed(description=f'Перевод ---> {result.text} '))
        await channel.send(embed=discord.Embed(
            description=f':warning: Неверно введен текст. Проверьте пунктуацию или проверьте слова на наличие ошибок :warning:'))
