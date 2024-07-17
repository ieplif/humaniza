# pagamento_fisio.py

fisioterapeutas = []


def obter_dados_fisio():

    num_fisioterapeutas = int(input('Digite o número de fisioterapeutas: '))

    for _ in range(num_fisioterapeutas):
        fisioterapeuta = str(input('Digite o nome da fisioterapeuta: '))
        num_dias = int(
            input(f'Digite a quantidade de dias para {fisioterapeuta}: ')
        )
        horas_por_dia = [0] * num_dias

        for i in range(num_dias):
            horas = float(
                input(
                    f'Digite a quantidade de horas para o dia {i + 1} de {fisioterapeuta}: '
                )
            )
            horas_por_dia[i] = horas

        pagamento_total = calcular_pagamento_total(
            horas_por_dia, num_dias
        )
        fisioterapeutas.append({
            'nome': fisioterapeuta,
            'pagamento_total': pagamento_total,
        })

    # Exibir pagamento total para cada fisioterapeuta e somar ao total geral

    total_pagamentos_fisioterapeutas = 0.0
    for fisioterapeuta in fisioterapeutas:
        print(
            f"O pagamento total para {fisioterapeuta['nome']} é: R${fisioterapeuta['pagamento_total']:.2f}"
        )
        total_pagamentos_fisioterapeutas += fisioterapeuta['pagamento_total']


def total_pg_fisio():
    total_pagamentos_fisioterapeutas = 0.0
    for fisioterapeuta in fisioterapeutas:
        total_pagamentos_fisioterapeutas += fisioterapeuta['pagamento_total']
    return total_pagamentos_fisioterapeutas


def calcular_somatorio(horas_por_dia):
    # Constante multiplicadora
    valor_hora = 26.00

    # Calcula o somatório da lista de horas
    somatorio_horas = sum(horas_por_dia)

    # Multiplica o somatório pela constante
    pgto_horas = somatorio_horas * valor_hora

    return pgto_horas


def obter_valor_aulas_experimentais():
    # Pergunta se houve aulas experimentais
    houve_aulas_experimentais = (
        input('Houve aulas experimentais? (sim/não): ').strip().lower()
    )

    total_valor_aulas_experimentais = 0.0

    if houve_aulas_experimentais == 'sim':
        # Pergunta a quantidade de aulas experimentais
        quantidade_aulas_experimentais = int(
            input('Quantas aulas experimentais houve? ')
        )

        # Pergunta os valores respectivos de cada aula experimental
        for i in range(quantidade_aulas_experimentais):
            valor_aula = float(
                input(f'Digite o valor da aula experimental {i + 1}: ')
            )
            total_valor_aulas_experimentais += 0.40 * valor_aula
        print(total_valor_aulas_experimentais)
    else:
        print('Nenhuma aula experimental a ser considerada.')

    return total_valor_aulas_experimentais


def obter_ajuda_de_custo(num_dias):
    # Pergunta o valor da ajuda de custo por dia
    valor_ajuda_custo = float(
        input('Digite o valor da ajuda de custo por dia: ')
    )
    # Calcula a ajuda de custo total
    ajuda_custo_total = num_dias * valor_ajuda_custo
    print(f'{ajuda_custo_total:.2f}')
    return ajuda_custo_total


def calcular_pagamento_total(horas_por_dia, num_dias):
    # Calcula o somatório das horas multiplicado pela constante
    valor_horas = calcular_somatorio(horas_por_dia)

    # Obtém o valor total das aulas experimentais
    valor_aulas_experimentais = obter_valor_aulas_experimentais()

    # Obtém o valor total da ajuda de custo
    ajuda_custo_total = obter_ajuda_de_custo(num_dias)

    # Calcula o pagamento total
    pagamento_total = (
        valor_horas + valor_aulas_experimentais + ajuda_custo_total
    )

    return pagamento_total
