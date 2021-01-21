import discord
from discord.ext import commands
# NxNs
from pyTwistyScrambler import scrambler333, scrambler222, scrambler444, scrambler555, scrambler666, scrambler777
# Other WCA
from pyTwistyScrambler import megaminxScrambler, squareOneScrambler, skewbScrambler, pyraminxScrambler, clockScrambler

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # <------------------------ NxNs ------------------------>

    @commands.command(name="2x2", aliases=['2*2', '2'], case_insensitive=True)
    async def twobytwo(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler222.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler222.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="3x3", aliases=['3*3', '3'], case_insensitive=True)
    async def threebythree(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="4x4", aliases=['4*4', '4'], case_insensitive=True)
    async def fourbyfour(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler444.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler444.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="5x5", aliases=['5*5', '5'], case_insensitive=True)
    async def fivebyfive(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler555.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler555.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")\

    @commands.command(name="6x6", aliases=['6*6', '6'], case_insensitive=True)
    async def sixbysix(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler666.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler666.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="7x7", aliases=['7*7', '7'], case_insensitive=True)
    async def sevenbyseven(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler777.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler777.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    # <------------------------ Other so called (cubes) ------------------------>

    @commands.command(name="skewb", aliases=['s'], case_insensitive=True)
    async def skewb(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(skewbScrambler.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(skewbScrambler.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="pyraminx", aliases=['p', 'pyra'], case_insensitive=True)
    async def pyra(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(pyraminxScrambler.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(pyraminxScrambler.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="clock", aliases=['c', 'clok'], case_insensitive=True)
    async def clock(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(clockScrambler.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(clockScrambler.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="megaminx", aliases=['mega', 'm'], case_insensitive=True)
    async def mega(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(megaminxScrambler.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(megaminxScrambler.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="squan", aliases=['s1', 'square1'], case_insensitive=True)
    async def squan(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Use a smaller number!"
            )

        scrambles = []
        scrambles.append(squareOneScrambler.get_WCA_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(squareOneScrambler.get_WCA_scramble() )
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

def setup(client):
    client.add_cog(Commands(client))