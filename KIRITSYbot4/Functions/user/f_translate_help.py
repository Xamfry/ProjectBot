import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# translate_help
@client.command()
async def f_translate_help(ctx):
    emb = discord.Embed(
        title="Поддерживаемые языки. Формат ввода - '!tanslate <язык текста> <язык, который захотите>'",
        colour=discord.Color.orange()
    )
    emb.add_field(
        name='Аббревиатура и язык{0}'.format(":"),
        value="af - afrikaans\n sq - albanian\n am - amharic\n ar - arabic\n hy - armenian\n \
            az - azerbaijani\n eu - basque\n be - belarusian\n bn - bengali\n bs - bosnian\n \
            bg - bulgarian\n ca - catalan\n ceb - cebuano\n ny - chichewa\n zh-cn - chinese (simplified)\n \
            zh-tw - chinese (traditional)\n co - corsican\n hr - croatian\n cs - czech\n da - danish\n \
            nl - dutch\n en - english\n eo - esperanto\n et - estonian\n tl - filipino\n fi - finnish\n \
            fr - french\n fy - frisian\n gl - galician\n ka - georgian\n de - german\n el - greek\n \
            gu - gujarati\n ht - haitian creole\n ha - hausa\n haw - hawaiian\n iw - hebrew\n hi - hindi\n \
            hmn - hmong\n hu - hungarian\n is - icelandic\n ig - igbo\n id - indonesian\n ga - irish\n \
            it - italian\n ja - japanese\n jw - javanese\n kn - kannada\n kk - kazakh\n km - khmer\n \
            ko - korean\n ku - kurdish (kurmanji)\n ky - kyrgyz"
    )
    emb.add_field(
        name='Аббревиатура и язык{0}'.format(":"),
        value="lo - lao\n la - latin\n lv - latvian\n lt - lithuanian\n lb - luxembourgish\n \
        mk - macedonian\n mg - malagasy\n ms - malay\n ml - malayalam\n mt - maltese\n mi - maori\n \
        mr - marathi\n mn - mongolian\n my - myanmar (burmese)\n ne - nepali\n no - norwegian\n \
        ps - pashto\n fa - persian\n pl - polish\n pt - portuguese\n pa - punjabi\n ro - romanian\n \
        ru - russian\n sm - samoan\n gd - scots gaelic\n sr - serbian\n st - sesotho\n sn - shona\n \
        sd - sindhi\n si - sinhala\n sk - slovak\n sl - slovenian\n so - somali\n es - spanish\n \
        su - sundanese\n sw - swahili\n sv - swedish\n tg - tajik\n ta - tamil\n te - telugu\n \
        th - thai\n tr - turkish\n uk - ukrainian\n ur - urdu\n uz - uzbek\n vi - vietnamese\n \
        cy - welsh\n xh - xhosa\n yi - yiddish\n yo - yoruba\n zu - zulu\n fil - Filipino\n he - Hebrew"
    )
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=emb)
