from rolador_codigo import *
from models import Personagem
from dao import PersonagemDao


def hello(update, context):
    print(f'Update : {update}')
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def processa_r(comando):
    resposta = ""
    msg = ""

    argumentos = remover_comando(comando)

    if argumentos == "":
        resposta = "Você precisa passar argumentos para o /r (ex.: /r 2d6)"
    else:
        resultado = rolar_dados(argumentos)
        if resultado['err']:
            msg = resultado['msg']
        else:
            resposta = resultado['total']
            msg = resultado['msg']

    return f'Resultado: {resposta}. {msg}'


def remover_comando(text):
    text = text.split()
    text = " ".join(text[1:])
    print(f'text: {text}')

    return text


def criar_personagem(comando, jogador_id, jogador_nome, chat_id):
    personagem_dao = PersonagemDao()

    personagem_nome = remover_comando(comando)

    pj = Personagem(chat_id, jogador_id, personagem_nome)

    personagem_dao.definir_nome(pj)

    return f'{jogador_nome} agora é: {pj.nome}'


def listar_personagens(chat_id):
    personagem_dao = PersonagemDao()

    personagens = personagem_dao.listar_personagens(chat_id)

    msg = []
    for pj in personagens:
        msg.append(f'Personagem: {pj.nome} - Jogador: {pj.jogador_id}')

    print(f'msg: {msg}')
    return msg
