import pprint

usuario = input("Digite seu nome: ")
mostrador = f"""           Seja bem-vindo, {usuario}!

[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair
"""



extrato = {}
i = 1
a = 1
d = 0

while True:
    print("\n" + mostrador + "\n")
    valor = int(input("Selecione uma opção: "))
    if valor == 1:
        deposito = float(input("Digite o valor do depósito: "))
        if deposito <= 0:
            print("Impossível efetuar o depósito")
        else:
            extrato[f"depósito {i} R$"] = deposito  # Corrigido para armazenar 'deposito' corretamente
            i += 1
            print("Depósito realizado com sucesso.")


    elif valor == 2:
        saque = float(input("Digite o valor de saque: "))
        if saque <= 0:
            print("não foi possível realizar o saque, tente novamente.")

        elif sum(extrato.values()) < saque :
            print("saldo inferior ao valor do saque")

        elif saque > 500.00:
            print("Só é permitido saques de até 500.00")  
        
        elif d == 3:
            print("Você atingiu o limite de saques no dia")

        else:
            extrato[f"saque {a} R$"] = -saque
            a += 1
            d += 1
            print("Saque realizado com sucesso!")

        

    elif valor == 3:
        print("\n"+"===================================="+"\n")
        for chave, valor in extrato.items():
            print(f"{chave}: {valor}")

        print(f'SALDO R$: {sum(extrato.values())}')
        print("\n"+"===================================="+"\n")


    elif valor == 4:
        break

    else:
        print("Selecione um opção válida!!!")