# main.py

import pagamento_fisio
import pagamento_geral
import receita_clinica
import resultado


def main():

    pagamento_fisio.obter_dados_fisio()

    pagamento_geral.obter_desp_geral()

    pagamento_geral.total()

    receita_clinica.obter_receita()

    receita_clinica.exibir_receita()

    resultado.exibir_resultado()


if __name__ == '__main__':
    main()
