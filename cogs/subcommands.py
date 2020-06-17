import discord
from discord.ext import commands
import random

class Groups(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("SubCommands Cog has been loaded\n-----")

    #@commands.group()
    #async def first(self, ctx):
    #    if ctx.invoked_subcommand is None:
    #        await ctx.send("This is the first command layer")

    #@first.group()
    #async def second(self, ctx):
    #    print(ctx.invoked_subcommand)
    #    if ctx.invoked_subcommand is None:
    #        await ctx.message.author.send("Hey! Did this come through clearly?")

    #@second.command()
    #async def third(self, ctx, channelId=None):
    #    if channelId != None:
    #        channel = self.bot.get_channel(int(channelId))
     #       await channel.send("WASSAAAAAAAAAPPPP", delete_after=15)

    #@commands.group()
    #async def goodevening(self, ctx):
    #    print(ctx.invoked_subcommand)
    #    if ctx.invoked_subcommand is None:
    #        await ctx.message.author.send("Good Evening Child.")

    @commands.group()
    async def calculator(self, ctx):
        """
        Simple calculator command using two integers
        """
        pass

    @calculator.command(pass_context=True)
    async def add(self, ctx, a: int, b: int):
        """
        Simple calculator command in the form of a + b
        """
        embed = discord.Embed(title="Addition", color=random.choice(self.bot.color_list), timestamp=ctx.message.created_at)

        embed.add_field(name="First no.", value=a, inline=True)
        embed.add_field(name="Second no.", value=b, inline=True)
        embed.add_field(name="Total", value=(a + b), inline=True)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @calculator.command(pass_context=True)
    async def subtract(self, ctx, a: int, b: int):
        """
        Simple calculator command in the form of a - b
        """
        embed = discord.Embed(title="Subtract", color=random.choice(self.bot.color_list), timestamp=ctx.message.created_at)

        embed.add_field(name="First no.", value=a, inline=True)
        embed.add_field(name="Second no.", value=b, inline=True)
        embed.add_field(name="Total", value=(a - b), inline=True)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @calculator.command(pass_context=True)
    async def multiply(self, ctx, a: int, b: int):
        """
        Simple calculator command in the form of a * b
        """
        embed = discord.Embed(title="Multiply", color=random.choice(self.bot.color_list),timestamp=ctx.message.created_at)

        embed.add_field(name="First no.", value=a, inline=True)
        embed.add_field(name="Second no.", value=b, inline=True)
        embed.add_field(name="Total", value=(a * b), inline=True)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @calculator.command(pass_context=True)
    async def divide(self, ctx, a: int, b: int):
        """
        Simple calculator command in the form of a / b
        """
        embed = discord.Embed(title="Divide", color=random.choice(self.bot.color_list), timestamp=ctx.message.created_at)

        embed.add_field(name="First no.", value=a, inline=True)
        embed.add_field(name="Second no.", value=b, inline=True)
        embed.add_field(name="Total", value=(a / b), inline=True)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Groups(bot))