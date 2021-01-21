import discord, os, random, sqlite3
from discord.ext import commands, tasks
from discord.ext.commands import when_mentioned_or
from discord import Intents
from data.secrets import secrets
intents = Intents.all()

def get_prefix(client,message):

    try: 
        db = sqlite3.connect("data/prefixes.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT PREFIX FROM guild WHERE GuildID = {message.guild.id}")
        result = cursor.fetchone()

        prefix = result[0]

        return when_mentioned_or(prefix)(client, message)
    except:
        return "-"

client = commands.Bot(
    command_prefix=get_prefix,
    allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=True),
    intents=intents,
    case_sensitive=False,
)

client.remove_command('help')

@client.command(name="load")
async def load(ctx, extension):
    if ctx.author.id == 711444754080071714:
        try:
            client.load_extension(f'cogs.{extension.lower()}')
            await ctx.send(f"> <a:DC_verified2:749472983487217694> loaded {extension}!")
        except:
            await ctx.send(f"{extension} is either not loaded or is not there")
    else:
        await ctx.send("Are you donut?")

@client.command(name="unload")
async def unload(ctx, extension):
    if ctx.author.id == 711444754080071714:
        try:
            client.unload_extension(f'cogs.{extension.lower()}')
            await ctx.send(f"> <a:DC_verified2:749472983487217694> Unloaded {extension}!")
        except:
            await ctx.send(f"{extension} is either not loaded or is not there")
    else:
        await ctx.send("Are you donut?")

@client.command(name="reload")
async def reload(ctx):
    if ctx.author.id == 711444754080071714:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
                client.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded {filename[:-3]}")

        await ctx.send(f"> <a:DC_verified2:749472983487217694> Reloaded all!")
    else:
        await ctx.send("Are you donut?")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded {filename[:-3]}")

@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")
    change_status.start()

status = ['Jamming out to music', 'With Beer 🍻 ', 'Watching Donuts Café!!: https://discord.gg/xV98GwE', 'Minecraft', "Donut's Cafe Security!"]

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(random.choice(status)))

@client.event
async def on_guild_join(guild):

    channel = await client.fetch_channel(789054704491429893)
    embed = discord.Embed(title="New Guild Join!", description=f"CubePy was added to {guild.name}, total guilds = {len(client.guilds)}")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
    await channel.send(embed=embed)

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages and channel.permissions_for(guild.me).embed_links:

            array = [1048575, 8137918, 16182940]
            value = random.choice(array)

            join_embed = discord.Embed(title="CubePy Info", description=f"Heya! 👋🏻 Thanks For adding me to your server! The default prefix is `-`, hope you enjoy using me!", color=value)
            join_embed.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")
            join_embed.add_field(name="Useful Links", value=f"[Invite Me](https://discord.com/api/oauth2/authorize?client_id=787559221880815636&permissions=8&scope=bot) | [Support Server](https://discord.gg/Rp2RJjBEHp)", inline=False)

            await channel.send(embed=join_embed)

            break

@client.event
async def on_guild_remove(guild):

    channel = await client.fetch_channel(789054704491429893)

    embed = discord.Embed(title="Guild Leave:", description=f"CubePy was removed from {guild.name}, total guilds = {len(client.guilds)}")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/715556818939805717/789165095980499004/cubepygif.gif")

    await channel.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    error = getattr(error, "original", error)

    # They Didn't run a valid command
    if isinstance(error, commands.errors.CommandNotFound):
        pass

    # They were an Idiot and thought could use that command ;-;
    elif isinstance(error, commands.errors.MissingPermissions):
        permissions = []
        for perm in error.missing_perms:
            permissions.append(f"`{perm}`")
        permissions = ", ".join(permissions)
        await ctx.send(
            f"> <:NO:801699177934618634> You are missing the {permissions} permission(s)!" # works
        )

    # CooooooooooooooooooooooooolDown
    elif isinstance(error, commands.errors.CommandOnCooldown):
        message = await ctx.send(
            f"> <:NO:801699177934618634> You Are on Cool down, Try again in \
{round(ctx.command.get_cooldown_retry_after(ctx))} seconds") # works

    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"> <:NO:801699177934618634> {error.param.name} is a required argument :|") #  works

    elif isinstance(error, discord.ext.commands.errors.RoleNotFound):
        await ctx.send(f"> <:NO:801699177934618634> {error.argument} is not a valid role!") # works
    
    elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
        await ctx.send(f"> <:NO:801699177934618634> {error.argument} is not a valid member!") # works

    elif isinstance(error, discord.ext.commands.errors.ChannelNotFound):
        await ctx.send(f"> <:NO:801699177934618634> {error.argument} is not a valid channel!") # works

    elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
        await ctx.send("I dont seem to have the permissions required to do this action..") # works

    elif isinstance(error, discord.Forbidden): # works
        try:
        	await ctx.send("I dont seem to have the permissions required to do this action..")
        except:
            print(f"Some Duffer in the server {ctx.guild.name}, Forgot to give me send_messages Perms. ;-;")
    else:
        raise error

client.run(secrets['token'])