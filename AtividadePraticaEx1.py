print("Bem-vindo a loja de Marlon Maverick Vasconcelos Machado")
valor_produto = float(input("Entre com o valor do produto: "))
quantidade_produto = int(input("Entre com a quantidade do produto: "))
#Nesta parte o if verificará se a pessoa digitou um número 0 em um ou ambos dos casos.
if (valor_produto != 0) and (quantidade_produto != 0):
    #Caso passe pela verificação, entrará só no if ou elif de acordo com a quantidade do produto.
    if(quantidade_produto < 5):
        soma = valor_produto * quantidade_produto
        desconto = (soma * 0) / 100
    elif(quantidade_produto > 4 and quantidade_produto < 20):
        soma = valor_produto * quantidade_produto
        desconto = (soma * 3) / 100
    elif(quantidade_produto > 19 and quantidade_produto < 100):
        soma = valor_produto * quantidade_produto
        desconto = (soma * 6) / 100
    elif(quantidade_produto > 99):
        soma = valor_produto * quantidade_produto
        desconto = (soma * 10) / 100
else:
    #Está linha de else é caso a verificação do primeiro if seja 0 em um ou ambos dos casos.
    print("Algum dos dados está errado!")
#E está última linha de if é para caso esteja tudo correto, ele acessará e imprimirá no console o valor sem e com desconto.
if(valor_produto and quantidade_produto):
    print("O valor sem desconto do produto é: R$ {}".format(soma))
    print("O valor com desconto do produto é: R$ {}".format(soma - desconto))
