'''
4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida,
use min() e max() para garantir que sua lista realmente começa em um e termina em um
 milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é capaz
 de somar um milhão de números.
'''

numeros = [numero for numero in range(1, 1000001)]
print(min(numeros)) #validar se a lista começa mesmo em 1
print(max(numeros)) #validar se a lista termina mesmo em 1000000
print(sum(numeros))
