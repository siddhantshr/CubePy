import discord
from discord.ext import commands
import sqlite3
import random
import platform

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group()
    async def prefix(self, ctx):

        if ctx.invoked_subcommand is None:

            array = [1048575, 8137918, 16182940]
            value = random.choice(array)

            embed = discord.Embed(title="Prefix Help:", description="`set` : sets the prefix, `view` : view the current prefix", color=value)
            await ctx.send(embed=embed)

    @prefix.command()
    @commands.has_permissions(manage_guild = True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def set(self, ctx, prefix : str):

        if len(prefix) > 5:
            return await ctx.send("Prefix cannot be more than 5 characters in lenght!")
        db = sqlite3.connect("data/prefixes.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO guild(GuildID, PREFIX) VALUES(?,?)")
            val = (ctx.guild.id, prefix)
            await ctx.send(f"Prefix has been set to `{prefix}`")
        elif result is not None:
            sql = ("UPDATE guild SET PREFIX = ? WHERE GuildID = ?")
            val = (prefix, ctx.guild.id)
            await ctx.send(f"Prefix has been changed to `{prefix}`")
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()

    @prefix.command()
    async def view(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)
        guild = ctx.guild

        try:
            db = sqlite3.connect("data/prefixes.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {guild.id}")
            result = cursor.fetchone()

            prefix = result[0]
        except:
            prefix = "-"

        embed=discord.Embed(title=f"{ctx.guild.name}'s Prefix:", description=f"1. {self.client.user.mention} \n2. `{prefix}`", color=value)
        embed.set_footer(text=f"Use {prefix} before each command!")

        await ctx.send(embed=embed)

    @commands.command()
    async def members(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)
        guild = ctx.guild

        all_members = guild.member_count
        humans = len([m for m in guild.members if not m.bot])
        bots = all_members-humans

        embed = discord.Embed(title=f"Member Count Of {guild.name}", description=f"All Members : {all_members} \nUsers : {humans} \nBots : {bots}", color=value)
        embed.set_footer(text="CubePy", icon_url=guild.icon_url)

        await ctx.send(embed=embed)


    @commands.command(aliases = ["pong"])
    async def ping(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        embed = discord.Embed(
            color=value
        )

        pingV = round(self.client.latency * 1000)

        embed.set_author(name='🏓 Pong!')
        embed.add_field(name='Client Pong!', value=f'`{pingV} ms!`')

        await ctx.send (embed=embed)

    @commands.command(name="suggest")
    async def suggest(self, ctx, *, message=None):

        if message == None:
            await ctx.send("Please use `suggest [message here]`")
            return
        else:

            array = [1048575, 8137918, 16182940]
            value = random.choice(array)
            channel = await self.client.fetch_channel(789143685828837386)

            embed = discord.Embed(color=value, timestamp=ctx.message.created_at)
            embed.set_author(name=f"New Suggestion From {ctx.author}, Guild : {ctx.guild.name}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="Suggestion:", value=message)
            embed.set_footer(text=f"{ctx.author} • {ctx.guild.name}")

            msg = await channel.send(embed=embed)

            await msg.add_reaction('⬆️')
            await msg.add_reaction('⬇️')

            await ctx.send(f"{ctx.author.mention}, your suggestion has reached the dev! Support server : `https://discord.gg/CnhN4Jh`")

    @commands.command(name="bug_report", aliases = ['report'])
    async def report(self, ctx, *, message=None):

        if message == None:
            await ctx.send("Please use `report [message here]`")
            return
        else:

            array = [1048575, 8137918, 16182940]
            value = random.choice(array)
            channel = await self.client.fetch_channel(789143685828837386)

            embed = discord.Embed(color=value, timestamp=ctx.message.created_at)
            embed.set_author(name=f"New Bug Report From {ctx.author}, Guild : {ctx.guild.name}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="Report:", value=message)
            embed.set_footer(text=f"{ctx.author} • {ctx.guild.name}")

            msg = await channel.send(embed=embed)

            await msg.add_reaction('⬆️')
            await msg.add_reaction('⬇️')

            await ctx.send(f"{ctx.author.mention}, your report has reached the dev! Join support server for further problems : `https://discord.gg/CnhN4Jh`")

    @commands.command()
    async def userinfo(self, ctx, *, target : discord.Member=None):

        if target == None:
            target = ctx.author

        roles = [role for role in target.roles]
        roles = [role for role in target.roles if role != ctx.guild.default_role]


        embed = discord.Embed(title="User information", colour=discord.Color.gold(), timestamp=ctx.message.created_at)
        embed.set_author(name=target.name, icon_url=target.avatar_url)
        embed.set_thumbnail(url=target.avatar_url)
        embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)

        fields = [("Name", str(target), False),
            ("ID", target.id, False),
            ("Status", str(target.status).title(), False),
            (f"Roles ({len(roles)})", " ".join([role.mention for role in roles]), False),
            ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
            ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @commands.command()
    async def stats(self, ctx):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)


        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        memberCount = ctx.guild.member_count
        self.client.version = '1.4'
        embed = discord.Embed(title=f'{self.client.user.name} Stats', description='\uFEFF', colour=value, timestamp=ctx.message.created_at)

        embed.add_field(name='Bot Version:', value=self.client.version)
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Users:', value=memberCount)
        embed.add_field(name='Bot Developers:', value="Donut#4427")

        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def invites(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)
        embed = discord.Embed(title="Useful Invites", description="[**Invite Me**](https://discord.com/api/oauth2/authorize?client_id=787559221880815636&permissions=8&scope=bot) | [**Support Server**](https://discord.gg/Rp2RJjBEHp)", color=value)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Commands(client))