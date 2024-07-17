# tests/test_receita_clinica.py

from humaniza import receita_clinica
from humaniza.receita_clinica import Receita


def test_calcular_receita_total():
    receita_clinica.receitas = [
        Receita('01/05/2023', 'Paciente 1', 'Atividade 1', 100.0),
        Receita('02/05/2023', 'Paciente 2', 'Atividade 2', 200.0),
    ]
    assert receita_clinica.calcular_receita_total() == 300.0


def test_calcular_total_receitas_por_mes():
    receita_clinica.receitas = [
        Receita('01/05/2023', 'Paciente 1', 'Atividade 1', 100.0),
        Receita('01/06/2023', 'Paciente 2', 'Atividade 1', 200.0),
        Receita('01/06/2023', 'Paciente 3', 'Atividade 1', 150.0),
    ]
    receitas_por_mes = receita_clinica.calcular_total_receitas_por_mes()
    assert receitas_por_mes['05-2023'] == 100.0
    assert receitas_por_mes['06-2023'] == 350.0
