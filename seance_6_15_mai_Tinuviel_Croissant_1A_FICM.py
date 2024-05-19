from tkinter import *
from random import *
import numpy as np
from math import *

root = Tk()
window = Frame(root)
window.grid()


canvas = Canvas(window, width=800, height=800, background='white')

graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0],
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

pos = np.array([(randint(0,800), randint(0,800)) for i in range(len(graph))])


def draw(canvas, graph, pos):
    count= 0
    for i in range(len(graph)):
        for j in graph[i]:
            canvas.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        canvas.create_oval(x-20,y-20,x+20,y+20,fill="white")
        txt = canvas.create_text(pos[count][0], pos[count][1], text=str(count), font="Arial 16", fill="black")
        count+=1

#draw(canvas,graph,pos)

signe=[-1,1]
def force(x1,y1,x2,y2,k,lo):
    Fx = signe[randint(0,1)]*k*(abs(x2-x1) - lo)
    Fy = signe[randint(0,1)]*k*(abs(y2-y1) - lo)
    return (Fx,Fy)


lo = 100
k = 100
tau = 0.01
vit = np.array([((random()-0.5)*10, (random()-0.5)*10) for i in range(len(graph))])

def ressort(canvas, graph):
    global vit
    global pos
    for i in range(len(graph)):
        F=[None]*len(graph[i])
        print(F)
        count = 0
        for j in graph[i]:
            F[count] = force(pos[i][0], pos[i][1], pos[j][0], pos[j][1], k, lo)
            print(F)
            count += 1
        vit[i][0] = vit[i][0] + sum(F[k][0] for k in range(count))*tau
        pos[i][0] = pos[i][0] + tau*vit[i][0]
        # somme des Fx fonctionne : renvoit bien un entier
        vit[i][1] = vit[i][1] + sum(F[k][1] for k in range(count))*tau
        pos[i][1] = pos[i][1] + tau*vit[i][1]
    canvas.delete('all')
    draw(canvas,graph,pos)


canvas.pack()
root.bind("<KeyPress-f>", lambda e : ressort(canvas,graph))
root.mainloop()















