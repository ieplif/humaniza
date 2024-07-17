# pagamento_geral.py
from collections import defaultdict
from datetime import datetime

from humaniza import pagamento_fisio


class Despesa:
    def __init__(self, descricao, data, valor):
        self.descricao = descricao
        self.data = data
        self.valor = valor


despesas = []


def obter_desp_geral():
    # Adicionar despesas
    while True:
        add_despesa = (
            input('Deseja adicionar uma despesa? (sim/não): ').strip().lower()
        )
        if add_despesa == 'sim':
            adicionar_despesa()
        else:
            break

    # Listar despesas
    listar_despesas()


def adicionar_despesa():
    descricao = input('Digite a descrição da despesa: ')
    data = input('Digite a data da despesa (formato DD/MM/YYYY): ')
    valor = float(input('Digite o valor da despesa: '))
    despesas.append(Despesa(descricao, data, valor))


def listar_despesas():
    for despesa in despesas:
        print(
            f'Descrição: {despesa.descricao}, Data: {despesa.data}, Valor: R${despesa.valor:.2f}'
        )


def calcular_total_despesas():
    return sum(despesa.valor for despesa in despesas)


def calcular_total_despesas_por_mes():
    despesas_por_mes = defaultdict(float)
    for despesa in despesas:
        mes = datetime.strptime(despesa.data, '%d/%m/%Y').strftime('%m-%Y')
        despesas_por_mes[mes] += despesa.valor

    return despesas_por_mes


def total():
     # Calcular o total de despesas
    total_despesas = calcular_total_despesas()
    print(f'Total de despesas gerais: R${total_despesas:.2f}')
    print()

    # Calcular o total de despesas por mês
    despesas_por_mes = calcular_total_despesas_por_mes()
    print('Total de despesas gerais por mês:')
    for mes, total in despesas_por_mes.items():
        print(f'{mes}: R${total:.2f}')

    total_pg_fisioterapeutas = pagamento_fisio.total_pg_fisio()
    print(
        f'Total de pagamentos para todas as fisioterapeutas: R${total_pg_fisioterapeutas:.2f}'
    )

    # Calcular o total de gastos
    total_gastos = total_pg_fisioterapeutas + total_despesas

    print(f'Total de DESPESASs: R${total_gastos:.2f}')
