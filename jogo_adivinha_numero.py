#Jogo adivinha número de 1 a 10
from random import randint
from time import sleep
continuar = True
while continuar:
    computador = randint(1, 10)
    usuario = int(input("Estou pensando em um número, tente advinhar: "))
    while True: #teste de acerto
        if computador == usuario:
            print("Você acertou....Parabéns!!!")
            break
        elif computador > usuario:
            usuario = int(input("Muito baixo...tente um número maior: "))
        elif computador < usuario:
            usuario = int(input("Muito alto...tente um número menor: "))
    continuar = input("Deseja continuar jogando? [s/n] ")
    if continuar == "s":
        continuar = True
    elif continuar == "n":
        continuar = False
sleep(1)
print("Fim do Jogo...")