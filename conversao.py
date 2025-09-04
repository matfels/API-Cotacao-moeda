from modedas import converter_cotacao


def menu():
    print()
    print("1 - Converter Dólar em Real")
    print("2 - Converter Euro em Real")
    print("3 - Converter Libras em Real")
    print("4 - Converter em outra opção")
    print("0 - sair")
    print()
    

opcao = 1 
while opcao != 0:
    menu()
    opcao = int(input("Ecolha uma das opções a cima: "))

    destino = 'BRL'
    valor = int(input("Digite o valor: "))

    match opcao:
        case 1: origem = 'USD'    
        case 2: origem = 'EUR'    
        case 3: origem = 'GBP'    
        case 4: 
            origem = input("Digite a Origem: ")    
            destino = input("Digite o Destino: ")    

    if opcao:
        print()
        print("***********************")
        print(f"{origem} para {destino}: ", converter_cotacao(origem,destino, valor))
        print("***********************")
        print()
