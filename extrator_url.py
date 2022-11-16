url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

url ="           "


# Sanatização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")


# Realizar o Fatiamento da URL

# Separa base e os parâmetros
indice_interrogacao = url.find("?")
url_base = url[0:indice_interrogacao] # começa do indice 0 e vai até o "?"
url_parametros = url[indice_interrogacao+1:] # começa a partir do "?" e vai até o final da URL
print(url_parametros) # printa o moedaDestino

# Busca o valor de um parâmetro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca) # Encontra o moedaOrigem
indice_valor = indice_parametro + len(parametro_busca) + 1 # Começa a partir "?" e vai até o moedaOrigem + 1 que é o =
indice_e_comercial =  url_parametros.find("&", indice_valor) #Encontra primeiro o "&" a partir do indice_valor que é o moedaOrigem +, o .find quando não encontra VALOR ele retorna -1"""

if indice_e_comercial == -1: # Se não encontrar "&" depois do real volta False
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

