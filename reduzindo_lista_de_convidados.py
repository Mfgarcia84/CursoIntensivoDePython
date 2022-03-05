#3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua
# nova mesa de jantar não chegará a tempo para o jantar e tem espaço para
# somente dois convidados.
#• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
# mostre uma mensagem informando que você pode convidar apenas duas pessoas
# para o jantar.
#• Utilize pop() para remover os convidados de sua lista, um de cada vez,
# até que apenas dois nomes permaneçam em sua lista. Sempre que remover
# um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que
# ela saiba que você sente muito por não poder convidá-la para o jantar.
#• Apresente uma mensagem para cada uma das duas pessoas que continuam na
# lista, permitindo que elas saibam que ainda estão convidadas.
#• Utilize del para remover os dois últimos nomes de sua lista, de modo
# que você tenha uma lista vazia. Mostre sua lista para garantir que você
# realmente tem uma lista vazia no final de seu programa.

pessoas = ['marcela', 'malena', 'bárbara', 'andressa', 'fernanda', 'glaucia']
print(pessoas)
r1 = pessoas.pop()
print("Sinto muito " + r1.title() + " mas teremos que remarcar nosso jantar.")
print("Sinto muito " + pessoas.pop().title() + " mas teremos que remarcar nosso jantar.")
r3 = pessoas.pop()
print("Sinto muito " + r3.title() + " mas teremos que remarcar nosso jantar.")
print("Sinto muito " + pessoas.pop().title() + " mas teremos que remarcar nosso jantar.")
print(pessoas)
del pessoas[0]
del pessoas[0]
print(pessoas)

#outra maneira com laço for:
for index in range(5,1,-1):
    nomeRetirado = pessoas.pop(index)
    print(f"Sinto muito {nomeRetirado.title()}, mas teremos que remarcar nosso jantar.")
print(pessoas)