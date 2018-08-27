nome = 'Seja bem-vindo a calculadora'


print('{:=^60}'.format(nome))

print()

while True:

    print('-> + para somar\n-> - para subtrair\n-> x para multiplicar\n-> / para dividir\n-> d para divisão inteira\n-> % para resto da divisão\n-> p para potência\n-> q para Sair ')
    opcao = input('Escolha uma opção: ')
    
    if opcao == 'q' or opcao == 'Q':
        break

    if opcao == '+' or opcao == '-' or opcao == 'x' or opcao == '/' or opcao == 'd' or opcao == '%' or opcao == 'p':
        if opcao == '+':
            print('Você escolheu o cálculo de soma!')
            s = float(input('Digite um valor : '))
            s1 = float(input('Digite outro valor: '))
            print()
            print('O resultado da soma é: ', s + s1)
            print()        
                    
        
        elif opcao == '-':
            print('você escolheu o cálcuo para subtração!')
            sb = float(input('Digite um valor : '))
            sb1 = float(input('Digite outro valor: '))
            print()
            print('O restuldado da subtração é: ', sb - sb1)
            print()


        elif opcao == 'x': 
            print('Você escolheu o cálculo de multiplicação!')
            m = float(input('Digite um valor : '))
            m1 = float(input('Digite outro valor: '))
            print()
            print('O resultado multiplicação é: ', m * m1)
            print()


        elif opcao == '/':
            print('Você escolheu o cálculo de divisão!')
            d = float(input('Digite um valor : '))
            d1 = float(input('Digite outro valor: '))
            print()
            print('O resultado da divisão é: ', d / d1)
            print()


        elif opcao == 'D':
            print('Você escolheu o cálculo para a divisão inteira!')
            di = int(input('Digite um valor : '))
            di1 = int(input('Digite outro valor: '))
            print()
            print('O resultado da divisão inteira é: ', di // di1)
            print()


        elif opcao == '%':
            print('Você escolheu o cálculo de resto da divisão!')
            rd = int(input('Digite um valor: '))
            rd1 = int(input('Digite outro valor: '))
            print()
            print('O resto da divisão é: ', rd % rd1)
            print()

        elif opcao == 'p':
            print('Você escolheu o cálculo para potência!')
            p = int(input('Digite um valor: '))
            p1 = int(input('Digite outro valor: '))
            print()
            print('A potência é: ', p ** p1)
            print()

    else:
        print('opção invalida')
        n = input('deseja continuar? s/n!')
        if n == 's':
            continue
        elif n == 'n':
            break


         
print()
              
print('='*60)


