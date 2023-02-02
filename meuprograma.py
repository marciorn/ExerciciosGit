#Módulo 1 - Exercício 2: Escreva um programa que exiba o resultado de 5a x 3b onde a = 2 e b = 5.
while True:
    try:
        a = float(input('Digite o valor de a: '))
        b = float(input('Digite o valor de b: '))
        operação = (5 * a) * (3 * b)
        print(f'O resultado da equação 5a x 3b é igual a {operação:.3f}.')
        break
    except ValueError:
        print("Deu ruim vacilão!!! Digite apenas números.  Tente novamente.")
