
for c in g.dicCel.values():
    
    
    cmds.select('C'+str(c.index))
    if c.c==0:
        cmds.sets(e=True,fe="solSG")
        cmds.rename("Sol"+str(c.index))
    if c.c==1:
        cmds.sets(e=True,fe="murSG")
        cmds.rename("Mur"+str(c.index))

    if c.c==2:
        cmds.sets(e=True,fe="murSG")
        cmds.rename("Mur"+str(c.index))

    cmds.move(-25,0,-25)
    cmds.xform(s=[0.1,1,0.1],p=True,cp=True)
    




            ###debut des subdiv###

         
import maya.cmds as cmds
import random
HauteurDeMaison = 0.5
LongeurDeMaison = 0.2
LargeurDeMaison =0.2


ListeDsMurs =cmds.ls("Mur*")

#print(ListeDsMurs)

                    ##fonction qui definit la maison

def Maison():
    
    a = cmds.polyCube(w=LargeurDeMaison,h=HauteurDeMaison+random.uniform(0, 0.3),d=LongeurDeMaison,n=Maison)
    cmds.rename('Maison#')
    
                    ##Pour chaque case subdivise2fois 
    
for j in range(len(ListeDsMurs)):
    
    cmds.select(ListeDsMurs[j])
    
    list = cmds.ls(sl=True,fl = True)

    
    cmds.polySubdivideFacet(dvv=2)

                   ##deselectionne les vertices du bords et fait une liste de points
    #print(list)
    for item in list:
        vtxCount = cmds.polyEvaluate(v=True)
        #print(vtxCount)
        cmds.select(cl=True)
        cmds.select(item+'.vtx[0:'+str(vtxCount)+']', add=True)
        #cmds.polySelectConstraint(pp=6)
        mel.eval('PolySelectTraverse 2')
        pointsInternes = cmds.ls(selection = True , sn=True, fl = True)
        
                   ##Bouge chaque point selon un random et place une instance de maison

    #print(pointsInternes)

    for i in range(len(pointsInternes)):
        
        if len(pointsInternes) > 1:

    
            maSel = cmds.select(pointsInternes[i])
            cmds.move(random.uniform(0, 0.2) ,0,random.uniform(0, 0.2) ,r=True)
            posDesObjs = cmds.xform(maSel,q=True,ws=True, t=True)
            NvlMaison = Maison()
            #cmds.move(posDesObjs[0],posDesObjs[1],posDesObjs[2],'Maison'+str(i+1))    
            cmds.move(posDesObjs[0],posDesObjs[1]+HauteurDeMaison/2.0,posDesObjs[2])

#cmds.move

#materialName = 'sol'#nom du matos dans l'hypershade
#shadingGroup = cmds.listConnections(materialName, type='shadingEngine')
#print(shadingGroup)
#componentsWithMaterial = cmds.sets(shadingGroup, q=True)
#print(componentsWithMaterial)