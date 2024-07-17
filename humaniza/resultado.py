# resultado.py
from humaniza import pagamento_fisio, pagamento_geral, receita_clinica


def calcula_resultado(receita_total, total_gasto):
    resultado = receita_total - total_gasto
    if resultado < 0:
        retirada = 0
        caixa = 0
    else:
        retirada = 0.80 * resultado
        caixa = 0.20 * resultado
    return resultado, retirada, caixa


def exibir_resultado():

    total_receita = receita_clinica.calcular_receita_total()
    total_gastos = pagamento_fisio.total_pg_fisio() + pagamento_geral.calcular_total_despesas()
    # Calcular e exibir o resultado
    resultado_total, retirada, caixa = calcula_resultado(
        total_receita, total_gastos
    )
    print(f'Resultado total: R${resultado_total:.2f}')
    print()
    print(f'Valor de retirada (80%): R${retirada:.2f}')
    print()
    print(f'Valor deixado para o caixa (20%): R${caixa:.2f}')
