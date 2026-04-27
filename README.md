# API de cotação de moedas em tempo real

# O objetivo desse código e trazer uma cotação de moedas em tempo real e gráficos representando.

# ---------------------------- Arquivo --------------------------- 
# MOEDAS
# Este é o arquivo que realizar a API. Dentro do metodo "get_cootacao" busca site que disponibiliza as informações em JSON, realiza uma verificação se foi possivel realizar a conexão e roda o resto do código.
# Metodo "converter_cotacao" recebe os parâmetros para buscar a moéda que será cotada, ele ja está setado como padão (origem = 'USD', destino = 'BRL', valor = 1), será cotado o dolar com o real, em comparação a 1 real.

# CONVERSÃO
# Este arquivo contem o backend do menu da interface para o usuário.

# GRAFICOS
# Contem a programação para a criação de gráficos de comparação de moedas, apresenta 3 tipos de gráficos (Barra, Pizza, Dispersão).

# index_grafico 
# Contem um menu para a seleção de gráfico.

# interface
# Contem a interface gráfica para o usuário poder realizar a conversão da moeda.