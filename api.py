from cProfile import label
import requests 
import json 
import tkinter
url = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
url = url.json()
cont_euro = url ['EURBRL']["bid"]
cont_dolar = url ['USDBRL']["bid"]
cont_bct = url ['BTCBRL']["bid"]
tela = tkinter.Tk()
tela.geometry('400x400')
telaEuro = tkinter.Label(
    tela,
    text=f"EURO = {cont_euro[:3]}",
    font="Arial",
    bd =1 
).pack()
telaDolar = tkinter.Label(
    tela,
    text=f"Dolar = {cont_dolar[:4]}",
    font="Arial",
    bd = 1
).pack()
telaBtc = tkinter.Label(
    tela,
    text=f"Bitcoin = {cont_bct}",
    font="Arial",
    bd=1
).pack()
tela.mainloop()

