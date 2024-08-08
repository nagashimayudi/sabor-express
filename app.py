import os

# Criação de Dicionários. Listas [] com chaveamento {} e dados distribuídos
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Ultra Burger', 'categoria': 'Lanche', 'ativo':True}]

def finalizar_app():
    exibir_subtitulo('Encerrando...')

# Para refatorar e reduzir repetição de código e faciltar mudanças futuras
def exibir_subtitulo(texto):
    # 'cls' para limpar terminal no Windows. 'clear' no MacOS e Linux.
    os.system('cls')
    # Cria uma linha de astericos de acordo com o tamanho do texto
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

# Fonte diferente do fSymbols
def exibir_nome_programa():
    print('Ⓢⓐⓑⓞⓡ Ⓔⓧⓟⓡⓔⓢⓢ\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    # Input para a população de um dicionário
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Os restaurantes cadastrados são:')
    # A função ljust() adiciona espaçamentos padronizados para justifica elementos/texto
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        # Edita os textos exibidos dependendo dos status com condicionais
        status = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}')
    voltar_ao_menu()

# Alterando o status do restaurante. Importante para validação de dados!
def alterar_status_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante o qual deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem) 
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida) -> Transformar um input
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            print('Encerrando...')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()