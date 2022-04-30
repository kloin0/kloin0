import tkinter as tk 
from tkinter import * 
tela = Tk()
tela.title("Login em Python") 
def click_button():
    login = edemail.get()
    senha = edsenha.get() 
    if login == "gustavohenrique@gmail.com" and senha == "g1u2s3t4":
        lb = Label(tela,text="Bem vindo")
        lb.grid(row=4, column=1) 
    else:
        lb1 = Label(tela, text="Erro") 
        lb1.grid(row=4, column=1)
email = Label(tela, text="Login: ")
email.grid(row=0,column=0) 
senha = Label(tela, text="Senha:") 
senha.grid(row=1, column=0 )
edemail = Entry(tela) 
edemail.grid(row=0,column=1)
edsenha = Entry(tela) 
edsenha.grid(row=1 , column=1)
bot = Button(tela, text="Confirmar", command=click_button) 
bot.grid(row = 2, column = 1) 
tela.geometry("300x300") 
tela.mainloop() 
