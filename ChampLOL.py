from random import choices
from ttkthemes import ThemedTk
from tkinter import ttk

def ChampTop(event):
    top = ['Aatrox', 'Akali', 'Bardo', 'Braum', 'Camille', 'Cassiopeia', "Cho'Gath", 'Darius', 'Diana', 'Dr.Mundo', 'Ekko', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 
    'Garen', 'Gnar', 'Gragas', 'Heimerdinger', 'Illaoi', 'Irelia', 'Jarvan-IV', 'Jax', 'Jayce', 'Kayle', 'Kayn', 'Kennen', 'Kled', 'Lee-Sin', 'Lillia', 'Lissandra', 
    'Malphite', 'Maokai', 'Master-Yi', 'Mordekaiser', 'Nasus', 'Nautilus', 'Nunu', 'Olaf', 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Rammus', "Rek'Sai", 'Renekton', 
    'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Swain', 'Tahm-Kench', 'Taric', 'Teemo', 'Trundle', 'Tryndamere', 
    'Urgot', 'Vayne', 'Vi', 'Viego', 'Vladmir', 'Volibear', 'Warwick', 'Wukong', 'Xin-Zhao', 'Yasuo', 'Yone', 'Yorick']

    top = choices(top, k=1)
    texto2['text'] = top

    return top

def ChampJg(event):
    jg = ['Amumu', 'Bel-Veth', 'Cho-Gath', 'Darius', 'Diana', 'Ekko', 'Elise', 'Evelynn', 'Fiddlesticks', 'Garen', 'Grargas', 'Ivern', 'Jarvan-IV', 'Jax', 'Karthus', 
    'Kayn', "Kha'Zix", 'Kindred', 'Lee-Sin', 'Lillia', 'Master-Yi', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Pantheon', 'Poppy', 'Qiyana', 'Rammus', 'Rek-Sai', 'Rengar', 
    'Sejuani', 'Shaco', 'Shyvana', 'Skarner', 'Taliyah', 'Trundle', 'Tryndamere', 'Udyr', 'Vi', 'Viego', 'Volibear', 'Warwick', 'Wukong', 'Xin-Zhao', 'Zac']

    jg = choices(jg, k=1)
    texto2['text'] = jg

    return jg

def ChampMid(event):
    mid = ['Ahri', 'Akali', 'Akshan', 'Amumu', 'Anivia', 'Annie', 'Aurelion-Sol', 'Azir', 'Bardo', 'Blitzcrank', 'Brand', 'Caitlyn', 'Cassiopeia', 'Cho-Gath', 'Corki', 
    'Diana', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fizz', 'Galio', 'Gangplank', 'Grargas', 'Heimerdinger', 'Janna', 'Jayce', 'Jhin', 'Kai-sa', 'Karma', 'Karthus', 'Kassadin',
    'Katarina', 'Kayn', 'Kennen', 'LeBlanc', 'Lissandra', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Morgana', 'Neeko', 'Nidalee', 'Nocturne', 'Oriana', 'Qiyana', 'Rakan', 'Rumble',
    'Ryze', 'Swain', 'Sylas', 'Syndra', 'Taliyah', 'Talon', 'Teemo', 'Tristana', 'Twisted-Fate', 'Veigar', "Vel'Koz", 'Vex', 'Viktor', 'Vladmir', 'Wukong', 'Xerath', 'Yasuo', 
    'Yone', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']

    mid = choices(mid, k=1)
    texto2['text'] = mid

def ChampADC(event):
    adc = ['Akshan', 'Aphelios', 'Ashe', 'Bardo', 'Caitlyn', 'Cassiopeia', 'Corki', 'Draven', 'Ezreal', 'Heimerdinger', 'Jhin', 'Jinx', 'Kai-sa', 'Kalista', 'Kog-Maw', 
    'Lucian', 'Lulu', 'Miss-Fortune', 'Nilah', 'Quinn', 'Samira', 'Senna', 'Sivir', 'Teemo', 'Tristana', 'Twitch', 'Varus', 'Vayne', 'Veigar', 'Vel-Koz', 'Xayah', 
    'Yasuo', 'Zeri', 'Ziggs']

    adc = choices(adc, k=1)
    texto2['text'] = adc

    return adc

def ChampSup(event):
    sup = ['Alistar', 'Amumu', 'Anivia', 'Annie', 'Ashe', 'Aurelion-Sol', 'Bardo', 'Blitzcrank', 'Brand', 'Braum', 'Camille', 'Cho-Gath', 'Fiddlesticks', 'Galio', 'Grargas', 
    'Ivern', 'Janna', 'Karma', 'Karthus', 'Leona', 'Lissandra', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Morgana', 'Nami', 'Nautilus', 'Neeko', 'Nidalee', 'Nunu', 
    'Pantheon', 'Poppy', 'Pyke', 'Rakan', 'Rammus', 'Rell', 'Renata-Glasc', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Sona', 'Soraka', 'Swain', 'Tahm-Kench', 
    'Taric', 'Thresh', 'Veigar', 'Vel-Koz', 'Vex', 'Xerath', 'Yummi', 'Zilean', 'Zoe', 'Zyra']

    sup = choices(sup, k=1)
    texto2['text'] = sup

    return sup



janela = ThemedTk(theme='breeze')
 
janela.title('Gerador de Champs Aleatório')

texto1 = ttk.Label(janela, text='Escolha a lane')
texto1.pack(pady=10)

botao1 = ttk.Button(janela, text='Top')
botao1.pack(pady=2.5)
botao1.bind('<ButtonPress-1>', ChampTop)

botao2 = ttk.Button(janela, text='Jungle')
botao2.pack(pady=2.5)
botao2.bind('<ButtonPress-1>', ChampJg)

botao3 = ttk.Button(janela, text='Mid')
botao3.pack(pady=2.5)
botao3.bind('<ButtonPress-1>', ChampMid)

botao4 = ttk.Button(janela, text='AdCarry')
botao4.pack(pady=2.5)
botao4.bind('<ButtonPress-1>', ChampADC)

botao5 = ttk.Button(janela, text='Support')
botao5.pack()
botao5.bind('<ButtonPress-1>', ChampSup)

texto2 = ttk.Label(janela, text='')
texto2.pack(pady=10)

janela.mainloop()