nome_valido = False
salario_valido = False
porcentagem_valida = False


while not nome_valido:
    try:
        nome = input("Digite o Nome: ")
        validacao = bool(nome.replace(" ", "").isalpha() == True)
        if validacao is True:
            nome_valido = True
        else:
            print("Digite um nome  valido que contenha só letras")
    except:
        print("o Nome não é valido")
        break
while not salario_valido:
    try: 
        salario = int(input("Digite o Salário: "))
        salario_valido = True
    except ValueError:
        print("O salario não é um salario válido")
while not porcentagem_valida:  
    try:
        porcentagem = int(input("Qual a porcentagem do bonus: "))
        porcentagem_valida = True
    except ValueError:
        print("A porcentagem não é válida")
    
    bonus = salario * porcentagem / 100


    print(f"O bonus de {nome} será R${bonus}")
