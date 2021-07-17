opcao = int(input('Escolha entre a opção "add" digite 1, "mul" digite 2 e "in" digite 3: '))
if opcao == 1:
    a = str(input('Digite uma palavra: '))
    b = str(input('Digite outra palavra: '))
    c = a+b
    print('O valor de "{}" add "{}" é "{}".'.format(a, b, c))
elif opcao == 2:
    a = str(input('Digite uma palavra: '))
    n = int(input('Digite um número: '))
    c = n*(a)
    print('O valor de "{}" mul "{}" é "{}".'.format(a, str(n), c))
elif opcao == 3:
    a = str(input('Digite uma palavra: '))
    b = str(input('Digite outra palavra: '))
    c = a in b
    print('O valor de "{}" in "{}" é {}.'.format(a, b, c))
