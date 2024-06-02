from tkinter import *
from random import *
import numpy as np

root = Tk()
window = Frame(root)
window.grid()


canvas = Canvas(window, width=800, height=800, background='light grey')

"""
graph = [[2, 7, 11], [3,4,10,9], [0, 5, 8], [1,4,6,10], [1,3,6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1,6,9], [0]]


pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])
"""

"""
générer grille cafe
"""

def color_generator():
    r, g, b = rd.randint(0,255), rd.randint(0,255),rd.randint(0,255)
    return f"#{r:02x}{g:02x}{b:02x}"

i = 0
j = 0

def graphcafe(canvas):
    D = {}
    global i
    global j
    pos=[]
    for x in range(0,800,20):
        for y in range(0,800,20):
            pos.append([x,y])
            canvas.create_oval(x-4,y-4,x+4,y+4,fill=color_generator())
            if i == 40:
                i = 0
                j += 1
            D[(i,j)] = []
            i += 1
    for (k,l) in D:
        probak, probal = random(), random()
        if probak <= 0.4 :
            D[(k,l)].append((k+1,l))
        if probal <= 0.4 :
            D[(k,l)].append((k,l+1))
    #print(D)
    for a in D:
        for b in D[a]:
            canvas.create_line(pos[a][0], pos[a][1], pos[j][0], pos[j][1])


COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']

# liste de couleur adaptée au graph
color = COLORS[0:len(graph)]

def draw(canvas, graph, pos,color):
    N = len(graph)
    count= 0
    for i in range(N):
        for j in graph[i]:
            canvas.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for i in range(N):
        (x,y) = (pos[i][0],pos[i][1])
        canvas.create_oval(x-6,y-6,x+6,y+6,fill=color[i])
        txt = canvas.create_text(pos[count][0]-20, pos[count][1], text=str(count), font="Arial 16", fill="black")
        count+=1

"""
trouver les composantes connexes
"""


def min_local(i,graph):
    global color
    noeud_min = i
    for j in graph[i]:
        if j<=i :
            noeud_min = j
    #print(str(noeud_min) + ":" + color[noeud_min])
    for j in graph[i]:
        color[j] = color[noeud_min]
    color [i] = color[noeud_min]
    #print(color)

def connexe(graph):
    N = len(graph)
    for i in range(N):
        min_local(i,graph)
    soluc = []
    for name in color:
        if name not in soluc:
            soluc.append(name)
    return len(soluc)





canvas.pack()

#min_local(4,graph)
#connexe(graph)
"""
à rentrer dans la console pour avoir le nombre de composantes connexes
"""
graphcafe(canvas)

#draw(canvas,graph,pos,color)

root.mainloop()