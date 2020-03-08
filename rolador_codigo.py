from models import Dado, CestaDados


def rolar_dados2(lados, qtd):
    dado = Dado(lados)
    dados = []

    for i in range(qtd):
        dados.append(dado)
    cesta = CestaDados(dados)

    resultado = cesta.rolar()
    dados = resultado[0]
    total = resultado[1]

    # print('')
    # print(f'Resultado: {total} - Dados: {dados}')

    return total


def verifica_dado(palavra):
    for i in range(len(palavra)):
        if palavra[i] == 'd':
            if palavra[:i].isdigit():
                qtd = int(palavra[:i])
                if palavra[i + 1:].isdigit():
                    lados = int(palavra[i + 1:])
                    return True, lados, qtd
                else:
                    # print('num lado nok')
                    break
            else:
                # print('qtd nok')
                break
    return False, 0, 0


def verifica_operador(palavra):
    if palavra == '+' or palavra == '-':
        return True
    return False


def verifica_bonus(palavra):
    if palavra.isdigit():
        return True
    return False


def verifica_comandos_agregados(palavra):
    posicoes = []
    comandos_agregados = False

    for i in range(1, len(palavra)):
        # print(f'i: {i}')
        # print(f'carac: {palavra[i]}')
        if verifica_operador(palavra[i]) and i > 0:
            # print('comandos agregados')
            posicoes.append(i)
            comandos_agregados = True

    return {'comandos_agregados': comandos_agregados, 'posicoes_operadores': posicoes}


def separa_comandos(palavra):
    z = 0
    subcomandos = []
    comandos_agregados = False
    err = False

    comandos = verifica_comandos_agregados(palavra)
    # print(comandos)

    if comandos['comandos_agregados']:
        comandos_agregados = True
        for i in comandos['posicoes_operadores']:
            subpalavra = verifica_tipo_valor(palavra[z:i])
            if subpalavra['err']:
                return {'err': subpalavra['err'], 'comandos_agregados': comandos_agregados, 'subcomandos': subcomandos}
            sub = {'tipo_valor': subpalavra['tipo_valor'], 'valor': palavra[z:i], 'resultado': subpalavra['resultado']}
            subcomandos.append(sub)
            sub = {'tipo_valor': 'operador', 'valor': palavra[i:i + 1]}
            subcomandos.append(sub)
            tipo_valor = subpalavra['tipo_valor']
            # print (f'número: {palavra[z:i]} | tipo: {tipo_valor}')
            z = i + 1

        subpalavra = verifica_tipo_valor(palavra[z:])
        # print(f'subpalabra: {subpalavra}')
        if subpalavra['err']:
            # print(f'subpalabra: {subpalavra}')
            return {'err': subpalavra['err'], 'comandos_agregados': comandos_agregados, 'subcomandos': subcomandos}
        # print(f'subpalabra: {subpalavra}')
        sub = {'tipo_valor': subpalavra['tipo_valor'], 'valor': palavra[z:], 'resultado': subpalavra['resultado']}
        subcomandos.append(sub)
        tipo_valor = subpalavra['tipo_valor']
        # print(f'número: {palavra[z:]} | tipo: {tipo_valor}')
        # if sub['tipo_valor'] == 'operador':
        # print('erro último sub operador')

    return {'err': err, 'comandos_agregados': comandos_agregados, 'subcomandos': subcomandos}


def verifica_tipo_valor(palavra):
    tipo_valor = ''
    resultado = 0
    err = False

    dado = verifica_dado(palavra)
    if dado[0]:
        resultado = rolar_dados2(dado[1], dado[2])
        tipo_valor = 'dado'
    elif verifica_operador(palavra):
        tipo_valor = 'operador'
    elif verifica_bonus(palavra):
        tipo_valor = 'bonus'
        resultado = int(palavra)
    else:
        err = True

    return {'err': err, 'tipo_valor': tipo_valor, 'resultado': resultado}


def rolar_dados(comando_digitado):
    comandos = []
    palavras = comando_digitado.split()
    err = False
    msg = '( '

    for palavra in palavras:
        subcomando = separa_comandos(palavra)
        # print(f'Subcomandos: {subcomando}')
        if subcomando['comandos_agregados'] and not subcomando['err']:
            lista_subcomandos = subcomando['subcomandos']
            for sub in lista_subcomandos:
                comandos.append(sub)
            # print(f'comandos2-agregados: {comandos}')
        else:
            subcomando = verifica_tipo_valor(palavra)
            comando = {'tipo_valor': subcomando['tipo_valor'], 'valor': palavra, 'resultado': subcomando['resultado']}
            comandos.append(comando)
        if subcomando['err']:
            # print('Erro')
            msg = f'Valor inválido: {palavra}'
            err = True
            return {'total': 0, 'err': err, 'msg': msg}

    i = 0
    total = 0
    oper = False

    for comando in comandos:
        # print(f'comando: {comando}')
        if comando['tipo_valor'] == 'operador':
            oper = True
            valor1 = comandos[i - 1]['resultado'] if total == 0 else total
            valor2 = comandos[i + 1]['resultado']
            op = comandos[i]['valor']
            total = calcula_operacao(valor1, valor2, op)

            msg += comandos[i]['valor']
            msg += " "
        elif comando['tipo_valor'] == 'dado':
            msg += comandos[i]['valor']
            msg += "= "
            msg += str(comandos[i]['resultado'])
            msg += " "
        else:
            msg += "Bonus: "
            msg += comandos[i]['valor']
            msg += " "
        i += 1

    msg += ")"

    if not oper and not err:
        total = comandos[0]['resultado']

    return {'total': total, 'msg': msg, 'err': err}


def calcula_operacao(valor1, valor2, op):
    if op == '+':
        resultado = valor1 + valor2
    else:
        resultado = valor1 - valor2

    return resultado
