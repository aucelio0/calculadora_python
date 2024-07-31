# Loop 
while True:   
    # operações
    print(f'{'='*30} Operações {'='*30}\n')
    print('1 - SOMA')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')

    # seleção da operação
    opcao = input('\nEscolha qual operação: ')

    x = str(input('Informe um número: ')).replace(',', '.')
    y = str(input('Informe outro número: ')).replace(',', '.')
    
    # conversão
    x = float(x)
    y = float(y)

    match int(opcao):
        case 1:
            try:
                soma = x + y
                print(f'Resultado:{soma}')
            except:
                print('Não foi possível realizar cálculo.')
        case 2:
            try:
                subtracao = x - y
                print(f'Resultado:{subtracao}') 
            except:
                print('Não foi possível realizar cálculo.')  
        case 3: 
            try: 
                multiplicacao = x * y
                print(f'Resultado:{multiplicacao}') 
            except:
                print('Não foi possível realizar cálculo.')  
        case 4:
            try:
                divisao = x / y
                print(f'Resultado:{divisao}') 
            except:
                print('Não foi possível realizar cálculo.')  
        
 # continuar com algum cálculo
     
    continuar = input('Deseja continuar (s/n)').lower()

    if continuar == 's':
      continue
    else:
       break
       
   
        