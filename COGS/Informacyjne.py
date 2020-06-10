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

class Informacyjne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
      embed=discord.Embed(title="**Pong! :ping_pong:**", description=f"**Mój ping:** `{round(self.bot.latency * 1000)}` **ms**", color=0x16e960)
      embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)


    @commands.command()
    async def bot(self, ctx):
      embed=discord.Embed(title="**Bot Informacje**",description="[Dodaj bota](https://discordapp.com/api/oauth2/authorize?client_id=699260666204389457&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize&scope=bot)  | [Support serwer](https://discord.gg/kyMpqjG)", color=0xeb35fd)
      embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/699260666204389457/5c153aab4e95590eb20e34b5bb7a0c33.webp?size=1024")
      embed.add_field(name="***Liczba Użytkowników bota***", value=f"```{len(self.bot.users)}```", inline=False)
      embed.add_field(name="***Wersja bota***", value="```0.0.5 Alpha```", inline=True)
      embed.add_field(name="***Liczba serwerów***", value=f"```{len(self.bot.guilds)}```", inline=True)
      embed.set_footer(text=f"Wywołane przez: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(Informacyjne(bot))