from comandos import *


def hello_telegram(update, context):
    print(f'Update : {update}')
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def r_telegram(update, context):
    msg = processa_r(update.message.text)
    update.message.reply_text(msg)


def criar_personagem_telegram(update, context):
    jogador_nome = format(update.message.from_user.first_name)
    jogador_id = update.message.from_user.id
    chat_id = update.message.chat.id

    msg = criar_personagem(update.message.text, jogador_id, jogador_nome, chat_id)

    update.message.reply_text(msg)


def listar_personagens_telegram(update, context):
    msg = listar_personagens(update.message.chat.id)
    update.message.reply_text(msg)
