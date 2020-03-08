import random


class Dado:
    def __init__(self, lados):
        self.lados = lados

    def rolar(self):
        return random.randrange(1, self.lados + 1)


class CestaDados:
    def __init__(self, dados):
        self.dados = dados

    def rolar(self):
        # ROLAGEM DE DADOS
        resultados_dados = []
        subtotal = 0
        dados = self.dados

        for dado in dados:
            resultado = dado.rolar()
            subtotal += resultado
            resultados_dados.append(resultado)

        return resultados_dados, subtotal

class Personagem:
    def __init__(self, chat_id, jogador_id, personagem_nome):
        self.chat_id = chat_id
        self.jogador_id = jogador_id
        self.nome = personagem_nome
