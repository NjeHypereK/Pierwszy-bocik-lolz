import keep_alive
import discord
import json
import os
import time
import inspect 
import asyncio
import random
from itertools import cycle
from discord.ext import commands
from discord.ext import tasks

client = commands.Bot(command_prefix='.')
status = cycle(['Użyj .help', 'JD 100%'])
client.remove_command('help') 
print('--------------------------------')
print('|     Bot daje znaki życia     |')
print('|                              |')


@client.event
async def on_ready():
    change_status.start()
    print('| Bot żyje panie Hyperze Mrauu |')
    print('--------------------------------')
    print('    ')
    print('--------------------------')
    print('|  Zalogowano sie jako:  |')
    print(f'|      {client.user.name}      |')
    print('--------------------------')
    print('    ')
    print('----------------------')
    print('|  ID zalogowanego:  |')
    print(f'| {client.user.id} |')
    print('----------------------')
    print('    ')
    print('cos jeszcze jtr dodaj, okej ?')

@tasks.loop(seconds=30)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))


@client.command(name='eval', pass_context=True)
@commands.is_owner()
async def eval_(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await ctx.send(await res)
    else:
        await ctx.send(f"**Wynik:**\n```py\n{res}```")

@client.event
async def on_command_error(ctx, error):
    pass

client.load_extension("COGS.Helpcustom")
client.load_extension("COGS.Informacyjne")
client.load_extension("COGS.Fun")
client.load_extension("COGS.Support")
client.load_extension("COGS.Moderacyjne")

keep_alive.keep_alive()

client.run('Njk5MjYwNjY2MjA0Mzg5NDU3.XqAGPA.qgK6mZpFjjQLy5gaqKaIfZD0Mm4')
                               