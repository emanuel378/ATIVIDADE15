# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
num1 = float(input("Digite seu primeiro numero:"))
num2 = float(input("Digite seu primeiro numero:"))
opera =input("Digite a operação ex :soma,multiplicação.subtração e divisão:")

#operaçoes
if opera =="soma":
    print(num1 + num2)
elif opera =="multiplicação":
    print(num1 * num2)
elif opera == "subtração":
    print(num1 - num2)
elif opera == "divisão":
    print(num1/num2)