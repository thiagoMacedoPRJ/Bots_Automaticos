import re
# 'r'   -> Usado somente para ler algo
# 'w'  -> Usado somente para escrever algo
# 'r+' -> Usado para ler e escrever algo
# 'a'  -> Usado para acrescentar algo

# Exemplo para acrescentar.
"""
with open('coco.txt', 'a') as arquivo:
      for valor in arquivo:
         arquivo.write(str(padrao))
"""

# Exemplo para escrever.
"""
with open('coco.txt', 'w') as arquivo:
     for valor in arquivo:
         arquivo.write(str(padrao) + '\n') -----------> '\n' serve para para ir em uma nova linha abaixo
"""
# Exemplo para escrever.
"""
with open('visao.txt', 'r') as arquivo:
     for valor in arquivo:
           print(valor + '\n') -----------> '\n' serve para para ir criando uma nova linha abaixo
"""

# Exemplo para escrever.
"""
with open('coco.txt', 'r+') as arquivo:
     for valor in arquivo:
          print(padrao)
     arquivo.write('Teste de exemplo')
"""

a = input('Qual palavra você quer encontrar: ')

with open('visao.txt', 'r') as arquivo:
     for valor in arquivo:
         x = '\\b{a} \\b'
         if re.search(x, valor, re.IGNORECASE):
             print("A string tem o nome Thiago")
         else:
            print("A string não tem o nome thiago")
