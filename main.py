while True:
    try:
        nome = input("Digite o Nome: ")
        validacao = bool(nome.replace(" ", "").isalpha() == True)
    except:
        print("o Nome não é valido")
        break

    try: 
        salario = int(input("Digite o Salário: "))
    except ValueError:
        print("O salario não é um salario válido")
        break
    
    try:
        porcentagem = int(input("Qual a porcentagem do bonus: "))
    except ValueError:
        print("A porcentagem não é válida")
        break
    bonus = salario * porcentagem / 100


    print(f"O bonus de {nome} será R${bonus}")
