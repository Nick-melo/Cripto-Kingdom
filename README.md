# Cripto Kingdom

Cripto Kingdom é um projeto que utiliza a API da Binance para obter dados de preços de criptomoedas em tempo real e gera gráficos simulados. O objetivo do projeto é fornecer uma visualização clara das flutuações de preços de criptomoedas específicas e enviar como um report.

## Funcionalidades

- Obtenção de dados em tempo real: Coleta dados de preços de criptomoedas em tempo real da Binance.
- Simulação de gráficos: Plota gráficos simulados (pode ser configurado para utilizar os dados reais de uma API propria da Binance).
- Conversão de valores: Preços das criptomoedas convertidos para Real (R$) utilizando a API de conversão de moeda.
- Personalização: Possibilidade de selecionar diferentes criptomoedas para análise.
- Relatório PDF: Gera um relatório com os gráficos e dados de preços em formato PDF.
- Envio por e-mail: Possibilidade de enviar o relatório PDF gerado por e-mail.



## Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Você também precisará instalar as bibliotecas necessárias.

### Instalação das Dependências

Use o gerenciador de pacotes `pip` para instalar as bibliotecas necessárias:
- bibliotecas utilizadas no arquivo import.py

## API Utilizada:
- Binance API: Utilizada para obter os preços atualizados das criptomoedas.
- Exchangerate API: Utilizada para converter os valores das criptomoedas de USD para BRL (Real).

Esse projeto pode ser expandido para incluir mais criptomoedas ou ajustar a formatação e estilo dos relatórios gerados, permitindo uma personalização maior conforme a necessidade.
