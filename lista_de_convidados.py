#3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto,
# para o jantar, quem você convidaria? Crie uma lista que inclua pelo
# menos três pessoas que você gostaria de convidar para jantar.
# Em seguida, utilize sua lista para exibir uma mensagem para cada pessoa,
# convidando-a para jantar.


pessoas = ["malena", "andressa", "fernanda"]

print("Oi " + pessoas[0].title() + ", vamos sair para jantar hoje?")
print(f"Oi {pessoas[1].title()}, vamos sair para jantar hoje?")
print("Oi " + pessoas[-1].title() + ", vamos sair para jantar hoje?")

#outra maneira
for nome in pessoas:
    print(f"Oi {nome.title()}, vamos sair para jantar hoje?")
