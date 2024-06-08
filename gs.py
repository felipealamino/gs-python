def coleta_dados_usuario():
    print('Bem-vindo ao OceanPreserve')

    nome = input('Digite seu nome: ')
    print(f'Bem-vindo {nome} ao nosso sistema de preservação dos oceanos')

    ano_nascimento = input('Digite seu ano de nascimento: ')
    while not (ano_nascimento.isnumeric() and len(ano_nascimento) == 4):
        print('ERRO: O ano deve ser um inteiro de 4 dígitos')
        ano_nascimento = input('Digite seu ano de nascimento: ')

    return nome, int(ano_nascimento)


def seleciona_acoes():
    total_acoes = 0

    lista_acoes = [
        'Reduzir o uso de plástico',
        'Participar de limpezas de praia',
        'Apoiar organizações ambientais',
        'Educar outras pessoas sobre a importância dos oceanos',
        'Reduzir a pegada de carbono'
    ]

    acoes = {
        'Reduzir o uso de plástico': 0,
        'Participar de limpezas de praia': 0,
        'Apoiar organizações ambientais': 0,
        'Educar outras pessoas sobre a importância dos oceanos': 0,
        'Reduzir a pegada de carbono': 0
    }

    opcoes_acoes = {
        '1': 'Reduzir o uso de plástico',
        '2': 'Participar de limpezas de praia',
        '3': 'Apoiar organizações ambientais',
        '4': 'Educar outras pessoas sobre a importância dos oceanos',
        '5': 'Reduzir a pegada de carbono'
    }

    texto_menu = 'Digite o número referente à ação que deseja realizar:\n' + \
                 '\n'.join([f'{i} - {acao}' for i, acao in opcoes_acoes.items()]) + '\n> '

    while True:
        print(f'\nTotal de Ações Escolhidas: {total_acoes}')
        opcao = input(texto_menu)

        while opcao not in opcoes_acoes:
            print('[ERRO] Selecione uma das opções presentes no menu')
            opcao = input(texto_menu)

        acao_selecionada = opcoes_acoes[opcao]
        acoes[acao_selecionada] += 1
        total_acoes += 1

        resposta_finalizar = input(
            'Você deseja encerrar a seleção de ações ou escolher mais ações (encerrar/continuar)?\n> ')
        while resposta_finalizar not in ['encerrar', 'continuar']:
            print('[ERRO] Forneça uma resposta cadastrada')
            resposta_finalizar = input(
                'Você deseja encerrar a seleção de ações ou escolher mais ações (encerrar/continuar)?\n> ')
        if resposta_finalizar == 'encerrar':
            print('A seleção será finalizada')
            break

    return total_acoes, acoes


def imprime_resumo_acoes(total_acoes, acoes):
    print('Obrigado por contribuir para a preservação dos oceanos!')
    print(f'Total de ações selecionadas: {total_acoes}\n'
          f'Ações escolhidas:')
    for acao, quantidade in acoes.items():
        print(f' - {acao}: {quantidade} vezes')


nome, ano_nascimento = coleta_dados_usuario()
total_acoes, acoes = seleciona_acoes()
imprime_resumo_acoes(total_acoes, acoes)
