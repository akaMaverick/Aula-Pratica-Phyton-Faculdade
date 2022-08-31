lista_produtos = []

def cadastrar_produto(codigo):
    print("O código do produto a ser cadastrado é: {}".format(codigo))
    # colocado as váriaveis para guardar os valores
    nome = input("Qual o nome do produto? ").upper()
    # adicioando upper para que os valores sejam sempre em letras maiúsculas
    fabricante = input("Qual o nome do fabricante? ").upper()
    # Realizado um loop para que sempre que não for digitado um número na váriavel valor, a pergunta se repetir
    while True:
        try:
            valor = float(input("Qual o valor do produto? "))
            if valor > 0:
                break
        except ValueError:
            print("Isto não é um número, digite o valor do produto novamente.")
            continue
    # Criado um dicionário e feito a cópia para dentro da lista
    cadastro = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor}
    lista_produtos.append(cadastro.copy())


def consultar_produto():
    # Criado o loop para fazer as perguntas de consulta de cadastro
    while True:
      try:
        print("Bem-vindo ao consultar produtos: ")
        opcao_consultar = int(input("Entre com a opção desejada:\n "
                                "1 - Consultar todos os produtos\n"
                                "2 - Consultar produtos por código\n"
                                "3 - Consultar produtos por fabricante\n"
                                "4 - Retornar\n"
                                ">>"))
        print("-" * 40)
        # O If é usado para verificar o que foi colocado no input do consultar
        if opcao_consultar == 1:
            print("Bem-vindo ao estoque dos produtos!")
            print("Confira abaixo o que está cadastrado no sistema: ")
            # Os loops dentro do if são usados para percorrer a lista de produtos que foi colocado no dicionário
            for produto in lista_produtos:
                print("-" * 40)
                for key, value in produto.items():
                    print("{} : {}".format(key, value))

        elif opcao_consultar == 2:
            print("Bem-vindo ao estoque dos produtos!")
            entrada = int(input("Digite o código do produto desejado: "))
            print("Confira abaixo o que está cadastrado no sistema pelo código informado: ")
            for produto in lista_produtos:
                print("-" * 40)
                # Colocado o print com o traço para poder ser mais legível
                if produto['codigo'] == entrada:
                    for key, value in produto.items():
                        print("{} : {}".format(key, value))
        elif opcao_consultar == 3:
            print("Bem-vindo ao estoque dos produtos!")
            entrada = input("Digite o fabricante desejado: ").upper()
            """ colocado o upper neste input para que mesmo que seja escrito com minusculas 
            e maiusculas juntas sempre ficará maiusculo no input."""
            print("Confira abaixo os itens cadastrado no sistema por fabricante informado: ")
            for produto in lista_produtos:
                print("-" * 40)
                if produto['fabricante'] == entrada:
                    for key, value in produto.items():
                        print("{} : {}".format(key, value))
        elif opcao_consultar == 4:
            break

      except ValueError:
        # colocado o try juntamente com o except para caso a pessoa digitar algo que não é um número
        print("Valor colocado não é aceito")


def remover():
    print("Bem-vindo ao remover cadastros de produto(s): ")
    entrada = int(input("Digite o código do produto que deseja remover: "))
    # Usado um input para pegar o código do produto e remove-lo
    for produto in lista_produtos:
        if produto['codigo'] == entrada:
            lista_produtos.remove(produto)


codigo_produto = 0
# Usado um loop para o Menu principal
while True:
    try:
        print("Bem-vindo ao controle de estoque da mercearia do Marlon Maverick Vasconcelos Machado")
        print("Escolha a opção desejada: ")
        print("1 - Cadastrar Produto")
        print("2 - Consultar Produto(s)")
        print("3 - Remover Produto")
        print("4 - Sair")
        numero = int(input(": "))
        # Com a resposta a váriavel número, ele começa a tentar entrar nos if do número inserido
        if numero == 1:
        # E dentro dos if’s acessará as funções predefinidas
            codigo_produto = codigo_produto + 1
            cadastrar_produto(codigo_produto)
        elif numero == 2:
            consultar_produto()
        elif numero == 3:
            remover()
        elif numero == 4:
            break
        else:
            # Caso não for um número dentro da lista do menu,
            # aparecerá a mensagem abaixo e dará continue para digitar novamente
            print("Número digitado não está nas opções disponiveis. Tente novamente!")
            continue
    except ValueError:
        #Caso não for um número inteiro ou um número em si, entrará no except.
        print("O número digitado não é válido. Tente novamente.")
