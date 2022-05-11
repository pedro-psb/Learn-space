# Desafio

## Conversão de moedas - dolar/real

Agora que conseguimos extrair valores da nossa URL como moeda de origem, moeda de destino e quantidade de moeda, proponho a você o desafio de realizar essa conversão.

Modifique o nosso projeto, levando em conta o valor do dólar em real (por exemplo: DOLAR = 5.50), para, sabendo o valor do dólar em real (por exemplo: DOLAR = 5.50), ler da URL os 3 parâmetros (origem, destino e quantidade) e imprimir na tela o valor da conversão.

Observação: pode assumir que a moeda de origem e destino será sempre “real” ou “dolar”, ou seja, só faremos a conversão de dólar para real e vice-versa.

Vou deixar algumas linhas de código de exemplo para você começar.

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

<script>
VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")
</script>