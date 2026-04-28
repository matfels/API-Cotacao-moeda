=======
# Conversor de Moedas e Análise Gráfica

Este projeto é uma ferramenta multifuncional desenvolvida em Python para consultar taxas de câmbio e realizar conversões monetárias em tempo real. A aplicação consome dados de uma API externa e oferece três formas de interação: via consola, interface gráfica (GUI) e visualização de gráficos.

## 📋 Funcionalidades

O sistema divide-se em módulos que permitem:

* **Conversão de Moedas:** Calcula o valor de conversão entre moedas (Dólar, Euro, Libra) para o Real Brasileiro (BRL), utilizando taxas atualizadas.
* **Interface Gráfica (GUI):** Uma janela amigável onde o utilizador seleciona a moeda e visualiza a cotação.
* **Visualização de Dados:** Geração de gráficos (barras, pizza e dispersão) para comparar a valorização de diferentes moedas face ao Real.
* **Integração com API:** Conexão direta com a `exchangerate-api.com` para obter dados JSON.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Requests:** Para realizar as requisições HTTP à API de câmbio.
* **Tkinter:** Para a construção da interface gráfica do utilizador.
* **Matplotlib:** Para a criação e exibição dos gráficos estatísticos.

## 📂 Estrutura do Projeto

```text
├── modedas.py        # Módulo central (backend) que consome a API e realiza os cálculos
├── interface.py      # Aplicação Desktop (GUI) usando Tkinter
├── conversao.py      # Aplicação de Linha de Comandos (CLI) com menu interativo
├── graficos.py       # Funções para gerar gráficos (Barra, Pizza, Dispersão) usando Matplotlib
└── index_grafico.py  # Script principal para executar a visualização dos gráficos
>>>>>>> 59e27e0bce82297eb2c4a241e547d6c914835a98
