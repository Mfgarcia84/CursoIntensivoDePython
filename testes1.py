#Jogo advinhação de número de 1 a 5
from random import randint
from time import sleep
continuar = True
while continuar:
    computador = randint(1, 5)
    usuario = int(input("Estou pensando em um número, tente advinhar: "))
    if computador == usuario:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    continuar = input("Deseja continuar jogando? [s/n] ")
    if continuar == "s":
        continuar = True
    elif continuar == "n":
        continuar = False
sleep(1)
print("-="*15)
print("Fim do programa")
print("-="*15)