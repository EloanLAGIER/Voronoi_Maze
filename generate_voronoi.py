from random import *
from math import *
from copy import *
import sys
sys.setrecursionlimit(50000)


def distance(p1,p2,dist):
    return sqrt(pow((p1[0]-p2[0]),2)+pow((p1[1]-p2[1]),2))<dist
def random_point(taille,np,dist,l=[]):
    print(np)
    Li=l[::]
    if np==0:
        return True,l
    
    for i in range(3):
        drap=True
        x=randint(dist,taille-dist)
        y=randint(dist,taille-dist)
        print(len(l))
        for p in range(len(Li)):
            if distance(Li[p],[x,y],dist):
                drap=False
                break
        if drap==True:
            Li.append([x,y])
            b,L=random_point(taille,np-1,dist,Li)
            if b==True:
                return b,L
            


#fonction principale( taille = dimension du carrÃƒÂ© gÃƒÂ©nÃƒÂ©ral et n nombre de cellules de voronoi )
def generate_voronoi(taille,n,dist):
    

    


    #generation des points aleatoire (encore trÃƒÂ¨s simple )
    print("generation des points")
    b,ListPoint=random_point(taille,n,dist)
    print("done")
    #fonction renvoyant les triangles de la triangulation des points
    print("generation triangulation")
    listTri=BowyerWatson(taille,ListPoint)
    print("done")
    #fonction renvoyant les cellules de voronoi
    print("génération voronoi")
    lVor=voronoi(ListPoint,listTri)
    
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

def box(seg):
    x1=seg[0][0]
    x2=seg[1][0]
    y1=seg[0][1]
    y2=seg[1][1]
    if x1<x2:
        xb1=x1
        xb2=x2
    else:
        xb1=x2
        xb2=x1
    if y1<y2:
        yb1=y1
        yb2=y2
    else:
        yb1=y2
        yb2=y1
    return([xb1,yb1,xb2,yb2])
    
def bool_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return True

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    b=box(line1)
    if (b[0]<=x)and(x<=b[2])and(b[1]<=y)and(y<=b[3]):
        return False
    else: 
        return True

