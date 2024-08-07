import os

def finalizar_app():
    os.system('clear')
    print('Encerrando...\n')

def exibir_nome_programa():
    print('Ⓢⓐⓑⓞⓡ Ⓔⓧⓟⓡⓔⓢⓢ\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    #opcao_escolhida = int(opcao_escolhida)
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()