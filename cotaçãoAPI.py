from tkinter import * 
import tkinter as tk 
import requests 
import json
tela = Tk()
tela.geometry('600x600')
# Pagar a api
cont = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cont = cont.json()
cont_euro = cont ['EURBRL']["bid"]
cont_dolar = cont['USDBRL']["bid"]
cont_bct = cont ['BTCBRL']["bid"]
# Interface grafica para Api 
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
# Criar um visor,Pagar o valor do visor em real e converter de acordo com a cotação das moedas 
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
# Uma função para converter as moedas

# Criar um button para realizar a coversão 

tela.mainloop()
