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

class Moderacyjne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ban(self, ctx, osoba: discord.Member=None, *, powod=None):
        if not osoba:
            embed=discord.Embed(title="**Błąd :no_entry_sign:**", description=":white_check_mark: Poprawne użycie: `ban (osoba) <powód>`", color=0xff0000)
            await ctx.send(embed=embed)

        if ctx.message.author.guild_permissions.ban_members:
            await osoba.ban(reason=powod)
            embed=discord.Embed(title="**ban :no_entry_sign:**", description=f'**:hammer: {osoba.mention} dostał/a bana.**\n  \n**:busts_in_silhouette: Z serwera:** `{ctx.guild.name}`\n  \n**:warning: Powód:** `{powod}`', color=0xfd3550)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Administrator: {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await osoba.send(embed=embed)
            
        else:
            embed=discord.Embed(title="**Błąd :no_entry_sign:**", description=":no_entry: Brak uprawnienia: `Ban Members`", color=0xff0000)
            await ctx.send(embed=embed)

    @commands.command()
    async def kick(self, ctx, osoba: discord.Member=None, *, powod=None):
        if not osoba:
            embed=discord.Embed(title="**Błąd :no_entry_sign:**", description=":white_check_mark: Poprawne użycie: `kick (osoba) <powód>`", color=0xff0000)
            await ctx.send(embed=embed)

        if ctx.message.author.guild_permissions.kick_members:
            await osoba.kick(reason=powod)
            embed=discord.Embed(title="**Kick :no_entry_sign:**", description=f'**:hammer: {osoba.mention} dostał/a kicka.**\n  \n**:busts_in_silhouette: Z serwera:** `{ctx.guild.name}`\n  \n**:warning: Powód:** `{powod}`', color=0xff8d00)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Administrator: {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await osoba.send(embed=embed)
            
        else:
            embed=discord.Embed(title="**Błąd :no_entry_sign:**", description=":no_entry: Brak uprawnienia: `Kick Members`", color=0xff0000)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderacyjne(bot))