##def convex(V):
##    L=V.l_points
##    LSeg=[]
##    for i in range(len(L)-1):
##        LSeg.append([L[i],L[(i+1)%len(L)]])
##    for i in range(len(LSeg)):
##        for j in range(len(LSeg)):
##            if i!=j:
##                if not(bool_intersection(LSeg[i],LSeg[j])):
##                    return False
##    return True

    
#fonction faite par moi calculant la mediane mais du coup mdr c'est n'importequoi
def mediane(p1,p2):
    x1=p1[0]
    x2=p2[0]
    y1=p1[1]
    y2=p2[1]
    div=y1-y2

    #genre ÃƒÂ§a c'est de la triche, euler se suicide
    if div==0:
        div=0.1
    mil=[(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
    p1y= (pow(x1,2) - pow(x2,2) + pow(y1,2) - pow(y2,2))/(2*(div))
    return [mil,[0,p1y]]

#instancede l'objet triangle qui va beaucoup servir
class Triangle :

    #ÃƒÂ§a c'est la fonction qui s'active quand on crÃƒÂ©er une instance
    def __init__(self,point1,point2,point3):

        #les trois points du triangle p1,p2,p3
        self.p1=point1
        self.p2=point2
        self.p3=point3

        self.listVorV=[]
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

    def voro_vois(self,v):
        if not(v in self.listVorV):
            self.listVorV.append(v)

    #fonction qui pour un point p regarde si il est dans le cercle Circoncis
    def est_dans_cercle(self,p):
              return (sqrt(pow(p[0]-self.centre[0],2)+pow(p[1]-self.centre[1],2))<self.rayon)

    #fonction qui regarde si un point p est dans le triangle
    def a_le_point(self,p):
        return self.p1==p or self.p2==p or self.p3==p

    #fonction qui regarde si un triangle t a un cotÃƒÂ© commun
    def cote_commun(self,t):
        return (t.seg1==self.seg1)or(t.seg1==self.seg2)or(t.seg1==self.seg3)or(t.seg2==self.seg1)or(t.seg2==self.seg2)or(t.seg2==self.seg3)or(t.seg3==self.seg1)or(t.seg3==self.seg2)or(t.seg3==self.seg3)

    #fonction qui regarde si un triangle t a un point commun
    def point_commun(self,t):
        return (t.p1==self.p1)or(t.p1==self.p2)or(t.p1==self.p3)or(t.p2==self.p1)or(t.p2==self.p3)or(t.p2==self.p3)or(t.p3==self.p1)or(t.p3==self.p2)or(t.seg3==self.p3)

#en faite quand on compare les segments des fois c'est les meme mais dans l'autre sens alors le programme comprend pas
#du coup j'ai crÃƒÂ©e une fonction qui tri toujours les sgmens dans le meme sens voila voila
def trier_edge(x1,y1,x2,y2):
    calc1=x1*500+y1
    calc2=x2*500+y2
    if calc1<calc2:
        return [[x1,y1],[x2,y2]]
    else:
        return [[x2,y2],[x1,y1]]

class Vor :
    def __init__(self,centre,nb_cote):

        self.centre=centre
        self.nb_cote=nb_cote
        self.c=-1
        self.l_points=[]
        self.l_mur=[]
        self.l_vois=[]
        self.l_mv=[]
    def add_vert(self,c):
        self.l_points.append(c)
    def add_vois(self,v):
        if not(v in self.l_vois):
            self.l_vois.append(v)
    def add_mur(self,v):
        self.l_mur.append(v)
    def add_mv(self,v):
        self.l_mv.append(v)


         
#fonction qui crÃ©Ã© le voronoi sa complexitÃ© est de O^3 c'est affreux
def voronoi(lp, lt):
    ListVor=[]
    incr=0
    lpb=[]
    for p in lp:
        print(str(lp.index(p))+"/"+str(len(lp)))
        incr+=1
        L=[]

        for t in lt:

            if t.a_le_point(p):
                L.append(t)
        LT=L[::]
        V=Vor(p,len(L))
        if len(L)==2:
           a="nothing" 
        elif len(L)==3:
            V.add_vert(L[0].centre)
            V.add_vert(L[1].centre)
            V.add_vert(L[2].centre)
        else:
            t_act=L[0]
            t_suiv=L[1]
            V.add_vert(t_act.centre)
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
                V.add_vert(t_suiv.centre)
                L.pop(L.index(t_act))
                t_act=t_suiv
                if len(L)>1:
                    r=randint(0,len(L)-1)
                    while (r==L.index(t_act)):
                        r=randint(0,len(L)-1)
                    t_suiv=L[r]
        b=True
        
        if b:
            for i in range(len(LT)-1):
                LT[i].voro_vois(V)

            ListVor.append(V)

    for t in lt:
        if len(t.listVorV)==2:
            v1=t.listVorV[0]
            v2=t.listVorV[1]
            v1.add_vois(v2)
            v2.add_vois(v1)
        if len(t.listVorV)==3:
            v1=t.listVorV[0]
            v2=t.listVorV[1]
            v3=t.listVorV[2]
            v1.add_vois(v2)
            v1.add_vois(v3)
            v2.add_vois(v1)
            v2.add_vois(v3)
            v3.add_vois(v2)
            v3.add_vois(v1)
    for v in ListVor:
        if len(v.l_vois)!=v.nb_cote:
            for v2 in v.l_vois:
                v2.c= 2
            ListVor.pop(ListVor.index(v))
    print(lpb)
    return ListVor


#la triangulation a une complexitÃƒÂ© de O^2 mais askip on peut la faire en O*ln(0)
#faut la nettoyer et cheker comment les cas particuliers possible
def BowyerWatson(taille,lp):
    triangulation=[]
    L=[[-taille,-10],[2*taille,-20],[taille/2,2*taille]]
    supT=Triangle(*L)

    triangulation.append(supT)
    for p in lp:
        print(str(lp.index(p))+"/"+str(len(lp)))
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

class Mur:
    def __init__(self,vm,v1,v2):
        self.vm=vm
        self.v1=v1
        self.v2=v2


def coloriser(lv):

    for v in lv:

        if v.c==-1:
            drap=True
            for vo in v.l_vois:
                if vo.c==0:
                    drap=False
                    break
            if drap==True:
                v.c=0
                for vo in v.l_vois:
                    if vo.c==-1:
                        for vi in vo.l_vois:
                            if (vi.c==0) and (vi!=v) and not(vi in v.l_mv):
                                vo.c=1
                                m=Mur(vo,v,vi)
                                v.add_mur(m)
                                v.add_mv(vi)
                                vi.add_mur(m)
                                vi.add_mv(v)
                                break

                
#genere une liste de voronoi prenant en paramÃƒÂ¨tre la taille et le nombre de point
ListV=generate_voronoi(50000,200,30)
coloriser(ListV)
print(len(ListV))
print("good")
