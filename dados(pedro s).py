from random import randint  # Importa a funcao de gerar numeros aleatorios

print("hamburger")
print("jogo do dado")

dado1 = randint(1, 6)   # numero aleatorio entre 1 e 6
dado2 = randint(1, 6)   # numero aleatorio entre 1 e 6
print("Dado 1=", dado1 + dado2)

dado3 = randint(1, 6)   # numero aleatorio entre 1 e 6
dado4 = randint(1, 6)   # numero aleatorio entre 1 e 6
print("Dado 3=", dado3 + dado4)

P1 = dado1+dado2

P2 = dado3+dado4

if P1 > P2:
    print("P1 win")
elif P2 > P1:
    print("P2 win")
else:
    print("draw")
