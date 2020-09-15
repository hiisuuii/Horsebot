# bot.py
import os
import random

import discord
import typing
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Connected as ' + str(bot.user) + ' to guilds: \n' + str(bot.guilds))


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Player')
    await member.add_roles(role)

@bot.command(name='roll')
async def roll(ctx, max: typing.Optional[int] = 20):

    embed = discord.Embed(
        #title = 'Dice Roll',
        colour = discord.Colour.red()
    )

    response = str(random.randint(1,max))
    #await ctx.send('Rolled a D' + str(max) + ' and got: ' + response)

    author = ''
    if ctx.author.nick:
        author = ctx.author.nick
    else:
        author = ctx.author.name

    embed.set_footer(text='Rolled by '+ str(author),icon_url=str(ctx.author.avatar_url))
    embed.set_author(name='Dice Roll',icon_url='https://cdn.pixabay.com/photo/2017/08/31/04/01/d20-2699387_960_720.png')
    embed.add_field(name='Dice', value='D'+str(max),inline=True)
    embed.add_field(name='Result',value=response,inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()
    

@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Must only be 1 argument and argument must be a whole number')


bot.run(TOKEN)