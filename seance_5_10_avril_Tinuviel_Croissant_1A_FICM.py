
from tkinter import *
from tkinter import ttk
from random import *
from math import *
import keyboard

"""
Je n'arrive pas à installer le module keyboard sur mon ordinateur donc je n'ai pas pu tester le fonctionnement d'un tir unique avec la touche f

"""

root = Tk()
window = Frame(root)
window.grid()


# cible
canvas = Canvas(window, width=400, height=400, background='red')

def all_cercle():
    R = 180
    """les cercles sont centrés en (200,200)"""
    for i in range(6):
        R = 180 - 30*i
        if i == 4 :
            canvas.create_oval(200-R, 200-R, 200+R, 200+R, outline = "red", fill = "red", width = 2)
        else:
            canvas.create_oval(200-R, 200-R, 200+R, 200+R, outline = "red", fill = "ivory", width = 2)

def ligne():
    ligne1 = canvas.create_line(200, 0, 200, 400, fill="red")
    ligne2 = canvas.create_line(0,200,400,200, fill="red")

def numero_cible():
    count = 35
    txt = canvas.create_text(200, count, text="1", font="Arial 16", fill="red")
    for i in range(2,7):
        count += 30
        if i == 5 :
            txt = canvas.create_text(200, count, text=str(i), font="Arial 16", fill="ivory")
        else:
            txt = canvas.create_text(200, count, text=str(i), font="Arial 16", fill="red")

# méchanisme de tir
nb_tir = 0
points = 0
nb_max = 5
label = Label(window, text="")
label.pack()
"""
Ces deux varibles sont absolues car on en a besoin dans et hors de fonctions. Une fois une partie terminée (5 tirs), elles sont réinitalisées quand on recharge la page

"""

def score(x,y):
    R = sqrt((x-200)**2 + (y-200)**2)
    if R<=30:
        return 6
    elif R <= 60:
        return 5
    elif R <= 90:
        return 4
    elif R <= 120:
        return 3
    elif R <= 150:
        return 2
    elif R <= 180:
        return 1
    else:
        return 0

# fin de partie
if nb_tir > nb_max:
    """ on dépasse le nombre maximal de tir pour une partie"""
    Label(window, text = "Plus de tirs disponibles. Quitter pour recommencer").pack()

# un tir avec la touche 'f'
if keyboard.read_key() == "f" and nb_tir <= nb_max :
    nb_tir += 1
    x = randint(0,400)
    y = randint(0,400)
    """ici x et y sont les vrais coordonées du centre du cercle"""
    canvas.create_oval(x-10,y-10,x+10,y+10,outline="black", fill = "black")
    points += score(x,y)
    label.config (text = "Score de " + str(points) + " points")

# tir en rafale
def tirer():
    global nb_tir
    global label
    nb_tir+=1
    if nb_tir > nb_max:
        Label(window, text = "Plus de tirs disponibles. Quitter pour recommencer").pack()
        return
    for i in range(nb_max-nb_tir):
        x = randint(0,400)
        y = randint(0,400)
        canvas.create_oval(x-10,y-10,x+10,y+10,outline="black", fill = "black")
        points += score(x,y)
    label.config(text = "Score de " + str(points) + " points")


b1 = ttk.Button(window, text="Feu", command = tirer)
b1.pack(side=RIGHT, padx=10, pady=10)
b2 = ttk.Button(window, text="Quitter", command=window.destroy)
b2.pack(side=LEFT, padx=10, pady=10)


all_cercle()
numero_cible()
line()
canvas.pack()
root.mainloop()

