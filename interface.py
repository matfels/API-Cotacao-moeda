from tkinter import *
from modedas import converter_cotacao

def execucao():
    texto = converter_cotacao()
    texto_cotacoes["text"] = texto

def obter():
    text_imput = imp.get() #OBTEM O TEXTO DO USUARIO
    moeda= 'BRL'

    if text_imput == '1':
        o_origem = 'USD'
        moeda = 'BRL'
    elif text_imput == '2':
        o_origem = 'EUR'
        moeda = 'BRL'
    elif text_imput == '3':  
        o_origem = 'GBP'
        moeda = 'BRL'    

    print((text_imput))
    print(moeda)
    
    valor_cotacao = converter_cotacao(origem = o_origem, destino=  moeda ) #RETORNA A COTACAO DA MOEDA COM O TEXTO DO USUÁRIO
    texto_cotacoes["text"] = valor_cotacao

janela = Tk()

janela.title("Cotação Atual Manelas")

#Primeiro texto
texto_orientacao = Label(janela, text = """Selecione a opção e clique no botão para calcular a cotação:
                         1 - Converter Dólar em Real
                         2 - Converter Euro em Real
                         3 - Converter Libras em Real
                         4 - Converter em outra opção
                         """ )
texto_orientacao.grid(column = 0,row = 0)




#Botão segunda linha
botao = Button(janela, text = "Buscar Cotação", command = obter)
botao.grid(column = 0,row = 1 )

#Texto resultado do botão
texto_cotacoes = Label(janela, text = '')
texto_cotacoes.grid(column = 0,row = 2)


#imput
imp = Entry(janela, width= 10)
imp.grid(column= 0, row= 3)


#Finalizando a janela
janela.mainloop()

