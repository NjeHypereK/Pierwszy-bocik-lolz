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

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command()
    async def moneta(self, ctx):
        joł = [
        "**Wypadł:** `Orzeł` :money_with_wings: ", "**Wypadła:** `Resztka` :money_with_wings: ",
        "`Oops` **moneta wypadła za kanape no trudno :eyes:**"
        ]
        hyper = random.choice(joł)
        embed=discord.Embed(title="**:money_with_wings: Rzut monetą**", description=f"{hyper}", color=0xe9ff66)
        embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def awatar(self, ctx, member:discord.Member=None):
        if member is None:
            embed = discord.Embed(
                colour = discord.Colour.red()
            )
            embed.add_field(name="**Błąd! :no_entry_sign:**", value=":white_check_mark: **Poprawne użycie:** `awatar (osoba)`")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'**:bust_in_silhouette: Awatar użytkownika: {member.name}**')
            embed = discord.Embed(colour = discord.Colour.blue())
            embed.set_image(url=f"{member.avatar_url}")
            embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def powiedz(self, ctx, *, tekst=None):
      if tekst is None:
        embed=discord.Embed(title="**Błąd :no_entry_sign:**", description=":white_check_mark: Poprawne użycie: `powiedz <tekst>`", color=0xff0000)
        await ctx.send(embed=embed)

      else:
        embed=discord.Embed(title=" ", description=f"`{ctx.author.name}` **kazał mi powiedzieć:**\n```css\n{tekst}```", color=0x69ffb4)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member:discord.Member=None):
      if member is None:
        embed=discord.Embed(title="**Błąd :no_entry_sign:**", description=":white_check_mark: Poprawne użycie: `kill (osoba)`", color=0xff0000)
        await ctx.send(embed=embed)
      else:
        embed=discord.Embed(title=" ", description=f"***{ctx.author.name}*** :dagger: `zabija` :dagger: ***{member.name}***", color=0xfd3550)
        embed.set_image(url="https://i.imgur.com/tZ5cVkG.png")
        embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member:discord.Member=None):
      if member is None:
        embed=discord.Embed(title="**Błąd :no_entry_sign:**", description=":white_check_mark: Poprawne użycie: `kiss (osoba)`", color=0xff0000)
        embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
      else:
        embed=discord.Embed(title=" ", description=f"***{ctx.author.name}*** :kissing_heart: `całuje` :kissing_heart: ***{member.name}***", color=0xff86f3)
        embed.set_image(url="https://i.imgur.com/Fx4i8an.png")
        embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, member:discord.Member=None):
      if member is None:
        embed=discord.Embed(title="**Błąd :no_entry_sign:**", description=":white_check_mark: Poprawne użycie: `hug (osoba)`", color=0xff0000)
        await ctx.send(embed=embed)
      else:
        embed=discord.Embed(title=" ", description=f"***{ctx.author.name}*** :heartpulse: `przytula` :heartpulse: ***{member.name}***", color=0xd467ff)
        embed.set_image(url="https://i.imgur.com/lGaj0JY.png")
        embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)



def setup(bot):
  bot.add_cog(Fun(bot))
