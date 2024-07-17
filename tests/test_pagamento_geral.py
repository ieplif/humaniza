# tests/test_pagamento_geral.py

from humaniza import pagamento_geral
from humaniza.pagamento_geral import Despesa


def test_calcular_total_despesas():
    pagamento_geral.despesas = [
        Despesa('Despesa 1', '01/05/2023', 100.0),
        Despesa('Despesa 2', '02/05/2023', 200.0),
    ]
    assert pagamento_geral.calcular_total_despesas() == 300.0


def test_calcular_total_despesas_por_mes():
    pagamento_geral.despesas = [
        Despesa('Despesa 1', '01/05/2023', 100.0),
        Despesa('Despesa 2', '02/05/2023', 200.0),
        Despesa('Despesa 3', '01/06/2023', 150.0),
    ]
    despesas_por_mes = pagamento_geral.calcular_total_despesas_por_mes()
    assert despesas_por_mes['05-2023'] == 300.0
    assert despesas_por_mes['06-2023'] == 150.0
