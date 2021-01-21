import discord
from discord.ext import commands
import random
import asyncio

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group()
    async def dev(self, ctx):

        if ctx.invoked_subcommand is None:

            array = [1048575, 8137918, 16182940]

            value = random.choice(array)

            embed = discord.Embed(title="Develepor commands:", description="`guilds`, \
`stop_bot`", color = value, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")

            await ctx.send(embed=embed)

    @dev.command()
    async def guilds(self, ctx):

        if ctx.author.id == 711444754080071714:
            for i in self.client.guilds:
                await ctx.send(i)
                await asyncio.sleep(0.5)
        else:
            await ctx.send("Sorry this is developer only command!")

    @dev.command()
    async def stop_bot(self, ctx):

        if ctx.author.id == 711444754080071714:
            await ctx.send("Stopping Bot!")
            exit()
        else:
            await ctx.send("Sorry this is developer only command!")

def setup(client):
    client.add_cog(Commands(client))