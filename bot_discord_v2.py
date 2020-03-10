import os
from discord.ext import commands
from comandos import *

BOT_PREFIX = ("?", "!")
TOKEN = os.getenv("TOKEN_DISCORD")

client = commands.Bot(command_prefix=BOT_PREFIX)


@client.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!!!')


@client.command()
async def r(ctx, *, arg):
    msg = processa_r(arg)
    print(f'ctx: {ctx.message}')
    print(f'arg: {arg}')
    await ctx.send(f'{ctx.author.mention} {msg}')


@client.command()
async def c(ctx, *, arg):
    jogador_nome = ctx.author.name
    jogador_id = ctx.author.id
    chat_id = ctx.channel.id

    msg = criar_personagem(arg, jogador_id, jogador_nome, chat_id)

    await ctx.send(msg)


@client.command()
async def ps(ctx):
    msg = listar_personagens(ctx.channel.id)
    await ctx.send(msg)


client.run(TOKEN)
