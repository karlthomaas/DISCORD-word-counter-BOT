import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)
TOKEN = ""

file = open("words.txt", "a")
file.close()


@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send('pong')



word = "juut"
@client.event
async def on_message(msg):
    if word in msg.content.lower():
        file = open("words.txt", "a")
        file.write(word + "\n")
        file.close()
    await client.process_commands(msg)

word_counter = []
@client.command()
async def words(ctx):
    await ctx.send('Counting...')
    file = open("words.txt", "r")
    print('a')
    for sona in file:
        word_counter.append(sona)
    times = len(word_counter)
    await ctx.send(f"The word '{word}' has been said {times} times.")
    word_counter.clear()
    file.close()



client.run(TOKEN)
