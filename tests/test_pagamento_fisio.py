# tests/test_pagamento_fisio.py

from pytest import MonkeyPatch

from humaniza import pagamento_fisio


def test_calcular_somatorio():
    assert pagamento_fisio.calcular_somatorio([1, 2, 3]) == 6 * 26


def test_obter_valor_aulas_experimentais(monkeypatch: MonkeyPatch):
    inputs = iter(['sim', '2', '100', '150'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pagamento_fisio.obter_valor_aulas_experimentais() == 0.40 * (
        100 + 150
    )


def test_obter_ajuda_de_custo(monkeypatch: MonkeyPatch):
    monkeypatch.setattr('builtins.input', lambda _: '50')
    assert pagamento_fisio.obter_ajuda_de_custo(10) == 500
