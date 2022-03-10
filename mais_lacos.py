'''
4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar
laços for para fazer exibições a fim de economizar espaço. Escolha uma versão
de foods.py e escreva dois laços for para exibir cada lista de comidas.
'''

my_foods = ['pizza', 'falafel', 'carrot cake']

for food in my_foods:
    print(food)

print("-="*15)

for food in range(len(my_foods)):
    print(my_foods[food])
