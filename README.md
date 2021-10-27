#Python3

print('-'*50)
print('''[ T ] Tabuada
[ H ] Hipotenusa
[ MAS ] Multiplicação, Adição, Subtração
[ P ] Potencia
[ B ] Conversor para binario
[ He ] Conversor para hexadecimal
[ O ] conversor para octadecimal''')
print('-'*50)
opção = str(input(' '))
print('~'*50)
if opção == 'T':
    n = int(input(' '))
    for c in range(0,11):
        print(f'{n} X {c} = {n*c}')
if opção == 'H':
    ca = float(input(' '))
    co = float(input(' '))
    hi = (co ** 2 + ca ** 2) **(1/2)
    print(f'{hi}')
if opção == 'MAS':
    op2 = str(input(('''Selecione uma letra[M/A/S]
    M = Multiplucação
    A = Adição
    S = subtração
    '''))).upper()
    if op2 == 'M':
        n1 = float(input(' '))
        n2 = float(input(' '))
        m = n1 * n2
        print(f'{n1} X {n2} = {m}')
    if op2 == 'A':
        a1 = float(input(' '))
        a2 = float(input(' '))
        ad = a1 + a2
        print(f'{a1} + {a2} = {ad}')
    if op2 == 'S':
        s1 = float(input(' '))
        s2 = float(input(' '))
        sub = s1 - s2
        print(f'{s1} - {s2} = {sub}')
if opção == 'P':
    e1 = int(input(' '))
    e2= int(input(' '))
    p = e1 ** e2
    print(f'{e1} ** {e2} = {p}')
if opção =='B':
    num = int(input(' '))
    print(f'{num,bin(num)[:2]}')
if opção == 'He':
    num = int(input(' '))
    print(f'{num,hex(num)[:2]} ')
if opção == 'O':
    num = int(input(' '))
    print(f'{num,oct[:2]}')
print('-='*30)
print('Até mais...')
