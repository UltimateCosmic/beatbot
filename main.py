import discord
import os
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('No Errors')

@client.event
async def on_member_join(member):
    channel = client.get_channel(676597482519789598)
    await channel.send('Bienvenido')

@client.command(name='del')
async def delete_message(ctx, amount=2, adm=False):
    if adm == False:
        if amount <= 15:
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send('Cantidad maxima de 15')
    elif adm == True:
        await ctx.channel.purge(limit=amount)

@client.command(name='join')
async def join(ctx):
    if ctx.author.voice:
        channels = ctx.message.author.voice.channel
        voice = await channels.connect()
        source = FFmpegPCMAudio('Noche.mp3')
        player = voice.play(source)
    else:
        await ctx.send('Nao Nao voce no esta en una canal de voz')

@client.command(name='leave')
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Chau')
    else:
        await ctx.send('No puedo salir de un canal si no estoy en un canal salame')


client.run(os.getenv('BEAT_TOKEN'))