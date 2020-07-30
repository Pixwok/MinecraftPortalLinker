from tkinter import *
from tkinter.messagebox import *

def link():
    Z = CordZ.get() / 8
    X = CordX.get() / 8
    showinfo('Coordonnées du portail','Voici les coordonnées de votre portail dans le Nether. \n X:{0:6.1f} Y: 64 Z:{1:6.1f}'.format(X, Z))

#Initialisation Feunêtre
window = Tk()
window.title("NetherPortalLinker")
window.iconbitmap('.img\\Portail_du_Nether.ico')
window.geometry("480x360")
window.minsize(480, 360)
window.maxsize(480, 360)
title = Label(window, text="Nether Portal Linker", font=("Helvetica", 35))

#Boutton
BouttonLink = Button(window, text="Link", fg='black', bg='#a4a4a4', width='15', command = link)

#Texte des champs
label_cord1 = Label(window, text="Coordonnée X", font=("Helvetica", 15))
label_cord2 = Label(window, text="Coordonnée Z", font=("Helvetica", 15))

#Champ (Coordonnées X et Z)
CordX = IntVar()
ChampX = Entry(window, textvariable=CordX, bg='#d7d4d3', fg='black', width="10")
ChampX.focus_set()

CordZ = IntVar()
ChampZ = Entry(window, textvariable=CordZ, bg='#d7d4d3', fg='black', width="10")
ChampZ.focus_set()

#Position des objets dans la feunêtre
title.pack(fill=X, pady=15)
label_cord1.pack(fill=X, padx=10, pady=10)
ChampX.pack(fill=X, padx=100, pady=5)
label_cord2.pack(fill=BOTH, padx=10, pady=10)
ChampZ.pack(fill=BOTH, padx=100, pady=5)
BouttonLink.pack(pady=12)


window.mainloop()