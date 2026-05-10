import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina','categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa ():
    '''Exibe o nome estilizado do programa na tela'''
    print ('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def exibir_opcoes():
    '''Exibe as opções para o usuário'''
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print ('3. Alternar estado do restaurante')
    print ('4. Sair\n')

def finalizar_app():
    '''Exibe o subtitulo de finalizacao quando o programa e encerrado'''
    exibir_subtuitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Retorna ao menu de opcoes'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Exibe o recado opcao invalida quando o usuario insere um valor invalido e retorna ao menu de opcoes'''
    print ('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtuitulo(texto):
    '''Essa função é responsável por exibir o subtítulo
    Exibe o subtitulo e limpa o terminal
    '''
    linha = '*' * (len(texto))
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo
    restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtuitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados'''
    exibir_subtuitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print (f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Altera o estado atual do restaurante: de ativado para desativado e vice versa'''
    exibir_subtuitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restarante que deseja alterar o estado: ')
    restaurante_encontrado = False   
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado') 
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Estrutura de decisao que seleciona a opcao do menu de opcoes de acordo com o valor inserido pelo usuario'''
    try:
        opcao_escolhida = int(input ('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()           
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app ()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main ():
     '''Função principal que inicia o programa '''
     os.system ('cls')
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()

if __name__ == '__main__':
     main ()
