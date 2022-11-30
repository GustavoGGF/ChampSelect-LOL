#Escolha aleatorias de armas COD

import random
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

def RandomGuns():

    Prim = ['KG-M40', 'NZ-41', 'UGM-8', 'Cooper-Carbine', 'Volk', 'M13', 'Kilo', 'Vargo-52']
    Sec = ['MP5', 'MP7', 'R9', 'PPSh', 'H4', 'Owen']

    gerador1 = random.choices(Prim)
    gerador2 = random.choices(Sec)

    saida1['text'] = gerador1
    saida2['text'] = gerador2

janela = ThemedTk(theme='breeze')

janela.title('Gerador de armas aleatorias')
janela.geometry('320x200')

botao1 = ttk.Button(janela, text='Gerar arma', command=RandomGuns)
botao1.pack(pady=20)

texto1 = ttk.Label(janela, text='Arma Principal: ')
texto1.pack()

saida1 = ttk.Label(janela, text='')
saida1.pack(pady=10)

texto2 = ttk.Label(janela, text='Arma Secundária: ')
texto2.pack()

saida2 = ttk.Label(janela, text='')
saida2.pack(pady=10)

janela.mainloop()