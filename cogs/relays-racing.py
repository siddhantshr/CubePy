import discord
from discord.ext import commands
import random
from pyTwistyScrambler import scrambler333, scrambler222, scrambler444, scrambler555, scrambler666, scrambler777
import asyncio

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="relay", aliases=["rel", "manycubes"])
    async def relay(self, ctx):
        if ctx.invoked_subcommand is None:
            array = [1048575, 8137918, 16182940]
            value = random.choice(array)

            embed=discord.Embed(title="Cube Relay!", description="2x2-3x3, 2x2-4x4, 2x2-5x5, 2x2-6x6, 2x2-7x7", colour=value)

            await ctx.send(embed=embed)

    @relay.command(name="2x2-3x3", aliases=['2-3'])
    async def twotothree(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        two = scrambler222.get_WCA_scramble()
        three = scrambler333.get_WCA_scramble()

        embed=discord.Embed(title="Cube Relay!", colour=value)
        embed.add_field(name="2x2", value=two, inline=False)
        embed.add_field(name="3x3", value=three, inline=False)

        await ctx.send(embed=embed)

    @relay.command(name="2x2-4x4", aliases=['2-4'])
    async def twotofour(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        two = scrambler222.get_WCA_scramble()
        three = scrambler333.get_WCA_scramble()
        four = scrambler444.get_WCA_scramble()

        embed=discord.Embed(title="Cube Relay!", colour=value)
        embed.add_field(name="2x2", value=two, inline=False)
        embed.add_field(name="3x3", value=three, inline=False)
        embed.add_field(name="4x4", value=four, inline=False)

        await ctx.send(embed=embed)

    @relay.command(name="2x2-5x5", aliases=['2-5'])
    async def twotofive(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        two = scrambler222.get_WCA_scramble()
        three = scrambler333.get_WCA_scramble()
        four = scrambler444.get_WCA_scramble()
        five = scrambler555.get_WCA_scramble()

        embed=discord.Embed(title="Cube Relay!", colour=value)
        embed.add_field(name="2x2", value=two, inline=False)
        embed.add_field(name="3x3", value=three, inline=False)
        embed.add_field(name="4x4", value=four, inline=False)
        embed.add_field(name="5x5", value=five, inline=False)

        await ctx.send(embed=embed)


    @relay.command(name="2x2-6x6", aliases=['2-6'])
    async def twotosix(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        two = scrambler222.get_WCA_scramble()
        three = scrambler333.get_WCA_scramble()
        four = scrambler444.get_WCA_scramble()
        five = scrambler555.get_WCA_scramble()
        six = scrambler666.get_WCA_scramble()

        embed=discord.Embed(title="Cube Relay!", colour=value)
        embed.add_field(name="2x2", value=two, inline=False)
        embed.add_field(name="3x3", value=three, inline=False)
        embed.add_field(name="4x4", value=four, inline=False)
        embed.add_field(name="5x5", value=five, inline=False)
        embed.add_field(name="6x6", value=six, inline=False)

        await ctx.send(embed=embed)

    @relay.command(name="2x2-7x7", aliases=['2-7'])
    async def twotoseven(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        two = scrambler222.get_WCA_scramble()
        three = scrambler333.get_WCA_scramble()
        four = scrambler444.get_WCA_scramble()
        five = scrambler555.get_WCA_scramble()
        six = scrambler666.get_WCA_scramble()
        seven = scrambler777.get_WCA_scramble()

        embed=discord.Embed(title="Cube Relay!", colour=value)
        embed.add_field(name="2x2", value=two, inline=False)
        embed.add_field(name="3x3", value=three, inline=False)
        embed.add_field(name="4x4", value=four, inline=False)
        embed.add_field(name="5x5", value=five, inline=False)
        embed.add_field(name="6x6", value=six, inline=False)
        embed.add_field(name="7x7", value=seven, inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def race(self, ctx, event, member : discord.Member=None):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        if event == None or member == None:
            self.client.get_command("race").reset_cooldown(ctx)
            await ctx.send("```Please mention all the required arguments: \n[prefix]race event[3x3] member[mention the member] ```")
            return
        if member.id == ctx.author.id:
            self.client.get_command("race").reset_cooldown(ctx)
            await ctx.send("Please dont mention yourself")
            return
        if member.bot:
            self.client.get_command("race").reset_cooldown(ctx)
            return await ctx.send(
                "That member is a bot! :|"
            )
        events = ['3x3', '4x4', '5x5', '2x2']
        if event not in events:
            self.client.get_command("race").reset_cooldown(ctx)
            return await ctx.send(
                f"{event} is not a valid event! Choose (2x2|3x3|4x4|5x5)"
            )
        embed=discord.Embed(
            description=f'{member.mention}, please react with 🏁 to start the race',
            color=value
        )
        timeout=int(15.0)
        message = await ctx.channel.send(embed=embed)

        await message.add_reaction('🏁')
        
        def check(reaction, user):
            return user == member and str(reaction.emoji) == '🏁'
            
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=timeout, check=check)
            
        except asyncio.TimeoutError:
            self.client.get_command("race").reset_cooldown(ctx)
            msg=(f"{member.mention} didn't react in time!!")
            await ctx.channel.send(msg)
            
        else:
            
            await ctx.send("Starting the game!!")

            if event == '3x3':

                guild = ctx.guild
                author = ctx.author
                user = member

                channel = await guild.create_text_channel(f'RACE-3x3')

                await channel.set_permissions(guild.default_role, read_messages=False)
                await channel.set_permissions(author, read_messages=True)
                await channel.set_permissions(user, read_messages=True)

                scrambles = []
                scrambles.append(scrambler333.get_WCA_scramble())
                a = 0
                s = 1
                amount = 4

                await channel.send(f"{ctx.author.mention}, {user.mention} Good luck!")

                for i in range(amount):
                    scrambles.append(scrambler333.get_WCA_scramble())
                    a+=1
                    s+=1
                
                for scr in scrambles:
                    msg = await channel.send(scr)
                    await msg.add_reaction("<a:DC_verified2:801699442495062016>")

                delete_em = discord.Embed(title="React with ❌ to end the race!", color=author.color)

                msg_em = await channel.send(embed=delete_em)

                await msg_em.add_reaction('❌')

                def check_del(reaction, user):
                    return (user == member or user == ctx.author)and str(reaction.emoji) == '❌'
                
                for i in range(2):
                    reaction, user = await self.client.wait_for('reaction_add', check=check_del)
                    if i == 1:
                        channelID = channel.id
                        channel = self.client.get_channel(id = channelID)
                        await channel.delete()
                        await ctx.send(f"Finished the match!! {ctx.author.mention}, {member.mention}")

            elif event == '2x2':


                guild = ctx.guild
                author = ctx.author
                user = member

                channel = await guild.create_text_channel(f'RACE-2x2')

                await channel.set_permissions(guild.default_role, read_messages=False)
                await channel.set_permissions(author, read_messages=True)
                await channel.set_permissions(user, read_messages=True)

                scrambles = []
                scrambles.append(scrambler222.get_WCA_scramble())
                a = 0
                s = 1
                amount = 4

                await channel.send(f"{ctx.author.mention}, {user.mention} Good luck!")

                for i in range(amount):
                    scrambles.append(scrambler222.get_WCA_scramble() )
                    a+=1
                    s+=1
                
                for scr in scrambles:
                    msg = await channel.send(scr)
                    await msg.add_reaction("<a:DC_verified2:801699442495062016>")

                delete_em = discord.Embed(title="React with ❌ to end the race!", color=author.color)

                msg_em = await channel.send(embed=delete_em)

                await msg_em.add_reaction('❌')

                def check_del(reaction, user):
                    return (user == member or user == ctx.author )and str(reaction.emoji) == '❌'
                
                for i in range(2):
                    reaction, user = await self.client.wait_for('reaction_add', check=check_del)
                    if i == 1:
                        channelID = channel.id
                        channel = self.client.get_channel(id = channelID)
                        await channel.delete()
                        await ctx.send(f"Finished the match!! {ctx.author.mention}, {member.mention}")

            elif event == '4x4':

                guild = ctx.guild
                author = ctx.author
                user = member

                channel = await guild.create_text_channel(f'RACE-4x4')

                await channel.set_permissions(guild.default_role, read_messages=False)
                await channel.set_permissions(author, read_messages=True)
                await channel.set_permissions(user, read_messages=True)

                scrambles = []
                scrambles.append(scrambler444.get_WCA_scramble())
                a = 0
                s = 1
                amount = 4

                await channel.send(f"{ctx.author.mention}, {user.mention} Good luck!")

                for i in range(amount):
                    scrambles.append(scrambler444.get_WCA_scramble() )
                    a+=1
                    s+=1
                
                for scr in scrambles:
                    msg = await channel.send(scr)
                    await msg.add_reaction("<a:DC_verified2:801699442495062016>")

                delete_em = discord.Embed(title="React with ❌ to end the race!", color=author.color)

                msg_em = await channel.send(embed=delete_em)

                await msg_em.add_reaction('❌')

                def check_del(reaction, user):
                    return (user == member or user == ctx.author )and str(reaction.emoji) == '❌'
                
                for i in range(2):
                    reaction, user = await self.client.wait_for('reaction_add', check=check_del)
                    if i == 1:
                        channelID = channel.id
                        channel = self.client.get_channel(id = channelID)
                        await channel.delete()
                        await ctx.send(f"Finished the match!! {ctx.author.mention}, {member.mention}")

            elif event == '5x5':

                guild = ctx.guild
                author = ctx.author
                user = member

                channel = await guild.create_text_channel(f'RACE-5x5')

                await channel.set_permissions(guild.default_role, read_messages=False)
                await channel.set_permissions(author, read_messages=True)
                await channel.set_permissions(user, read_messages=True)

                scrambles = []
                scrambles.append(scrambler555.get_WCA_scramble())
                a = 0
                s = 1
                amount = 4

                await channel.send(f"{ctx.author.mention}, {user.mention} Good luck!")

                for i in range(amount):
                    scrambles.append(scrambler555.get_WCA_scramble() )
                    a+=1
                    s+=1
                
                for scr in scrambles:
                    msg = await channel.send(scr)
                    await msg.add_reaction("<a:DC_verified2:801699442495062016>")

                delete_em = discord.Embed(title="React with ❌ to end the race!", color=author.color)

                msg_em = await channel.send(embed=delete_em)

                await msg_em.add_reaction('❌')

                def check_del(reaction, user):
                    return (user == member or user == ctx.author )and str(reaction.emoji) == '❌'
                
                for i in range(2):
                    reaction, user = await self.client.wait_for('reaction_add', check=check_del)
                    if i == 1:
                        channelID = channel.id
                        channel = self.client.get_channel(id = channelID)
                        await channel.delete()
                        await ctx.send(f"Finished the match!! {ctx.author.mention}, {member.mention}")

            else:
                pass

def setup(client):
    client.add_cog(Commands(client))