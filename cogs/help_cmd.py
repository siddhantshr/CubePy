import discord
from discord.ext import commands
import random
import sqlite3
import asyncio

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="help")
    async def help(self, ctx):

        if ctx.invoked_subcommand is None:
    
            try:
                db = sqlite3.connect("data/prefixes.sqlite")
                cursor = db.cursor()
                cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
                result = cursor.fetchone()

                prefix = result[0]
            except:
                prefix = "-"

            array = [1048575, 8137918, 16182940]

            value = random.choice(array)

            embed = discord.Embed(color=value)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
            embed.set_author(name="CubePy Help")
            embed.add_field(name="Navigating the pages:", value="◀️ : Previous Page \n⏹ : Stop help Screen \n▶️ : Next Page")
            embed.add_field(name="❓ | New To CubePy?", value="`CubePy is an easy to use cubing bot with all sorts of command you will ever need! Use this help page to get familiar with the bot!`", inline=False)
            embed.add_field(name="Contents:", value="**Page 1: **This Screen \n**Page 2: ** Numbered Cubes \n**Page 3: **Racing Page \n**Page 4: **Cube Relays \n**Page 5: **Non WCA and 3x3 Subsets \n**Page 6: **Fun Commands! \n**Page 7: **Utility Commands", inline=False)
            embed.add_field(name="Useful Links", value=f"[Invite Me](https://discord.com/api/oauth2/authorize?client_id=787559221880815636&permissions=8&scope=bot) | [Support Server](https://discord.gg/Rp2RJjBEHp)")
            embed.set_footer(text=f"Use {prefix} before each command!, use -help [page(number)] to view each page", icon_url=self.client.user.avatar_url)

            page2 = discord.Embed(color=value)
            page2.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
            page2.set_author(name="Numbered Cubes:")
            page2.add_field(name="WCA:", value="`2x2`, `3x3`, `4x4`, `5x5`, `6x6`, `7x7`")
            page2.add_field(name="Non WCA:", value="`8x8`, `9x9`")
            page2.add_field(name="Commmand Usage", value=f"`{prefix}[event name] [amount of scrambles (default = 1)]`", inline=False)

            race_page = discord.Embed(color=value)
            race_page.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
            race_page.set_author(name="Cube Racing:")
            race_page.add_field(name="Racing:", value="Gives two people a seperate channel for racing")
            race_page.add_field(name="Command Usage:", value=f"`{prefix}race [2x2|3x3|4x4|5x5] [member]`")


            page4 = discord.Embed(color=value)
            page4.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
            page4.set_author(name="Cube Relays")
            page4.add_field(name="Relays:", value="`2x2-3x3`, `2x2-4x4`, `2x2-5x5`, `2x2-6x6`, `2x2-7x7`")
            page4.add_field(name="Command Usage:", value=f"`{prefix}relay [relay name]`", inline=False)

            page5 = discord.Embed(color=value)
            page5.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
            page5.set_author(name="Non WCA:")
            page5.add_field(name="Cuboids", value="`1x1x2`, `1x3x3`, `2x2x3`, `superfloppy`, `3x3x2`")
            page5.add_field(name="3x3 Subsets", value="`edges`, `corners`, `LL`, `F2L`, `ez_cross`, `ZBLL`, `EOline`, `2GenRU`, `2GenLU`, `2GenMU`, `3GenFRU`, `3GenRUL`")
            page5.add_field(name="Command Usage:", value=f"`{prefix}[event] [amount of scrambles (default = 1)]`", inline=False)
            page5.add_field(name="Exception Usage:", value=f"`{prefix}ez_cross [amount] [cross moves (default = 3)]`", inline=False)

            page6 = discord.Embed(color=value)
            page6.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
            page6.set_author(name="Fun Commands:")
            page6.add_field(name="Commands:", value="`obese [user]`, `slap [user]`, `snipe`, `clap [text]`, `kill [member]`, `pp`, `howbald`, `8Ball [question]`, `treat [member]`, `ascii [text]`", inline=False)
            page6.add_field(name="GIFs:", value="`no`, `bruh`, `feliksGIF`, `jayden`")
            page6.add_field(name="Famous Scrambles:", value="`famous_scrams` for the list!")
            page6.add_field(name="Command Usage:", value="`Given with the commands ^^`")

            page7 = discord.Embed(color=value)
            page7.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
            page7.set_author(name="Utility Commands:")
            page7.add_field(name="Commands:", value="`prefix`, `prefix set [new prefix]`, `prefix view`, `members`, `ping`, `suggest [message]`, `report [message]`, `userinfo`, `stats`, `invites`, `dev`")
            page7.add_field(name="Command Usage:", value=f"`{prefix}command`")


            pages = 7
            cur_page = 1
            message = await ctx.send(embed=embed)
            # getting the message object for editing and reacting

            await message.add_reaction("◀️")
            await message.add_reaction("⏹")
            await message.add_reaction("▶️")

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["◀️", "⏹", "▶️"]
                # This makes sure nobody except the command sender can interact with the "menu"

            while True:
                try:
                    reaction, user = await self.client.wait_for("reaction_add", timeout=60, check=check)
                    # waiting for a reaction to be added - times out after x seconds, 60 in this
                    # example

                    if str(reaction.emoji) == "▶️" and cur_page != pages:
                        cur_page += 1
                        if cur_page == 2:
                            await message.edit(embed=page2)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 3:
                            await message.edit(embed=race_page)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 4:
                            await message.edit(embed=page4)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 5:
                            await message.edit(embed=page5)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 6:
                            await message.edit(embed=page6)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 7:
                            await message.edit(embed=page7)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass

                    elif str(reaction.emoji) == "◀️" and cur_page > 1:
                        cur_page -= 1
                        if cur_page == 1:
                            await message.edit(embed=embed)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 2:
                            await message.edit(embed=page2)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 3:
                            await message.edit(embed=race_page)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 4:
                            await message.edit(embed=page4)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 5:
                            await message.edit(embed=page5)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass
                        elif cur_page == 6:
                            await message.edit(embed=page6)
                            try:
                                await message.remove_reaction(reaction, user)
                            except:
                                pass

                    elif str(reaction.emoji) == "⏹":
                        try:
                            await message.clear_reaction("◀️")
                            await message.clear_reaction("⏹")
                            await message.clear_reaction("▶️")
                        except:
                            pass
                        await message.edit(content="Stopped the help screen!")

                    else:
                        await message.remove_reaction(reaction, user)
                        # removes reactions if the user tries to go forward on the last page or
                        # backwards on the first page
                except asyncio.TimeoutError:
                    try:
                        await message.clear_reaction("◀️")
                        await message.clear_reaction("⏹")
                        await message.clear_reaction("▶️")
                    except:
                        pass
                    break
                    # ending the loop if user doesn't react after x seconds



    @help.command(name="1")
    async def page1(self, ctx):

        try:
            db = sqlite3.connect("data/prefixes.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
            result = cursor.fetchone()

            prefix = result[0]
        except:
            prefix = "-"

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        embed = discord.Embed(color=value)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
        embed.set_author(name="CubePy Help")
        embed.add_field(name="Navigating the pages:", value="◀️ : Previous Page \n⏹ : Stop help Screen \n▶️ : Next Page")
        embed.add_field(name="❓ | New To CubePy?", value="`CubePy is an easy to use cubing bot with all sorts of command you will ever need! Use this help page to get familiar with the bot!`", inline=False)
        embed.add_field(name="Contents:", value="**Page 1: **This Screen \n**Page 2: ** Numbered Cubes \n**Page 3: **Racing Page \n**Page 4: **Cube Relays \n**Page 5: **Non WCA and 3x3 Subsets \n**Page 6: **Fun Commands! \n**Page 7: **Utility Commands", inline=False)
        embed.add_field(name="Useful Links", value=f"[Invite Me](https://discord.com/api/oauth2/authorize?client_id=787559221880815636&permissions=8&scope=bot) | [Support Server](https://discord.gg/Rp2RJjBEHp)")
        embed.set_footer(text=f"Use {prefix} before each command!", icon_url=self.client.user.avatar_url)

        await ctx.send(embed=embed)

    @help.command(name="2")
    async def page2(self, ctx):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        try:
            db = sqlite3.connect("data/prefixes.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
            result = cursor.fetchone()

            prefix = result[0]
        except:
            prefix = "-"    


        page2 = discord.Embed(color=value)
        page2.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
        page2.set_author(name="Numbered Cubes:")
        page2.add_field(name="WCA:", value="`2x2`, `3x3`, `4x4`, `5x5`, `6x6`, `7x7`")
        page2.add_field(name="Non WCA:", value="`8x8`, `9x9`")
        page2.add_field(name="Commmand Usage", value=f"`{prefix}[event name] [amount of scrambles (default = 1)]`", inline=False)

        await ctx.send(embed=page2)

    @help.command(name="3")
    async def page3(self, ctx):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        try:
            db = sqlite3.connect("data/prefixes.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
            result = cursor.fetchone()

            prefix = result[0]
        except:
            prefix = "-"  

        race_page = discord.Embed(color=value)
        race_page.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
        race_page.set_author(name="Cube Racing:")
        race_page.add_field(name="Racing:", value="Gives two people a seperate channel for racing")
        race_page.add_field(name="Command Usage:", value=f"`{prefix}race [2x2|3x3|4x4|5x5] [member]`")

        await ctx.send(embed=race_page)    


    @help.command(name="4")
    async def page4(self, ctx):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        try:
            db = sqlite3.connect("data/prefixes.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
            result = cursor.fetchone()

            prefix = result[0]
        except:
            prefix = "-"   

        page4 = discord.Embed(color=value)
        page4.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
        page4.set_author(name="Cube Relays")
        page4.add_field(name="Relays:", value="`2x2-3x3`, `2x2-4x4`, `2x2-5x5`, `2x2-6x6`, `2x2-7x7`")
        page4.add_field(name="Command Usage:", value=f"`{prefix}relay [relay name]`", inline=False)

        await ctx.send(embed=page4)

    @help.command(name="5")
    async def page5(self, ctx):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        try:
            db = sqlite3.connect("data/prefixes.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
            result = cursor.fetchone()

            prefix = result[0]
        except:
            prefix = "-"  

        page5 = discord.Embed(color=value)
        page5.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
        page5.set_author(name="Non WCA:")
        page5.add_field(name="Cuboids", value="`1x1x2`, `1x3x3`, `2x2x3`, `superfloppy`, `3x3x2`")
        page5.add_field(name="3x3 Subsets", value="`edges`, `corners`, `LL`, `F2L`, `ez_cross`, `ZBLL`, `EOline`, `2GenRU`, `2GenLU`, `2GenMU`, `3GenFRU`, `3GenRUL`")
        page5.add_field(name="Command Usage:", value=f"`{prefix}[event] [amount of scrambles (default = 1)]`", inline=False)
        page5.add_field(name="Exception Usage:", value=f"`{prefix}ez_cross [amount] [cross moves (default = 3)]`", inline=False)

        await ctx.send(embed=page5)      

    @help.command(name="6")
    async def page6(self, ctx):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        try:
            db = sqlite3.connect("data/prefixes.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
            result = cursor.fetchone()

            prefix = result[0]
        except:
            prefix = "-"  

        page6 = discord.Embed(color=value)
        page6.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
        page6.set_author(name="Fun Commands:")
        page6.add_field(name="Commands:", value="`obese [user]`, `slap [user]`, `snipe`, `clap [text]`, `kill [member]`, `pp`, `howbald`, `8Ball [question]`, `treat [member]`, `ascii [text]`", inline=False)
        page6.add_field(name="GIFs:", value="`no`, `bruh`, `feliksGIF`, `jayden`")
        page6.add_field(name="Famous Scrambles:", value="`famous_scrams` for the list!")
        page6.add_field(name="Command Usage:", value="`Given with the commands ^^`")

        await ctx.send(embed=page6)

    @help.command(name="7")
    async def page7(self, ctx):

        array = [1048575, 8137918, 16182940]

        value = random.choice(array)

        try:
            db = sqlite3.connect("data/prefixes.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {ctx.guild.id}")
            result = cursor.fetchone()

            prefix = result[0]
        except:
            prefix = "-"  

        page7 = discord.Embed(color=value)
        page7.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
        page7.set_author(name="Utility Commands:")
        page7.add_field(name="Commands:", value="`prefix`, `prefix set [new prefix]`, `prefix view`, `members`, `ping`, `suggest [message]`, `report [message]`, `userinfo`, `stats`, `invites`")
        page7.add_field(name="Command Usage:", value=f"`{prefix}command`")

        await ctx.send(embed=page7)

def setup(client):
    client.add_cog(Commands(client))