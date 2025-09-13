

nome = input("Digite o Nome: ")

salario = int(input("Digite o Salário: "))

porcentagem = int(input("Qual a porcentagem do bonus: "))

bonus = salario * porcentagem / 100

print("O bonus de " + nome + " será R$" + str(bonus))
