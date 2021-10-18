#Python3
print('-'*50)
print('''[ 1 ] Tabuada
[ 2 ] Hipotenusa
[ 3 ] Multiplicação, Adição, Subtração
[ 4 ] Potencia
[ 5 ] Conversor de base numerica
[ 6 ] Sair''')
print('-'*50)
opção = int(input('Digite um numero: '))
print('~'*50)
if opção == 1:
    n = int(input('Digite um numero '))
    for c in range(0,11):
        print(f'{n} X {c} = {n*c}')
if opção == 2:
    ca = float(input('Digite um numero '))
    co = float(input('Digite um numero '))
    hi = (co ** 2 + ca ** 2) **(1/2)
    print(f'A hipotenusa vai medir {hi}')
if opção == 3:
    op2 = str(input(('Selecione uma letra[M/A/S] '))).upper()
    if op2 == 'M':
        n1 = float(input('Digite um numero, para multiplicação '))
        n2 = float(input('Digite um numero, para multiplicação '))
        m = n1 * n2
        print(f'{n1} X {n2} = {m}')
    if op2 == 'A':
        a1 = float(input('Digite um numero para adição '))
        a2 = float(input('Digite um numero para adição '))
        ad = a1 + a2
        print(f'{a1} + {a2} = {ad}')
    if op2 == 'S':
        s1 = float(input('Digite um numero para subtração '))
        s2 = float(input('Digite um numero para subtração '))
        sub = s1 - s2
        print(f'{s1} - {s2} = {sub}')
if opção == 4:
    e1 = int(input('Digite um numero para elevar : '))
    e2= int(input('Digite um numero a potencia : '))
    p = e1 ** e2
    print(f'{e1} ** {e2} = {p}')
if opção == 5:
    num = int(input('Digite um numero para conventer '))
    print('''
    [ 1 ] = converter para binario
    [ 2 ] = converter para octal
    [ 3 ] = converter para hexadecimal''')
    opção2 = int(input('sua opção '))
    if opção2 == 1:
        print(f'binario {bin(num)[2:]}')
    elif opção2 == 2:
        print(f'octal {oct(num)[2:]}')
    elif opção2 == 3:
        print(f'hexadecimal {hex(num)[2:]}')
print('=-'*50)
print('Até mais...')
