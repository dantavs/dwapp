from config import iniciar_banco
from models import Personagem

SQL_PJ_NOME_INSERE_UPDATE = "INSERT INTO personagens (chat_id, jogador_id, nome) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE nome= VALUES(nome)"
SQL_PJ_NOME_SELECT = 'SELECT nome from personagens where chat_id = %s and jogador_id = %s'
SQL_PERSONAGENS_SELECT = 'SELECT chat_id, jogador_id, nome from personagens where chat_id = %s and jogador_id > %s'


class PersonagemDao:
    def __init__(self):
        db = iniciar_banco()['db']
        self.__db = db

    def definir_nome(self, pj):
        cursor = self.__db.cursor()
        print(f'pj: {pj.nome}')
        print(f'pj: {pj.jogador_id}')
        print(f'pj: {pj.chat_id}')

        cursor.execute(SQL_PJ_NOME_INSERE_UPDATE, (pj.chat_id, pj.jogador_id, pj.nome))

        self.__db.commit()

    def consultar_nome(self, chat_id, jogador_id):
        cursor = self.__db.cursor()

        cursor.execute(SQL_PJ_NOME_SELECT, (chat_id, jogador_id))

    def listar_personagens(self, chat_id):
        cursor = self.__db.cursor()
        jogador_id = '1'

        print(f'chatid: {chat_id}')
        cursor.execute(SQL_PERSONAGENS_SELECT, (chat_id, jogador_id))

        personagens = traduz_personagens(cursor.fetchall())

        print(f'nomes: {personagens}')
        return personagens


def traduz_personagens(personagens):
    def cria_personagem_com_tupla(tupla):
        return Personagem(tupla[0], tupla[1], tupla[2])

    return list(map(cria_personagem_com_tupla, personagens))
