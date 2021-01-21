import discord
from discord.ext import commands
from pyTwistyScrambler import cuboidsScrambler, scrambler333

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="1x1x2")
    async def onebyonebytwo(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(cuboidsScrambler.get_1x1x2_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(cuboidsScrambler.get_1x1x2_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="1x3x3", aliases = ['floppycube'])
    async def onebythreebythree(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(cuboidsScrambler.get_1x3x3_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(cuboidsScrambler.get_1x3x3_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="2x2x3")
    async def twobytwobythree(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(cuboidsScrambler.get_2x2x3_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(cuboidsScrambler.get_2x2x3_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="superfloppy")
    async def superfloppy(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(cuboidsScrambler.get_super_floppy_cube_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(cuboidsScrambler.get_super_floppy_cube_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")
        
    @commands.command(name="3x3x2")
    async def threebythreebytwo(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(cuboidsScrambler.get_3x3x2_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(cuboidsScrambler.get_3x3x2_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    # 3x3 subsets 

    @commands.command(name="edges-only", aliases = ['edges_only'])
    async def edges(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_edges_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_edges_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="corners", aliases = ['corners-only'])
    async def corners_only(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_corners_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_corners_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")


    @commands.command(name="ll", aliases = ['last-layer', 'last_layer'])
    async def last_layer(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_LL_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_LL_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="f2l")
    async def firsttwolayers(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_F2L_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_F2L_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="ez_cross", aliases=['easy_cross'])
    async def easy_cross(self, ctx, amount=1, number=3):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        if number < 1 or number > 8:
            await ctx.send("Please choose a number in a range from 1 to 8")
            return

        scrambles = []
        scrambles.append(scrambler333.get_easy_cross_scramble(n=number))
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_easy_cross_scramble(n=number))
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="ZBLL", aliases = ['ZB'])
    async def ZBLL(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_ZBLL_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_ZBLL_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="EO", aliases = ['EOline'])
    async def EO(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_EOLine_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_EOLine_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="2GRU", aliases = ['2GenRU'])
    async def twogenRU(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_2genRU_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_2genRU_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="2GLU", aliases = ['2GenLU'])
    async def twogenLU(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_2genLU_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_2genLU_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="2GMU", aliases = ['2GenMU'])
    async def twogenMU(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_2genMU_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_2genMU_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="3GFRU", aliases = ['3GenFRU'])
    async def threegenFRU(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_3genFRU_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_3genFRU_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

    @commands.command(name="3GRUL", aliases = ['3GenRUL'])
    async def threegenRUL(self, ctx, *, amount=1):

        if amount > 25:
            return await ctx.send(
                "Please give a smaller number!"
            )

        scrambles = []
        scrambles.append(scrambler333.get_3genRUL_scramble())
        a = 0
        s = 1
        for i in range(amount):
            msg = await ctx.send(str(s) + ") " + str(scrambles[a]) + "\n")
            scrambles.append(scrambler333.get_3genRUL_scramble())
            a+=1
            s+=1
            
            await msg.add_reaction("<a:DC_verified2:801699442495062016>")

def setup(client):
    client.add_cog(Commands(client))