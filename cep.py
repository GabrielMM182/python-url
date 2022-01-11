endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"


import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos podendo ser entre eles de 0 ate 9 os digitos 5x e 3x e podendo ser opcional o - por isso o ?

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)