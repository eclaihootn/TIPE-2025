import tkinter as tk
from PIL import Image
from qrcode_gen_nuance import *

root = tk.Tk()
fen = tk.Frame(root)
root.geometry("500x500")

canvas = tk.Canvas(fen, width = 500, height = 500)

def afficher_tab(qrcode):
    """Permet l'affichage dans la fenêtre tkinter du qrcode"""
    s = qrcode._size
    lc : int = 500//s   #largeur d'un module (= une case )
    tab = qrcode._modules_nuances
    n,m = len(tab),len(tab[0])
    for i in range(n):
        for j in range(m):
            c = "#" + tab[i][j].tk_format()*3      #+ "00"*2
            canvas.create_rectangle(j*lc, i*lc, (j+1)*lc, (i+1)*lc, fill = c, outline = "" )
    
qr = QrCode.encode_text("Texte à encoder" , QrCode.Ecc.MEDIUM, nb_nuances = 2)
tab = qr.cvt_intensite_to_numpy()   # converti mon tableau de valeurs de type Intensite en 
                                    # un tableau numpy pour afficher/enregistrer l'image
img = Image.fromarray(tab)
img.save(fp="nom_de_l_image_enregistree")
img.show()
afficher_tab(qr)

fen.pack()
canvas.pack()
root.mainloop()
