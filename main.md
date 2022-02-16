from curses import pair_number
from tkinter import *
from click import command
root = Tk()
root.title('Calculadora')
visor = Entry(root,bg='gray')
visor.pack(padx=100,pady=50)
def click_pon():
    visor.insert(END,".")
def igual():
    s_numero = visor.get()
    visor.delete(0,END)
    if matematica == 'soma':
        visor.insert(0,p_numero + float(s_numero))
def soma():
    p_valor = visor.get()
    global p_numero
    global matematica
    matematica = 'soma'
    p_numero = float(p_valor)
    visor.delete(0,END)
def multiplicação():
    p_calor = visor.get()
    global primeir_n
    global matematica
    matematica = 'multiplicação'
    primeir_n = float(p_calor)
    visor.delete(0,END)
def deletar():
    visor.delete(0,END)
def click_button(numeros):
    agora = visor.get()
    visor.delete(0,END)
    visor.insert(END,str(agora) + str(numeros))
lb = Label(root, text='Calculadora',font=("verdana",20,"bold"),pady=30)
bt1 = Button(root , text='1', bg='gray', padx=14, pady= 14,bd=4,command=lambda:click_button(1))
bt1.place(x=10,y=100)
bt2 = Button(root, text='2',bg='gray', padx=14, pady=14,bd=4,command=lambda:click_button(2))
bt2.place(x=60,y=100)
bt3 = Button(root, text='3',bg='gray',padx=14, pady=14, bd=4,command=lambda:click_button(3))
bt3.place(x=100,y=100)
bt4 = Button(root, text='4',bg='gray',padx=14,pady=14, bd=4,command=lambda:click_button(4))
bt4.place(x=10,y=160)
bt5 = Button(root,text='5',bg='gray',padx=14,pady=14, bd=4,command=lambda:click_button(5))
bt5.place(x=60,y=160)
bt6 = Button(root, text='6',bg='gray',padx=14,pady=14,bd=4,command=lambda:click_button(6))
bt6.place(x=100,y=160)
bt7 = Button(root,text='7',bg='gray',padx=14,pady=14, bd=4,command=lambda:click_button(7))
bt7.place(x=10,y=217)
bt8 = Button(root,text='8',bg='gray',padx=14,pady=14,bd=4,command=lambda:click_button(8))
bt8.place(x=60,y=217)
bt9 = Button(root,text='9',bg='gray',padx= 14,pady=14,bd=4,command=lambda:click_button(9))
bt9.place(x=100,y=217)
bt0 = Button(root,text='0',bg='gray',padx= 14,pady=14,bd=4,command=lambda:click_button(0))
bt0.place(x = 153,y = 217)
vir = Button(root,text='.',bg='gray',padx=14,pady=14,bd=4,command=click_pon)
vir.place(x=153,y=158)
spec = Button(root,text='  ',bg='gray',padx=14,pady=24,bd=4,command=lambda:click_button(' '))
spec.place(x=205,y=198)
mais = Button(root,text='+',bg='gray',padx=14,pady=14,bd=4,command=soma)
mais.place(x=152,y=104)
apagar = Button(root,text='<-',bg='gray',padx=14,pady=14,bd=4,command=deletar)
apagar.place(x=201,y=104)
b_igual = Button(root,text='=',bg='gray',padx=14,pady=34,bd=4,command=igual)
b_igual.place(x=255,y=150)
root.geometry('300x300')
root.mainloop()
