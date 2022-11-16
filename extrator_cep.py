endereco = "Rua das Flores, apartamento 1002, Laranjeiras, Rio de Janeira, RJ, 23440120"

import re

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") # Retorna um padrão em um texto, string.
busca = padrao.search(endereco) # Retorna o MATCH, aquela combinação do padrão, ele retorna o Valor ou None

if busca :
    cep = busca.group() # Ele trás o MATCH da combinação, ou seja ele trás a STRING em si.
    print(cep)
