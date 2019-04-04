import discord
from discord.ext import commands
import re
import asyncio
from discord.utils import get

Bot = commands.Bot(command_prefix='.')
TOKEN = 'BOT_TOKEN'

Bot.remove_command('help')

story_channel_id = id  # replace id with the id


@Bot.event
async def on_ready():

    await Bot.change_presence(
        activity=discord.Game(
            name='one word'
            )
        )
    print('words are being processed')

    if len(Bot.guilds) == 1:
        print('serving a lonely guild named: {}')

    else:
        print('serving {} guild :)'.format(len(Bot.guilds)))


@Bot.event
async def on_message(message):
    msg = message.content
    author = message.author.name
    channel = message.channel
    print('{}: {}: {}'.format(author, channel, msg))

    if message.channel.id == story_channel_id:
        words = len(message.content.split())
        signs_detected = re.search(r'[#@$%^&(,)_};+{:?/.><]+', message.content)

        if signs_detected or words > 1:
            try:
                await message.channel.purge(limit=1)

            except discord.errors.NotFound:
                print('a simple error happened')

        else:
            pass
    else:
        pass

    await Bot.process_commands(message)


@Bot.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        title='rules',
        description='you\'re allowed to write one word without characters',
        color=discord.Colour.darker_grey()
    )

    if ctx.channel.id == story_channel_id:
        await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)

    else:
        await ctx.channel.send(f'write the command in {<#story_channel_id>}')


Bot.run(TOKEN)
