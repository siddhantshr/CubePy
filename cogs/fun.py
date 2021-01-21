import discord, json, random, pyfiglet, asyncio
from http import client as http_client
from urllib import parse as urllib_parse
from discord.ext import commands
from PIL import Image
from io import BytesIO

deletes = {"channel" : [], "guild" : [], "user" : [], "content" : []}
class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        deletes["channel"].append(message.channel)
        deletes["guild"].append(message.guild)
        deletes["user"].append(message.author)
        deletes["content"].append(message.content)

    #famous scrams

    @commands.group(name="famous-scrams", aliases=['famous-scrambles', 'famous_scrambles', 'cubegobr'])
    async def famous_scrams(self, ctx):

        if ctx.invoked_subcommand is None:
            array = [1048575, 8137918, 16182940]
            value = random.choice(array)

            embed=discord.Embed(title="Famous Scrambles", description="lucas5, wr, max3, feliks4.22", color=value)
            await ctx.send(embed=embed)

    @famous_scrams.command(name="lucas5", aliases=['firstsub5', 'sub5', 'lucas'])
    async def lucas4(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        embed = discord.Embed(title="Lucas's 4.90 (First Ever Sub 5)", description="R2 B D2 F2 U2 R D2 L' B L' B D R' F' U B2 F L", color=value)
        await ctx.send(embed=embed)

    @famous_scrams.command(name="wr", aliases=['wr3.47', '3.47', 'yusheng'])
    async def worldrecord(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        embed = discord.Embed(title="Yusheg Du's 3.47:", description="F U2 L2 B2 F' U L2 U R2 D2 L' B L2 B' R2 U2", color=value)
        await ctx.send(embed=embed)

    @famous_scrams.command(name="max3.36", aliases=['max', 'sub4', 'max3.3'])
    async def max3(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        embed = discord.Embed(title="Max's 3.36:", description="B2 R2 U’ L2 F2 D B2 D R2 U B2 R U B’ D’ F U L’ D’ R2 D", color=value)
        await ctx.send(embed=embed)

    @famous_scrams.command(name="feliks4.22", aliases=['feliks', 'felikszemdegs', '4.22'])
    async def feliks4(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        embed = discord.Embed(title="Felik's 4.22:", description="L U2 D R' F2 R2 L2 U R' F' D2 F2 D2 B U L2 B2", color=value)
        await ctx.send(embed=embed)

    @commands.command(name="no", aliases=['nope', 'nah'])
    async def nobruh(self, ctx):

        await ctx.send("https://tenor.com/view/shannon-sharpe-shay-nope-nah-nuhuh-gif-12298561")

    @commands.command(name="feliks4.22GIF", aliases = ['4.22GIF', 'feliksGIF'])
    async def feliksGIF(self, ctx):

        await ctx.send("https://tenor.com/view/feliks-zemdegs-rubiks-cube-speed-world-record-fast-gif-17286533")

    @commands.command(name="jay", aliases=['jayden', '4.97'])
    async def jayden(self, ctx):

        await ctx.send("True pain press F")
        await ctx.send("https://media.discordapp.net/attachments/735362819012296758/788731191507157062/jayden-min.gif")

    @commands.command(name="cat", aliases=['catGIF', 'bruh'])
    async def catbruh(self, ctx):

        await ctx.send("BRUH")
        await ctx.send("https://tenor.com/view/cat-vibeing-vibing-cat-vibing-gif-16906597")

    # more fun :D

    @commands.command()
    async def obese(self, ctx, user : discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open("obese.png")
        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((341,342))
        wanted.paste(pfp, (460,113))
        wanted.save("Opic.jpg")

        await ctx.send(file = discord.File("Opic.jpg"))

    @commands.command()
    async def snipe(self, ctx):

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)

        for delete in deletes["guild"]:
            if delete.id == ctx.guild.id:
                index = deletes["guild"].index(delete)
                for channel in deletes["channel"]:
                    var = deletes["channel"].index(channel)
                    if index == var:
                        index_num = deletes["channel"].index(channel)
                        found = True

        if found:
            author = deletes["user"][index_num]
            msg = deletes["content"][index_num]
            embed = discord.Embed(title=f"{author.name}#{author.discriminator}", description=f"Message: {msg}", color=value)
            embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)
        else:
            await ctx.send("There's nothing to snipe!")

    @commands.command()
    async def slap(self, ctx, user : discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open("slap.png")

        asset = user.avatar_url_as(size = 128)
        asset2 = ctx.author.avatar_url_as(size = 128)

        data = BytesIO(await asset.read())
        data2 = BytesIO(await asset2.read())

        pfp = Image.open(data)
        pfp2 = Image.open(data2)

        pfp = pfp.resize((219,219))
        pfp2 = pfp2.resize((200,200))
        wanted.paste(pfp2, (350,70))
        wanted.paste(pfp, (581,261))
        wanted.save("Spic.jpg")

        await ctx.send(file = discord.File("Spic.jpg"))

    @commands.command()
    async def clap(self, ctx, text):
        length = len(text)
        part1 = text[:length//2]
        part2 = text[length//2:]

        await ctx.send(f"{part1} :clap: {part2}")

    @commands.command()
    async def kill(self, ctx, member : discord.Member):
        responses = [f"{ctx.author.mention} punched {member.mention} hard on the face and he died :'( press F to pay respect",
                    f"{member.mention} died of hunger, F",
                    f"{member.mention} was shot by a skeleton",
                    f"{member.mention} was blown up by a nuclear bomb",
                    f"{ctx.author.mention} pushed {member.mention} from a cliff",
                    f"{member.mention} stared at discord for 10 hours straight",
                    f"{member.mention} died of corona f",
                    f"{member.mention} froze to death",
                    f"{member.mention} went bald and got insulted to death",
                    f"{ctx.author.mention} pushed {member.mention} under a truck",
                    f"{ctx.author.mention} shot {member.mention}",
                    f"{member.mention} said no to a Donut"]

        await ctx.send(random.choice(responses))

    @commands.command()
    async def pp(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.author
        array = [1048575, 8137918, 16182940]
        value = random.choice(array)
        string = "8" + ("=" * random.randrange(0, 15)) + "D"
        embed = discord.Embed(title="PP Machine!", description=f"{member.mention}'s PP size: \n {string}", color=value)

        await ctx.send(embed=embed)

    @commands.command()
    async def howbald(self, ctx, member : discord.Member=None):

        if not member:
            member = ctx.author

        array = [1048575, 8137918, 16182940]
        value = random.choice(array)
        num1 = random.randint(0, 100)

        embed = discord.Embed(title="Bald rate machine", description=f"{member.mention}'s Bald rate: \n {num1}.69%", color=value)

        await ctx.send(embed=embed)

    # from Div_100
    @commands.command(name="8ball", aliases=['eightball', 'question'])
    async def ball(self, ctx, *, question):
        # Connecting to the API :)
        conn = http_client.HTTPSConnection("8ball.delegator.com")
        question = urllib_parse.quote(str(question))
        conn.request('GET', '/magic/JSON/' + question)
        response = conn.getresponse()
        data = json.loads(response.read())['magic']

        # Setting up some variables :|
        type_of_answer = data['type']
        answer = data['answer']
        question = data['question']
        embed = discord.Embed(title="8ball...")
        avatar = self.client.get_user(ctx.message.author.id).avatar_url

        # Setting up the embed
        embed.set_author(name=str(ctx.message.author), icon_url=avatar)
        if type_of_answer == "Contrary":
            embed.colour = discord.Colour.red()
        elif type_of_answer == "Affirmative":
            embed.colour = discord.Colour.blue()
        elif type_of_answer == "Neutral":
            embed.colour = discord.Colour.from_rgb(255, 255, 255)

        embed.add_field(name="Question: ", value=f"{question}", inline=False)
        embed.add_field(name="Answer: ", value=f"{answer}", inline=False)

        await ctx.send(embed=embed)

    # by Div lmfart
    @commands.command(case_insensitive=True)
    async def treat(self, ctx, member:discord.Member):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        if member == ctx.author:
            await ctx.send("You can't treat youself!")
            return
        embed=discord.Embed(
            description=f'You offered {member.name} a treat! {member.mention} react to the emoji below to accept!',
            color=value
        )
        timeout=int(15.0)
        message = await ctx.channel.send(embed=embed)

        await message.add_reaction('🍫')
        
        def check(reaction, user):
            return user == member and str(reaction.emoji) == '🍫'
            
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=timeout, check=check)
            
        except asyncio.TimeoutError:
            msg=(f"{member.mention} didn't accept the treat in time!!")
            await ctx.channel.send(msg)

        else:
            await ctx.channel.send(f"{member.mention} You have accepted {ctx.author.name}'s offer!")

    @commands.command()
    async def ascii(self, ctx, *, text=None):
        if text is None:
            return await ctx.send("You must input some text to make into Ascii!")
        result = pyfiglet.figlet_format(text)

        await ctx.send(f"``` \n {result} \n ```")

def setup(client):
    client.add_cog(Commands(client))