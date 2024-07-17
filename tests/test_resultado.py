# tests/test_resultado.py

from humaniza import resultado


def test_calcula_resultado():
    # Teste para resultado positivo
    receita_total = 1000.0
    total_gasto = 600.0
    resultado_total, retirada, caixa = resultado.calcula_resultado(receita_total, total_gasto)
    assert resultado_total == 400.0
    assert retirada == 320.0
    assert caixa == 80.0

    # Teste para resultado zero
    receita_total = 1000.0
    total_gasto = 1000.0
    resultado_total, retirada, caixa = resultado.calcula_resultado(receita_total, total_gasto)
    assert resultado_total == 0.0
    assert retirada == 0.0
    assert caixa == 0.0

    # Teste para resultado negativo
    receita_total = 600.0
    total_gasto = 1000.0
    resultado_total, retirada, caixa = resultado.calcula_resultado(receita_total, total_gasto)
    assert resultado_total == -400.0
    assert retirada == 0.0
    assert caixa == 0.0
