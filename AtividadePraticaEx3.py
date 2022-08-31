def volume_feijoada():
    print("Menu Volume Feijoada")
    # Enquanto não for digitado um valor válido o loop continuará.
    while True:
        # colocado o try para verificar se um número foi digitado(verifique linha 15)
        try:
            volume = int(input("Entre com a quantidade desejada(ml): "))
            # caso seja um número ativará o if para verificar se a ml está dentro dos valores válidos
            if volume >= 300 and volume <= 5000:
                total = volume * 0.08
                return total
            else:
                print("Não aceitamos porções menores que 300 ou maiores que 5000ml!")
        except ValueError:
            # caso não seja digitado um número exibirá o print abaixo
            print("Isto não é um número, digite novamente!")


def opcao_feijoada():
    # Colocado while novamente para que até a pessoa digite um valor válido, a pergunta se repita.
    while True:
        print("Menu Opção Feijoada")
        print("Entre com a opção da feijoada: ")
        print("b - Básica(Feijão + paiol + costelinha)")
        print("p - Premium(Feijão + paiol + costelinha + partes de porco)")
        print("s - Supreme(Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)")
        opcao = input("")
        if opcao == 'b':
            multiplicador = 1.00
            return multiplicador
        elif opcao == 'p':
            multiplicador = 1.25
            return multiplicador
        elif opcao == 's':
            multiplicador = 1.50
            return multiplicador
        else:
            print("Opção inválida. Tente novamente!")
            continue


def acompanhamento_feijoada():
    # valor colocado fora do "loop" para que ele não volte a 0 quando o "loop" estiver funcionando
    valor = 0
    while True:
        print("Deseja mais algum acompanhamento? ")
        print("0 - Não desejo mais nenhum acompanhamento.(encerrar pedido)")
        print("1 - 200g de arroz")
        print("2 - 150g de farofa especial")
        print("3 - 100g de couve cozida")
        print("4 - 1 laranja descascada")
        resposta = int(input(" "))
        # ELe só dara break para fora do loop caso a opção 0 for digitada
        if resposta == 0:
            valor = valor + 0.00
            break
        elif resposta == 1:
            valor = valor + 5.00
        elif resposta == 2:
            valor = valor + 6.00
        elif resposta == 3:
            valor = valor + 7.00
        elif resposta == 4:
            valor = valor + 3.00
        else:
            print("Opção inválida.")
    # quando a opção 0 for digitada retornará o valor da soma dos acompanhamentos digitados
    return valor


print("Bem-vindo ao programa de feijoada do Marlon Maverick Vasconcelos Machado!")
# Nesta parte estou passando o return de cada função chamada para uma váriavel para calcular o valor total
volume_final = volume_feijoada()
opcao_escolhida = opcao_feijoada()
acompanhamentos = acompanhamento_feijoada()

total_valor = (volume_final * opcao_escolhida) + acompanhamentos

print("O valor a ser pago é (R$): {}. (volume = {} * opção = {} + acompanhamento(s) = {})".format(total_valor, volume_final,
                                                                                                  opcao_escolhida,
                                                                                                  acompanhamentos))
