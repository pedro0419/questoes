nome = input('digite seu nome:')
idade = int(input('digite sua idade: '))
if idade >= 16:
    print(f'olá {nome} , você está apto a votar')
else:
    print(f'olá {nome} , você não está apto a votar')