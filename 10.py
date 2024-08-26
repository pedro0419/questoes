n1 = '1'
while n1 != '0':
    print('''
        -------calc.py-------
        escolha uma operação
        1 - soma
        2 - subtração
        3 - multiplicação
        4 - divisão
        5 - elevar ao quadrdo
        0 - sair
        ---------------------
        ''')
    x = input('escolha a operação: ')
    if x < '0' or x > '5':
        print("operação invalida , tente novamente!") 
        continue
    elif x == '1':
        n1 = int(input("digite o numero 1: "))
        n2 = int(input("digite o numero 2: "))
        print(f'O resultado de {n1} + {n2} é {n1+n2}')
    else:
        if x == '2':
            n1 = int(input("digite o numero 1: "))
            n2 = int(input('digite o numero 2:'))
            print(f'O resultado de {n1} - {n2} é {(n1-n2)}')
        if x == '3':
            n1 = int(input("digite o numero 1: "))
            n2 = int(input('digite o numero 2:'))
            print(f'O resultado de {n1} * {n2} é {(n1*n2)}')
        if x == '4':
            n1 = int(input("digite o numero 1: "))
            n2 = int(input('digite o numero 2:'))
            print(f'O resultado de {n1} / {n2} é {(n1/n2)}')
        if x == '5':
            n1 =int(input("digite o numero:"))
            print(f'O resultado de {n1} elevado a 2 = {n1**2}')
        if x == '0':
            print('você saiu')
            break