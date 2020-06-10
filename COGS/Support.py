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

class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def zgłoś(self, ctx, *, treść):
        channel = self.bot.get_channel(698672899623616564)
        embed=discord.Embed(title="**Zgłoszenie :e_mail:**", description=f"**{ctx.author.name}** `zgłosił błąd. Z serwera:` **{ctx.guild.name}** `o treści:`\n```css\n{treść}```", color=0xe9ff66)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Przesłane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await channel.send(embed=embed)
        await ctx.send('**Dziękujemy za zgłoszenie błędu :heart_exclamation:. Poprawimy go w najbliższym czasie :warning:.**')

def setup(bot):
  bot.add_cog(Support(bot))
