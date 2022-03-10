'''
3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma lista.
Por exemplo, você poderia criar uma lista de montanhas, rios, países, cidades, idiomas
 ou qualquer outro item que quiser. Escreva um programa que crie uma lista contendo esses
 itens e então utilize cada função apresentada neste capítulo pelo menos uma vez.
'''

lista = ["laptop", "futebol", "cerveja",
         "big brother", "redes", "python",
         "linux", "malena", "inglês"]
print(lista)
print(lista[-2])
lista.append("academia")
print(lista)
lista[-2] = "espanhol"
print(lista)
lista.insert(-2, "fernanda")
print(lista)
del lista[3]
print(lista)
a = lista.pop()
print(lista)
print(a)
b = lista.pop(0)
print(lista)
print(b)
lista.remove("espanhol")
print(lista)
lista.sort()
print(lista)
print(sorted(lista))
print(sorted(lista, reverse=True))
print(lista)
lista.reverse()
print(lista)
