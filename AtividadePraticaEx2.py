print("Bem-vindo a pizzaria do Marlon Maverick Vasconcelos Machado")
print("-"*23 + "Cardápio" + "-"*22)
print("| Código | Descrição   | Pizza Média | Pizza Grande |")
print("|   21   | Napolitana  |   R$ 20,00 |     R$ 26,00  |")
print("|   22   | Marguerita  |   R$ 20,00 |     R$ 26,00  |")
print("|   23   | Calabresa   |   R$ 25,00 |     R$ 32,50  |")
print("|   24   | Toscana     |   R$ 30,00 |     R$ 39,00  |")
print("|   25   | Portuguesa  |   R$ 30,00 |     R$ 39,00  |")
print("-"*53)

# valor_total será usada posteriormente para somar o valor do(s) pedido(s)
valor_total = 0
#Criado um loop para que o cliente fique até decidir sair do menu de pedidos realizados
while True:
    # input pedem tamanho e codigo deseado para poderem procurar o formato válido nos if's e elif's abaixo
    tamanho = input("Qual tamanho de pizza você gostaria (M/G): ")
    codigo = int(input("Entre com o código do sabor desejado: "))
    # Ao achar o código e tamanho complementares ele adicionará o valor a váriavel valor
    if(tamanho == 'M' and codigo == 21):
        valor = 20.00
        print("Você pediu uma pizza Napolitana média.")
    elif(tamanho == 'G' and codigo == 21):
        valor = 26.00
        print("Você pediu uma pizza Napolitana grande.")
    elif(tamanho == 'M' and codigo == 22):
        valor = 20.00
        print("Você pediu uma pizza Marguerita média.")
    elif(tamanho == 'G' and codigo == 22):
        valor = 26.00
        print("Você pediu uma pizza Marguerita grande.")
    elif (tamanho == 'M' and codigo == 23):
        valor = 25.00
        print("Você pediu uma pizza Calabresa média.")
    elif (tamanho == 'G' and codigo == 23):
        valor = 32.50
        print("Você pediu uma pizza Calabresa grande.")
    elif (tamanho == 'M' and codigo == 24):
        valor = 30.00
        print("Você pediu uma pizza Toscana média.")
    elif (tamanho == 'G' and codigo == 24):
        valor = 39.00
        print("Você pediu uma pizza Toscana grande.")
    elif (tamanho == 'M' and codigo == 25):
        valor = 30.00
        print("Você pediu uma pizza Portuguesa média.")
    elif (tamanho == 'G' and codigo == 25):
        valor = 39.00
        print("Você pediu uma pizza Portuguesa grande.")
    else:
        # Usado para que se digitar um valor errado, apareça o print e redirecione de volta ao inicio do loop com continue
        print("Tamanho ou código inválido, digite novamente!")
        continue
    # Ao final do pedido aparecerá o menu para caso queira pedir mais ou não
    print("Você deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("2 - Não")
    sair = input("")
    if(sair == "2"):
        valor_total = valor + valor_total
        break
    else:
        # Caso queira pedir novamente o valor do primeiro pedido será somado a váriavel valor total.
        # E ficará repetindo o processo até que não se queira mais pedir.
        valor_total = valor + valor_total
        continue

print("Valor total a pagar: R${}".format(valor_total))
