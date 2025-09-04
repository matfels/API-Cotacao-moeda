import matplotlib.pyplot as plt
import langgraph
import langchain
def grafico_barra(l_moedas,l_valores):
    plt.bar(l_moedas,l_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel("Moedas")
    plt.ylabel("BRL (R$)")
    plt.show()

def grafico_pizza(l_moedas,l_valores):
    plt.pie(l_valores, labels = l_moedas)
    plt.title('Proporção em relação ao BRL - Real Brasileiro')
    plt.show()



def grafico_dispersao(l_moedas,l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel("Moedas")
    plt.ylabel("BRL (R$)")
    plt.show()

def menu():
    print()
    print('1 - Gráfico de Barras')
    print('2 - Gráfico de pizza')
    print('3 - Gráfico de Dispersão')
    print('0 - Para sair')
    print()

