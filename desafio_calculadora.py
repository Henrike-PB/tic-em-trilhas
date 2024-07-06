def calculadora():
    while True:
        print('🅲🅰🅻🅲🆄🅻🅰🅳🅾🆁🅰 🆂🅸🅼🅿🅻🅴🆂')
        print()
        print('1. Soma')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('s. Sair\n')

        operacao = input("Selecione uma opção ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print('Obrigado por utilizar a Calculadora Simples!')
            break

        if operacao not in ['1', '2', '3', '4']:
            print('Opção inválida! Tente novamente.')
            continue

        numero_1 = float(input('Primeiro número: '))
        numero_2 = float(input('Segundo número: '))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print(f'O resultado da operação soma é: {resultado}\n')

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print(f'O resultado da operação subtração é: {resultado}\n')

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print(f'O resultado da operação multiplicação é: {resultado}\n')

        else:
            if numero_2 == 0:
                print('Divisões por zero não são possíveis. Tente novamente.\n')
                continue
            else:
                resultado = numero_1 / numero_2
                print(f'O resultado da operação divisão é: {resultado}\n')



calculadora()
