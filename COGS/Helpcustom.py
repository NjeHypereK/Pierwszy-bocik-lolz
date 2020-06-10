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

class Helpcustom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="**Help - UnlimiteqBit**", description="[Dodaj bota](https://discordapp.com/api/oauth2/authorize?client_id=699260666204389457&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize&scope=bot)  | [Support serwer](https://discord.gg/kyMpqjG)")
        embed.add_field(name="**_Informacyjne_**", value="> ```ping```**Wyświetla ping bota** ```help```**Wyświetla tą wiadomość** ```bot```**Wyświetla info o bocie**", inline=False)
        embed.add_field(name="**_4Fun_**", value="> ```awatar```**Wyświetla awatar oznaczonej osoby** ```powiedz```**Bot powie  cokolwiek zechcesz** ```moneta```**Bot rzuca monetą** ```kill```**Zabija oznaczoną osobe** ```kiss```**Całuje oznaczoną osobe** ```hug```**Przytula oznaczoną osobe**", inline=False)
        embed.add_field(name="**_Moderacyjne_**", value="> ```usuń```**Usuwa daną ilość wiadomości** ```kick```**Kickuje oznaczoną osobe** ```ban```**Banuje oznaczoną osobe**", inline=False)
        embed.add_field(name="**_Support_**", value="> ```zgłoś```**Zgłasza bug / błąd**", inline=False)
        embed.add_field(name="**_Developerskie_**", value="> ```eval```**Wykonuje polecenie developera** ```wyłącz```**Wyłącza bota**", inline=False)
        embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
        

def setup(bot):
  bot.add_cog(Helpcustom(bot))