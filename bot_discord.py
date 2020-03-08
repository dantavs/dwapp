import discord
from comandos import *


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        print(f'Discord message: {message}')
        print(f'Discord message content: {message.content}')
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        elif message.content.startswith('!r'):
            msg = processa_r(message.content)
            await message.channel.send(msg)
        elif message.content.startswith('!c'):
            jogador_nome = message.author.name
            jogador_id = message.author.id
            chat_id = message.channel.id

            msg = criar_personagem(message.content, jogador_id, jogador_nome, chat_id)

            await message.channel.send(msg)
        elif message.content.startswith('!ps'):
            msg = listar_personagens(message.channel.id)
            await message.channel.send(msg)


client = MyClient()
client.run('MzU0NDU4NTY1NjgwODI0MzMw.XmBkrQ.iHv1HitRs3oTC7jfIWMSkpwNOl4')