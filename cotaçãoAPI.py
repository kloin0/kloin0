from tkinter import *
import tkinter
import requests
import json 
tela = tkinter.Tk()
tela.geometry('300x400')
def cont_1btc():
    btc = visorbtc.get()
    real = cont_bct
    btcfinal = float( btc * real)
    print(f'{btcfinal}')

def cont_1euro():
    euro2 = visorbtc.get()
    real = cont_bct
    eurofinal = float( euro2 * real)
    print(f'{eurofinal}')

def cont_1dolar():
    dolar1 = visorbtc.get()
    real = cont_bct
    dolarfinal = float( dolar1 * real)
    print(f'{dolarfinal}')
tela_btc = Label(
tela,
text="BTC",
font="Arial 10",
bd=1, 
).pack()
visorbtc = Entry(tela,bg='gray')
visorbtc.pack(padx=100,pady=9)   
tela_euro = Label(
    tela,
    text="EURO",
    font="Arial 10",
    bd=1,
).pack()
visoreuro = Entry(tela,bg='gray')
visoreuro.pack(padx=100,pady=11)
tela_dollar = Label(
    tela,
    text="DOLAR",
    font="Arial 10",
    bd=1
).pack()
visor_dolar = Entry(tela,bg="gray")
visor_dolar.pack(padx=100,pady=12)
cont = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cont = cont.json()
cont_euro = cont ['EUR']["bid"]
cont_dolar = cont['USD']["bid"]
cont_bct = cont ['BTC']["bid"]
'''print(f'Dolar = {cont_dolar}')
print(f'Euro = {cont_euro}')
print(f'Bitcoin = {cont_bct}')'''
btc = Label(
    tela,
    text=f'BTC {cont_bct}',
    )
btc.pack()
euro = Label(
    tela,
    text=f'Euro {cont_euro}')
euro.pack()
dolar = Label(
    tela,
    text=f'Dolar {cont_dolar}')
dolar.pack()
tela.mainloop()
