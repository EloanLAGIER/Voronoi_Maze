from random import *
from math import *
from copy import *
##from tkinter import *

#fonction principale( taille = dimension du carré général et n nombre de cellules de voronoi )
def generate_voronoi(taille,n):
    
    listPoint=[] #liste dans laquelle va y avoir tout les points
    
    centieme=taille/100#calcul du centieme de la taille pour pas que yest des points pil sur les bords

    #generation des points aleatoire (encore très simple )
    for i in range(n):
        x= randint(centieme,taille-(centieme))
        y= randint(centieme,taille-(centieme))
        listPoint.append([x,y])

    #fonction renvoyant les triangles de la triangulation des points
    listTri=BowyerWatson(taille,listPoint)

    #fonction renvoyant les cellules de voronoi
    lVor=voronoi(listPoint,listTri)
    print(listPoint)
    return lVor

#fonction pas faite par moi calculant si deux lignes se croisent c'etait fait a la rache sur un forum on peut se l'aproprier
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]


#fonction faite par moi calculant la mediane mais du coup mdr c'est n'importequoi
def mediane(p1,p2):
    x1=p1[0]
    x2=p2[0]
    y1=p1[1]
    y2=p2[1]
    div=y1-y2

    #genre ça c'est de la triche, euler se suicide
    if div==0:
        div=0.1
    mil=[(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
    p1y= (pow(x1,2) - pow(x2,2) + pow(y1,2) - pow(y2,2))/(2*(div))
    return [mil,[0,p1y]]

#instancede l'objet triangle qui va beaucoup servir
class Triangle :

    #ça c'est la fonction qui s'active quand on créer une instance
    def __init__(self,point1,point2,point3):

        #les trois points du triangle p1,p2,p3
        self.p1=point1
        self.p2=point2
        self.p3=point3

        #les trois segments du triangle seg1,seg2,seg3
        self.seg1=trier_edge(self.p1[0],self.p1[1],self.p2[0],self.p2[1])
        self.seg2=trier_edge(self.p2[0],self.p2[1],self.p3[0],self.p3[1])
        self.seg3=trier_edge(self.p3[0],self.p3[1],self.p1[0],self.p1[1])

        #la liste des bords listEdge
        self.listEdge=[self.seg1,self.seg2,self.seg3]

        #liste des points P
        self.listP=[self.p1,self.p2,self.p3]

        #medianes med1 med2
        self.med1=mediane(self.p1,self.p2)
        self.med2=mediane(self.p2,self.p3)

        #centre cercle Circoncis (mdr la blague)
        self.centre=line_intersection(mediane(self.p1,self.p2),mediane(self.p2,self.p3))

        #rayon du cercle Circoncis
        self.rayon=sqrt(pow((self.centre[0]-self.p1[0]),2)+pow((self.centre[1]-self.p1[1]),2))


    #fonction qui pour un point p regarde si il est dans le cercle Circoncis
    def est_dans_cercle(self,p):
              return (sqrt(pow(p[0]-self.centre[0],2)+pow(p[1]-self.centre[1],2))<self.rayon)

    #fonction qui regarde si un point p est dans le triangle
    def a_le_point(self,p):
        return self.p1==p or self.p2==p or self.p3==p

    #fonction qui regarde si un triangle t a un coté commun
    def cote_commun(self,t):
        return (t.seg1==self.seg1)or(t.seg1==self.seg2)or(t.seg1==self.seg3)or(t.seg2==self.seg1)or(t.seg2==self.seg2)or(t.seg2==self.seg3)or(t.seg3==self.seg1)or(t.seg3==self.seg2)or(t.seg3==self.seg3)

    #fonction qui regarde si un triangle t a un point commun
    def point_commun(self,t):
        return (t.p1==self.p1)or(t.p1==self.p2)or(t.p1==self.p3)or(t.p2==self.p1)or(t.p2==self.p3)or(t.p2==self.p3)or(t.p3==self.p1)or(t.p3==self.p2)or(t.seg3==self.p3)

#en faite quand on compare les segments des fois c'est les meme mais dans l'autre sens alors le programme comprend pas
#du coup j'ai crée une fonction qui tri toujours les sgmens dans le meme sens voila voila
def trier_edge(x1,y1,x2,y2):
    calc1=x1*500+y1
    calc2=x2*500+y2
    if calc1<calc2:
        return [[x1,y1],[x2,y2]]
    else:
        return [[x2,y2],[x1,y1]]

#fonction qui crée le voronoi ça complexité et de O^3 c'est affreux
def voronoi(lp, lt):
    ListVor=[]
    incr=0
    lpb=[]
    for p in lp:
        incr+=1
        L=[]
        V=[]
        for t in lt:

            if t.a_le_point(p):
                L.append(t)
        if len(L)==3:
            V.append(L[0].centre)
            V.append(L[1].centre)
            V.append(L[2].centre)
        else:
            t_act=L[0]
            t_suiv=L[1]
            V.append([round(t_act.centre[0]),round(t_act.centre[1])])
            for i in range(len(L)-1):
                count=0
                while (not(t_suiv.cote_commun(t_act))) and count<100:
                    count+=1
                    r=randint(0,len(L)-1)

                    while (r==L.index(t_act)):

                        r=randint(0,len(L)-1)
                    t_suiv=L[r]
                if count==100:
                    lpb.append(incr)
                V.append([round(t_suiv.centre[0]),round(t_suiv.centre[1])])
                L.pop(L.index(t_act))
                t_act=t_suiv
                if len(L)>1:
                    r=randint(0,len(L)-1)
                    while (r==L.index(t_act)):
                        r=randint(0,len(L)-1)
                    t_suiv=L[r]


        ListVor.append(V)
    return ListVor


#la triangulation a une complexité de O^2 mais askip on peut la faire en O*ln(0)
#faut la nettoyer et cheker comment les cas particuliers possible
def BowyerWatson(taille,lp):
    triangulation=[]
    L=[[-taille,-10],[2*taille,-20],[taille/2,2*taille]]
    supT=Triangle(*L)

    triangulation.append(supT)
    for p in lp:
        badTriangles=[]
        badTriangleEdge=[]

        for t in triangulation :
            
            
            if t.est_dans_cercle(p):
                badTriangles.append(t)
                for e in t.listEdge:
                    badTriangleEdge.append(e)
        polygon = []
        
        for t in badTriangles :
            
            for e in t.listEdge :
                if badTriangleEdge.count(e)==1:
                    polygon.append(e)
        for e in polygon :
            triangulation.append(Triangle(e[0],e[1],p))
        

        for t in badTriangles:
            triangulation.pop(triangulation.index(t))

    

    for t in triangulation :
        if t.cote_commun(supT):
            triangulation.pop(triangulation.index(t))


    return triangulation



#genere une liste de voronoi prenant en paramètre la taille et le nombre de point
V=generate_voronoi(500,100)
print("la premiere cellule a ",len(V[0])," points")
print("il est représenté par :",V[0])



##si vous voulez representer avec tkinter
##fenetre =Tk()
##canvas = Canvas(fenetre,width=500, height=500, backgroun='grey')
##
##
##for v in range(len(V)):
##    for i in range(len(V[v])-1):
##
##        canvas.create_line(*V[v][i],*V[v][i+1])
##    canvas.create_line(*V[v][len(V[v])-1],*V[v][0])
##for v in range(len(V)):
##    if vp.count(v)==1:
##        print(v)
##        print("ok")
##        for i in range(len(V[v])-1):
##            canvas.create_line(*V[v][i],*V[v][i+1],fill="red")
##        canvas.create_line(*V[v][len(V[v])-1],*V[v][0],fill="red")
##canvas.pack()
##fenetre.mainloop()
