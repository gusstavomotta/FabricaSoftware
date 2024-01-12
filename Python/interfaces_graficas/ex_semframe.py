from tkinter import *

def f1(self):
    print('Botão clicado')

principal = Tk()
#fr1 = Frame(principal)
#fr1.configure(borderwidth=2, border=3)
#fr1.pack()
#fr2 = Frame(principal)
#fr2.configure(borderwidth=2, border=3)
#fr2.pack()
olatexto=Label(principal, text='Olá mundo!')
olatexto.pack()
botao1=Button(principal, text='Ok', width=10, height=2)
botao1["width"]=10
botao1["height"]=3
botao1.bind("<Button-1>", f1)
botao1.pack()
botao2=Button(principal, text='Sair')
botao2["width"]=10
botao2["height"]=3
botao2["command"]=principal.quit
botao2.pack(side=LEFT)
principal.mainloop()