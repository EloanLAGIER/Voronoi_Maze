import random
import itertools
from tkinter import *

distance = 50
nb_points = 100

points = []

# Generer tous les points du canvas
candidates = list(itertools.product(range(500), range(500)))

for i in range(nb_points):
    print(i)
    # Vérifier que l'on peut encore sampler des points sinon sortir
    if not len(candidates):
        break

    # Sampler un point au hasard dans la liste des points autorisés : `candidates`
    point = x, y = random.choice(candidates)

    # Ajouter ce point à la liste des points
    points.append(point)

    # Supprimer des points autorisés tous ceux qui sont 
    # dans le périmètre du dernier point échantilloné
    candidates = [
        (xx, yy) 
        for xx, yy in candidates 
        if ((x - xx) ** 2 + (y - yy) ** 2) ** .5 > distance
    ]


fenetre =Tk()
canvas = Canvas(fenetre,width=500, height=500, backgroun='grey')


for v in points:
    canvas.create_oval(v[0]-25,v[1]-25,v[0]+25,v[1]+25)
canvas.pack()
fenetre.mainloop()
