import datetime
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command("help")


# матека
@client.command()
async def f_math(ctx, example="0"):
    # now = datetime.datetime.now()
    await ctx.message.channel.send(f"Result: {eval(example)}")
    # print(now.strftime("%d-%m-%Y %H:%M:%S") + " - " + f"Result: {eval(example)}" )
