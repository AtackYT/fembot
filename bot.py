import discord
from discord.ext import bridge
import random
from datetime import datetime

token = [redacted]

intents = discord.Intents()
intents = intents.all()

bot = bridge.Bot(command_prefix="fb ", intents=intents)

images = [1, 2, 3, 4, 5]

second = datetime.now()
seconds = second.strftime("%H:%M")
pingv = "@"
pingv2 = "@everyone"


@bot.event
async def on_ready():
    scount = len(bot.guilds)
    game = discord.Game(f"on gay {scount} servers!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    second = datetime.now()
    seconds = second.strftime("%H:%M")
    print('                 Bot is online at', seconds, '!')
    print('-------------------------------------------------------------')

@bot.bridge_command(name = 'ping', description = 'pings and returns a pong.')
async def ping(ctx):
    scount = len(bot.guilds)
    game = discord.Game(f"on gay {scount} servers!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    await ctx.respond(f"Pong! Latency is {bot.latency}")
    second = datetime.now()
    seconds = second.strftime("%H:%M")
    print('             The ping command was sent at', seconds, '!')
    print('-------------------------------------------------------------')

@bot.bridge_command(name = 'helpinghand', description = 'displays the help message.')
async def helpinghand(ctx):
    scount = len(bot.guilds)
    game = discord.Game(f"on gay {scount} servers!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    await ctx.respond(f"Guess some commands!")
    second = datetime.now()
    seconds = second.strftime("%H:%M")
    print('             The help command was sent at', seconds, '!')
    print('-------------------------------------------------------------')

@bot.bridge_command(name = 'cum', description = 'shhhh....')
async def cum(ctx):
    scount = len(bot.guilds)
    game = discord.Game(f"on gay {scount} servers!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    await ctx.respond(f"I just cummed!")
    second = datetime.now()
    seconds = second.strftime("%H:%M")
    print('               Someone just came at', seconds, '!')
    print('-------------------------------------------------------------')

@bot.bridge_command(name="cuddle", description="cuddles the mentioned person.")
async def cuddle(ctx, user):
    scount = len(bot.guilds)
    game = discord.Game(f"on gay {scount} servers!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    embed = discord.Embed(
        title=f"Cuddles: ",
        description=f"{user}",
        color=discord.Colour.embed_background(),
    )
    if (random.choice(images)) == 1:
        embed.set_image(url="https://media.tenor.com/s44ige0diLYAAAAC/sanriokill-anime.gif")
    elif (random.choice(images)) == 2:
        embed.set_image(url='https://media.tenor.com/nxjuBYA2thMAAAAC/love-animecute.gif')
    elif (random.choice(images)) == 3:
        embed.set_image(url="https://media.tenor.com/oSPZDjEf9vQAAAAC/anime-hug-anime-hugging.gif")
    elif (random.choice(images)) == 4:
        embed.set_image(url="https://media.tenor.com/kCZjTqCKiggAAAAC/hug.gif")
    elif (random.choice(images)) == 5:
        embed.set_image(url="https://media.tenor.com/jAycgzTbAWwAAAAC/cuddle.gif")
    if pingv in user:
        if pingv2 in user:
            await ctx.respond('You may not ping everyone!')
        else:
            await ctx.respond(embed=embed)
    else:
        await ctx.respond('Mention someone not say their name!')
    second = datetime.now()
    seconds = second.strftime("%H:%M")
    print('            The cuddle command was sent at', seconds, '!')
    print('-------------------------------------------------------------')

@bot.bridge_command(name="worship", description="worships the mentioned person.")
async def worship(ctx, user):
    scount = len(bot.guilds)
    game = discord.Game(f"on gay {scount} servers!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    embed = discord.Embed(
        title=f"Worshiping: ",
        description=f"{user}",
        color=discord.Colour.embed_background(),
    )
    embed.set_image(url="https://media.tenor.com/7ArSyn_B__gAAAAC/mafu-mafumafu.gif")
    if pingv in user:
        if pingv2 in user:
            await ctx.respond('You may not ping everyone!')
        else:
            await ctx.respond(embed=embed)
    else:
        await ctx.respond('Mention someone not say their name!')
    second = datetime.now()
    seconds = second.strftime("%H:%M")
    print('           The worship command was sent at', seconds, '!')
    print('-------------------------------------------------------------')

@bot.bridge_command(name="kiss", description="kisses the mentioned person.")
async def kiss(ctx, user):
    scount = len(bot.guilds)
    game = discord.Game(f"on gay {scount} servers!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    embed = discord.Embed(
        title=f"Kissing: ",
        description=f"{user}",
        color=discord.Colour.embed_background(),
    )
    if (random.choice(images)) == 1:
        embed.set_image(url="https://media.tenor.com/Ogthkl9rYBMAAAAC/ichigo-hiro.gif")
    elif (random.choice(images)) == 2:
        embed.set_image(url='https://media.tenor.com/dn_KuOESmUYAAAAC/engage-kiss-anime-kiss.gif')
    elif (random.choice(images)) == 3:
        embed.set_image(url="https://media.tenor.com/8JdJyDd1higAAAAC/kiss-cheek.gif")
    elif (random.choice(images)) == 4:
        embed.set_image(url="https://media.tenor.com/YHxJ9NvLYKsAAAAC/anime-kiss.gif")
    elif (random.choice(images)) == 5:
        embed.set_image(url="https://media.tenor.com/jnndDmOm5wMAAAAC/kiss.gif")
    if pingv in user:
        if pingv2 in user:
            await ctx.respond('You may not ping everyone!')
        else:
            await ctx.respond(embed=embed)
    else:
        await ctx.respond('Mention someone not say their name!')
    second = datetime.now()
    seconds = second.strftime("%H:%M")
    print('             The kiss command was sent at', seconds, '!')
    print('-------------------------------------------------------------')

@bot.bridge_command(name="creampie", description="Does the thing...")
async def creampie(ctx, user):
    scount = len(bot.guilds)
    game = discord.Game(f"on gay {scount} servers!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    embed = discord.Embed(
        title=f"Does the thing with: ",
        description=f"{user}",
        color=discord.Colour.embed_background(),
    )
    embed.set_image(url="https://media.tenor.com/bLkaae5j5BIAAAAS/horny-anime.gif")
    if pingv in user:
        if pingv2 in user:
            await ctx.respond('You may not ping everyone!')
        else:
            await ctx.respond(embed=embed)
    else:
        await ctx.respond('Mention someone not say their name!')
    second = datetime.now()
    seconds = second.strftime("%H:%M")
    print('             The fuck command was sent at', seconds, '!')
    print('-------------------------------------------------------------')

bot.run(token)