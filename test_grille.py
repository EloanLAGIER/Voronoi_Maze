from random import *
from tkinter import *

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Cellule:
    index=-1
    vh=None
    vd=None
    vb=None
    vg=None
    p1=None
    p2=None
    p3=None
    p4=None
    def __init__(self,i):
        self.index=i
        
class Grille :
    dicCel={}
    def __init__(self,n,a):
        t=n/a
        b=t/4
        print(t)
        print(b)
        for j in range(a):
            for i in range(a):
                c=Cellule(j*a+i)
                if j==0:
                    if i==0:
                        c.p1=Point(i*t+uniform(-b,b),j+uniform(-b,b))
                        c.p2=Point((i+1)*t+uniform(-b,b),j+uniform(-b,b))
                    else:
                        c.p1=self.dicCel[j*a+(i-1)].p2
                        c.p2=Point((i+1)*t+uniform(-b,b),j+uniform(-b,b))
                else:
                    iv=(j-1)*a+i
                    c.p1=self.dicCel[iv].p4
                    c.p2=self.dicCel[iv].p3
                    c.vh=self.dicCel[iv]
                    self.dicCel[iv].vb=c
                if i==0:
                    c.p4=Point(i+uniform(-b,b),(j+1)*t+uniform(-b,b))
                else:
                    iv=(j*a+i-1)
                    c.p4=self.dicCel[iv].p3
                    
                    c.vg=self.dicCel[iv]
                    self.dicCel[iv].vd=c
                c.p3=Point((i+1)*t+uniform(-b,b),(j+1)*t+uniform(-b,b))
                self.dicCel[c.index]=c

g=Grille(500,100)
print(len(g.dicCel))

fenetre=Tk()
canvas=Canvas(fenetre,width=600,height=600,background='green')
for c in g.dicCel.values():
    canvas.create_line(50+c.p1.x,50+c.p1.y,50+c.p2.x,50+c.p2.y,50+c.p3.x,50+c.p3.y,50+c.p4.x,50+c.p4.y,50+c.p1.x,50+c.p1.y)
canvas.pack()
fenetre.mainloop()
    
    
