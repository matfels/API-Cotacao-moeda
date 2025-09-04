from modedas import get_cootacao
import graficos as gf
opcao = 1 

cotacoes = get_cootacao()
 
l_moedas =["USD - Dolar","EUR - Dolar","GBP - Libras"]
l_valores = [1 / cotacoes['USD'],1 / cotacoes['EUR'],1 / cotacoes['GBP']]

while opcao != 0:

    gf.menu()
    opcao = int(input('Escolha um tipo de gráfico: '))
    match opcao:
        case 1: gf.grafico_barra( l_moedas, l_valores)
        case 2: gf.grafico_pizza(l_moedas, l_valores)
        case 3: gf.grafico_dispersao(l_moedas, l_valores)
