import platform
import discord
import pyjokes

from discord.ext import commands
from random import choice
from joke.jokes import *
from Distractions import get_joke_categories, get_joke

import cogs._json


class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands Cog has been loaded\n-----")

    @commands.command()
    async def stats(self, ctx):
        """
        A usefull command that displays bot statistics.
        """
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=ctx.author.colour, timestamp=ctx.message.created_at)

        embed.add_field(name='Bot Version:', value=self.bot.version)
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Guilds:', value=serverCount)
        embed.add_field(name='Total Users:', value=memberCount)
        embed.add_field(name='Bot Developers:', value="<@284783915619713024>")

        embed.set_footer(text=f"Kelyph0 | {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['disconnect', 'close', 'stopbot'])
    @commands.is_owner()
    async def logout(self, ctx):
        """
        If the user running the command owns the bot then this will disconnect the bot from discord.
        """
        await ctx.send(f"Hey {ctx.author.mention}, I am now logging out :wave:")
        await self.bot.logout()

    @commands.command()
    async def echo(self, ctx, *, message=None):
        """
        A simple command that repeats the users input back to them.
        """
        message = message or "Please provide the message to be repeated."
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(name='stars')
    async def stars(self, ctx):
        """
        Adds some sparkle to chat!
        """
        await ctx.message.delete()
        await ctx.send(f". 　　 　　　　　　　 ✦ 　　　　　　　 　 　　 　　 　 　　✦ 　　 　 　　　　　 　　　　　　　　.　　　　,　　   　 "
                       f".　　　　　　　　　　　　　.　　　ﾟ　  　　　.　　　　　　　　　　　　　✦. 　　 　　　　　　　 ✦ 　　　　　　　 　 　　 　　 　 　　✦ 　　 　 　　　　　 "
                       f"　　　　　　　　.　　　　,　　   　 .　　　　　　　　　　　　　.　　　ﾟ　  　　　.　　　　　　　　　　　　　✦")

    @commands.command(name='joke')
    async def joke(self, ctx):
        """
        Tells a joke.
        """
        await ctx.message.delete()
        await ctx.send(f"{(choice([geek, icanhazdad, chucknorris, icndb]))()}")

    @commands.command()
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.Member):
        """
        Blacklist someone from the bot
        """
        if ctx.message.author.id == user.id:
            await ctx.send("Hey, you cannot blacklist yourself!")
            return

        self.bot.blacklisted_users.append(user.id)
        data = cogs._json.read_json("blacklist")
        data["blacklistedUsers"].append(user.id)
        cogs._json.write_json(data, "blacklist")
        await ctx.send(f"Hey, I have blacklisted {user.name} for you.")

    @commands.command()
    @commands.is_owner()
    async def unblacklist(self, ctx, user: discord.Member):
        """
        Unblacklist someone from the bot
        """
        self.bot.blacklisted_users.remove(user.id)
        data = cogs._json.read_json("blacklist")
        data["blacklistedUsers"].remove(user.id)
        cogs._json.write_json(data, "blacklist")
        await ctx.send(f"Hey, I have unblacklisted {user.name} for you.")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def prefix(self, ctx, *, pre='-'):
        """
        Set a custom prefix for a guild
        """
        data = cogs._json.read_json('prefixes')
        data[str(ctx.message.guild.id)] = pre
        cogs._json.write_json(data, 'prefixes')
        await ctx.send(f"The guild prefix has been set to `{pre}`. Use `{pre}prefix <prefix>` to change it again!")

    @commands.command(name='jokecategories')
    async def joke_categories(self, ctx):
        await ctx.send(get_joke_categories())

    @commands.command(name='joke get')
    async def joke_get(self, ctx):
        arguments = ctx.content.split(" ")
        if len(arguments) == 3:
            await ctx.send(get_joke(arguments[-1]))




def setup(bot):
    bot.add_cog(Commands(bot))

