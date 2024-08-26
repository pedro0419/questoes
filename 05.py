nome = input("digite seu nome: ")
diciplina = input("digite sua disciplina: ")
nota = float(input("digite sua nota: "))
if nota < 0 or nota > 10:
    print("nota invalida")
else:
    if nota >= 5.5 and nota <= 6:
        nota = 6
    if nota >= 6:
        print(f'o aluno {nome} está aprovado na diciplina de {diciplina} com a nota {nota} ')
    else :
        print(f'o aluno {nome} está reprovado na diciplina de {diciplina} coma nota {nota}')
 