print("Bem-vindo a pizzaria do Marlon Maverick Vasconcelos Machado")
print("-"*23 + "Cardápio" + "-"*22)
print("| Código | Descrição   | Pizza Média | Pizza Grande |")
print("|   21   | Napolitana  |   R$ 20,00 |     R$ 26,00  |")
print("|   22   | Marguerita  |   R$ 20,00 |     R$ 26,00  |")
print("|   23   | Calabresa   |   R$ 25,00 |     R$ 32,50  |")
print("|   24   | Toscana     |   R$ 30,00 |     R$ 39,00  |")
print("|   25   | Portuguesa  |   R$ 30,00 |     R$ 39,00  |")
print("-"*53)

valor_total = 0
while True:
    tamanho = input("Qual tamanho de pizza você gostaria (M/G): ")
    codigo = int(input("Entre com o código do sabor desejado: "))
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
        print("Tamanho ou código inválido, digite novamente!")
        continue
    print("Você deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("2 - Não")
    sair = input("")
    if(sair == "2"):
        valor_total = valor + valor_total
        break
    else:
        valor_total = valor + valor_total
        continue

print("Valor total a pagar: R${}".format(valor_total))
