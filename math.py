print('''
[0] = Contas Básicas
[1] = Bhaskara
[2] = Fatorial
[3] = Sequencia de Fibonaci
''')
escolha = int(input('Escolha uma: '))
print('''
#----------------------------------------------------#
                    Contas Básicas                  
#----------------------------------------------------#
''')
if escolha == 0:
    ssmdp = input('+\n-\nX\n/\n²\n') 
    if ssmdp == '+':
        num0 = input('>>> ') 
        num1 = input('>>> ') 
        soma = num0 + num1 
        print(soma) 
    elif ssmdp == '-':
        num0 = input('>>> ') 
        num1 = input('>>> ') 
        subtracao = num0 - num1
        print(subtracao) 
    elif ssdmp == 'X':
        num0 = input('>>> ') 
        num1 = input('>>> ') 
        mult = num0 * num1
        print(mult) 
    elif ssdmp == '²':
        num0 = input('>>> ') 
        num1 = input('>>> ') 
        potenci = num0 ** num1 
        print(potenci) 
print('''
#----------------------------------------------------# 
                    Bhaskara                        
#----------------------------------------------------#
''')
if escolha == 1:
    print('ax²+bx+c=0') 
    a = int(input('O valor de A: ')) 
    b = int(input('O valor de B: ')) 
    c = int(input('O valor de C: '))
    delta = b**2 -4*a*c
    divisor = 2*a 
    raizQuadradaDoDelta = delta ** (1/2) 
    x1 = (-b - raizQuadradaDoDelta) / divisor
    x2 = (-b + raizQuadradaDoDelta) / divisor
    print(x1,x2) 
print('''
#--------------------------------------------------#
                    Fatorial                      
#--------------------------------------------------#
''')
if escolha == 2:
    m = int(input('Digite um numero: ')) 
    c = m 
    f = 1 
    while c > 0:
        print(f'{c}',end='') 
        print(' X ' if c > 1 else ' = ',end=' ') 
        f = f*c 
        c -= 1 
    print(f'{f}')
print('''
#---------------------------------------------------#
               Sequencia de Fibonaci                     
#---------------------------------------------------#
''')
if escolha == 3:
    numero = int(input('>>> '))
    num0,num1 = 0,1
    print(num0,num1) 
    cont = 3 
    while cont <= numero:
        num2 = num0 + num1 
        print(num2,end=' ')
        num0 = num1 
        num1 = num2 
        cont += 1 
    print('-'*30,end=' ')
