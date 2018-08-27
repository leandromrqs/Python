nome = 'Seja bem-vindo a calculadora'

print('{:=^60}'.format(nome))

print()

while True:

    print('-> 1 para somar\n-> 2 para subtrair\n-> 3 para multiplicar\n-> 4 para dividir\n-> 5 para divisão inteira\n-> 6 para resto da divisão\n-> 7 para potência\n-> 0 para Sair ')
    opcao = input('Escolha uma opção: ')
    if opcao.isdigit() == True:
        opcao  = int(opcao)
        
        if opcao >= 0 and opcao <= 7:
            if opcao == 0:
                break
        
            if opcao == 1:
                print('Você escolheu o cálculo de soma!')
                s = float(input('Digite um valor : '))
                s1 = float(input('Digite outro valor: '))
                print()
                print('O resultado da soma é: ', s + s1)
                print()        
                        
            
            elif opcao == 2:
                print('você escolheu o cálcuo para subtração!')
                sb = float(input('Digite um valor : '))
                sb1 = float(input('Digite outro valor: '))
                print()
                print('O restuldado da subtração é: ', sb - sb1)
                print()


            elif opcao == 3: 
                print('Você escolheu o cálculo de multiplicação!')
                m = float(input('Digite um valor : '))
                m1 = float(input('Digite outro valor: '))
                print()
                print('O resultado multiplicação é: ', m * m1)
                print()


            elif opcao == 4:
                print('Você escolheu o cálculo de divisão!')
                d = float(input('Digite um valor : '))
                d1 = float(input('Digite outro valor: '))
                print()
                print('O resultado da divisão é: ', d / d1)
                print()


            elif opcao == 5:
                print('Você escolheu o cálculo para a divisão inteira!')
                di = int(input('Digite um valor : '))
                di1 = int(input('Digite outro valor: '))
                print()
                print('O resultado da divisão inteira é: ', di // di1)
                print()


            elif opcao == 6:
                print('Você escolheu o cálculo de resto da divisão!')
                rd = int(input('Digite um valor: '))
                rd1 = int(input('Digite outro valor: '))
                print()
                print('O resto da divisão é: ', rd % rd1)
                print()

            elif opcao == 7:
                print('Você escolheu o cálculo para potência!')
                p = int(input('Digite um valor: '))
                p1 = int(input('Digite outro valor: '))
                print()
                print('A potência é: ', p ** p1)
                print()
        else:
            print('opção invalida')

    else:
        print('opção invalida')
        n = input('deseja continuar? s/n!')
        if n == 's':
            continue
        elif n == 'n':
            break


         
print()
              
print('='*60)

