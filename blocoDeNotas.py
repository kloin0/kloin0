from cProfile import label
import tkinter 
import os 
from tkinter import * 
from tkinter.messagebox import * 
from tkinter.filedialog import * 
from turtle import width 
class Notepad():
    root = Tk()
    thiswidrh = 300
    thisheight = 300 
    thisTextArea = Text(root)
    thisMenuBar = Menu(root)
    thisFileMenu = Menu(thisMenuBar,tearoff=0)
    thisEditMenu = Menu(thisMenuBar,tearoff=0)
    thisHelpMenu = Menu(thisMenuBar,tearoff=0)
    thisScrollBar = Scrollbar(thisTextArea)
    file = None 
    def __init__(self,**kwargs):
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass 
        try:
            self.thiswidrh = kwargs['width']
        except KeyError:
            pass 
        try:
            self.thisheight = kwargs['height']
        except KeyError:
            pass 
        self.root.title("Untitled - Notepad")
        screenWidth = self.root.winfo_screenmmwidth()
        screenHeight = self.root.winfo_screenheight()
        left = (screenWidth/2) - (self.thiswidrh/2)
        top = (screenHeight/2) - (self.thisheight/2)
        self.root.geometry('%dx%d+%d+%d'%(self.thiswidrh,self.thisheight,left,top))
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.thisTextArea.grid(sticky=N+E+S+W)
        self.thisFileMenu.add_command(label='Novo',command=self.newFile)
        self.thisFileMenu.add_command(label='Abrir',command=self.openFile)
        self.thisFileMenu.add_command(label='Salvar',command=self.saveFile)
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label='Sair',command=self.quitapplication)
        self.thisMenuBar.add_cascade(label='Arquivo',menu=self.thisFileMenu)
        self.thisEditMenu.add_command(label='Cortar',command=self.cut)
        self.thisEditMenu.add_command(label='Copiar',command=self.copy)
        self.thisEditMenu.add_command(label='Colar',command=self.paste)
        self.thisMenuBar.add_cascade(label='Editar',command=self.thisEditMenu)
        self.thisHelpMenu.add_command(label='sobre o bloco de notas',command=self.thisFileMenu)
        self.thisMenuBar.add_cascade(label='Ajudar',menu=self.thisHelpMenu)
        self.root.config(menu=self.thisMenuBar)
        self.thisScrollBar.pack(side=RIGHT,fill=Y)
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)
    def quitapplication(self):
        self.root.destroy()
    def showAbout(self):
        showinfo("Notepad","Mrinal Verma")
    def openFile(self):
        self.file = askopenfilename(defaultextension='.txt',filetypes=[('Todos Arquivos',"*.*"),
            ("Text Documents","*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file)+"-Notepad")
            self.thisTextArea.delete(1.0,END)
            file = open(self.file,"r")
            self.thisTextArea.insert(1.0,file.read())
            file.close()
    def newFile(self):
        self.root.title("Untitled-Notepad")
        self.file = None
        self.thisTextArea.delete(1.0,END)
    def saveFile(self):
        if self.file== None:
            self.file = askopenfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),
            ("Text Documents","*.txt")])
                
            if self.file == "":
                self.file = None 
            else:
                file = open(self.file,"v")
                file.write(self.thisTextArea.get(1.0,END))
                file .close()
                self.root.title(os.path.basename(self.file)+"-Notepad")
        else:
            file = open(self.file,"v")
            file.write(self.thisTextArea.get(1.0,END))
            file.close()
    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")
    def copy(self):
        self.thisTextArea.event_generate("<<Copy>>")
    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")
    def run(self):
        self.root.mainloop()
notepad = Notepad(width=600,heigth=500)
notepad.run()