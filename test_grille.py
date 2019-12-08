from random import *
import re
cmds.file(new=True,f=True)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
class Mur:
    def __init__(self,cm,c1,c2):
        self.cm=cm
        self.c1=c1
        self.c2=c2
        
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
    visit=0
    def __init__(self,i):
        self.index=i
    def l_points(self):
        return [[self.p2.x,self.p2.y],[self.p1.x,self.p1.y],[self.p3.x,self.p3.y],[self.p4.x,self.p4.y]]
        
class Grille :
    dicCel={}
    l_che=[]
    dicMur={}

    def __init__(self,n,a):
        t=n/a
        b=t/4
        print(t)
        print(b)
        for j in range(a):
            for i in range(a):
                c=Cellule(j*a+i)
                if (j==0) or (i==0) or (j==a-1) or (i==a-1):
                    c.c=3
                else:
                    if (j%2==0):
                        
                        if (i%2==0):
                            c.c=2
                        else:
                            c.c=1
                            c1=(j-1)*a+i
                            c2=(j+1)*a+i
                            m=Mur(c,c1,c2)
                            if c1 in self.dicMur:
                                self.dicMur[c1].append(m)
                            else:
                                self.dicMur[c1]=[m]
                            if c2 in self.dicMur:
                                self.dicMur[c2].append(m)
                            else:
                                self.dicMur[c2]=[m]
                    else:
                        if (i%2==0):
                            c.c=1
                            c1=(j)*a+i-1
                            c2=(j)*a+i+1
                            m=Mur(c,c1,c2)
                            if c1 in self.dicMur:
                                self.dicMur[c1].append(m)
                            else:
                                self.dicMur[c1]=[m]
                            if c2 in self.dicMur:
                                self.dicMur[c2].append(m)
                            else:
                                self.dicMur[c2]=[m]
                        else:
                            c.c=0
                            self.l_che.append(c)
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
    def maze(self):
        l_mur=[]
        c=choice(self.l_che)
        c.visit=1
        l_mur+=self.dicMur[c.index]
        while l_mur!=[]:
            m=choice(l_mur)
            if self.dicCel[m.c1].visit+self.dicCel[m.c2].visit==1:
                m.cm.c=0
                if self.dicCel[m.c1].visit==0:
                    self.dicCel[m.c1].visit=1
                    for i in self.dicMur[m.c1]:
                        if not(i in l_mur):
                            l_mur.append(i)
                else:
                    self.dicCel[m.c2].visit=1
                    for i in self.dicMur[m.c2]:
                        if not(i in l_mur):
                            l_mur.append(i)
            l_mur.pop(l_mur.index(m))
                 
                 
          

                    
cmds.shadingNode('lambert',asShader=True,name="sol")
cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name="solSG")
cmds.connectAttr('sol.outColor','solSG.surfaceShader')
cmds.setAttr("sol.color",1,0,0) 

cmds.shadingNode('lambert',asShader=True,name="poto")
cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name="potoSG")
cmds.connectAttr('poto.outColor','potoSG.surfaceShader')
cmds.setAttr("poto.color",1,0,1)


cmds.shadingNode('lambert',asShader=True,name="mur")
cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name="murSG")
cmds.connectAttr('mur.outColor','murSG.surfaceShader')
cmds.setAttr("mur.color",0,1,0)


g=Grille(500,101)
g.maze()
for c in g.dicCel.values():
    l_point=c.l_points()
    cmds.polyPlane(sh=1,sw=1);
    cmds.rename("C"+str(c.index))
    for i in range(len(l_point)):
        pos=cmds.xform('C'+str(c.index)+'.vtx['+str(i)+']',q=True,t=True,ws=True)
        cmds.select('C'+str(c.index)+'.vtx['+str(i)+']')
        cmds.move(l_point[i][0],0.0,l_point[i][1])
    cmds.select('C'+str(c.index))
    if c.c==0:
        cmds.sets(e=True,fe="solSG")
    if c.c==1:
        cmds.sets(e=True,fe="murSG")
    if c.c==2:
        cmds.sets(e=True,fe="murSG")
    cmds.move(-25,0,-25)
    cmds.xform(s=[0.1,1,0.1],p=True,cp=True)
    
