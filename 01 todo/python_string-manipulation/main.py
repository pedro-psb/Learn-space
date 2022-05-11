url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

if '?' in url:
    interrogacao = url.find('?')
    url_base = url[:interrogacao]
    url_param = url[interrogacao + 1:]

print(url_base)
print(url_param)

# TODO buscar parametro: usar len para obter valor de parametros específico
# TODO multiplos paramentros: usar find('', ini) e find('&')
# TODO criar objeto extrator_url
# TODO expressão regular para cep
# TODO implementar validador_url no extrator_url
# TODO implementar métodos especiais __len__, __str__ e __eq__

'''
Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio
    '''


