# receita_clinica.py
from collections import defaultdict
from datetime import datetime


class Receita:
    def __init__(self, data, nome_paciente, atividade, valor):
        self.data = data
        self.nome_paciente = nome_paciente
        self.atividade = atividade
        self.valor = valor


receitas = []


def obter_receita():
    # Funções relacionadas a receita da clínica
    while True:
        add_receita = (
            input('Deseja adicionar uma receita? (sim/não): ').strip().lower()
        )
        if add_receita == 'sim':
            adicionar_receita()
        else:
            break

    # Listar receitas
    listar_receitas()


def adicionar_receita():
    data = input('Digite a data da receita (formato DD/MM/YYYY): ')
    nome_paciente = input('Digite o nome do paciente: ')
    atividade = input('Digite a atividade realizada: ')
    valor = float(input('Digite o valor da receita: '))

    receita = Receita(data, nome_paciente, atividade, valor)
    receitas.append(receita)


def listar_receitas():
    for receita in receitas:
        print(
            f'Atividade: {receita.atividade}, Data: {receita.data}, Valor: R${receita.valor:.2f}'
        )


def calcular_total_receitas_por_mes():
    despesas_por_mes = defaultdict(float)
    for receita in receitas:
        mes = datetime.strptime(receita.data, '%d/%m/%Y').strftime('%m-%Y')
        despesas_por_mes[mes] += receita.valor

    return despesas_por_mes


def calcular_receita_total():
    return sum(receita.valor for receita in receitas)


def exibir_receita():
    # Calcular o total de receitas por mês
    receitas_por_mes = calcular_total_receitas_por_mes()
    print('Total de receitas por mês:')
    for mes, total in receitas_por_mes.items():
        print(f'{mes}: R${total:.2f}')

    # Calcular o total da receita
    total_receita = calcular_receita_total()
    print(f'Total de Receitas: R${total_receita:.2f}')
