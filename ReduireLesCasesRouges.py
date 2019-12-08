cmds.select(all=True)
cmds.delete()
import re
cmds.file(new=True,f=True)

cmds.shadingNode('lambert',asShader=True,name="sol")
cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name="solSG")
cmds.connectAttr('sol.outColor','solSG.surfaceShader')
cmds.setAttr("sol.color",1,0,0) 

cmds.shadingNode('lambert',asShader=True,name="bord")
cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name="bordSG")
cmds.connectAttr('bord.outColor','bordSG.surfaceShader')
cmds.setAttr("bord.color",0,0,1)


cmds.shadingNode('lambert',asShader=True,name="mur")
cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name="murSG")
cmds.connectAttr('mur.outColor','murSG.surfaceShader')
cmds.setAttr("mur.color",0,1,0)


cmds.shadingNode('lambert',asShader=True,name="pb")
cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name="pbSG")
cmds.connectAttr('pb.outColor','pbSG.surfaceShader')
cmds.setAttr("pb.color",1,0,1) 

for j in range(len(ListV)):
    l_points = ListV[j].l_points
    cmds.polyDisc(subdivisions=0,sides=len(l_points))
    cmds.rename("V"+str(j))
    for i in range(len(l_points)):
        pos=cmds.xform('V'+str(j)+'.vtx['+str(i)+']',q=True,t=True,ws=True)

        cmds.select('V'+str(j)+'.vtx['+str(i)+']')
    
        cmds.move(pos[0]-pos[0]-l_points[i][0],0.0,pos[2]-pos[2]-l_points[i][1])
    L=re.findall(r"[\w.-]+", cmds.polyInfo("V"+str(j), faceNormals=True)[0])
    if "-" in L[3]:
        cmds.polyNormal(name='V'+str(j)+'.f[0]',userNormalMode=1)
    if ListV[j].c==0:
        cmds.select('V'+str(j))
        cmds.sets(e=True,fe="solSG")
    if ListV[j].c==1:
        cmds.select('V'+str(j))
        cmds.sets(e=True,fe="murSG")
    if ListV[j].c==2:
        cmds.select('V'+str(j))
        cmds.sets(e=True,fe="bordSG")
    if ListV[j].c==3:
        cmds.select('V'+str(j))
        cmds.sets(e=True,fe="pbSG")
    cmds.xform(p=True)
    
for i in range(len(ListV)):
    cmds.select("V"+str(i))
    pos=cmds.xform('V'+str(i),q=True,t=True,ws=True)
    cmds.move(25,pos[1],25)
    cmds.xform(s=[0.001,1,0.001],p=True,cp=True)



























##Rescale des faces 




cmds.select(all=True)
cmds.polyUnite(n='MazeComb')

#il faut unir les objets pour que ca marche

cmds.delete(ch = True)

#supprime l'history

list = cmds.ls(sl=True)
for item in list:
    vtxCount = cmds.polyEvaluate(v=True)
    cmds.select(cl=True)
    cmds.select(item+'.vtx[0:'+str(vtxCount)+']', add=True)
    
cmds.polyMergeVertex( d=0.00001 )
cmds.select(cl=True)

#merge tt les vertex pour que le scale etire les autres cellules

materialName = 'sol'#nom du matos dans l'hypershade
shadingGroup = cmds.listConnections(materialName, type='shadingEngine')
print(shadingGroup)
componentsWithMaterial = cmds.sets(shadingGroup, q=True)
print(componentsWithMaterial)

#cree une liste de tts les faces avec le matos



for i in range(0,len(componentsWithMaterial)):
    Sel = cmds.select(componentsWithMaterial[i])
    #cmds.scale(0.5,0.5,0.5)
    #cmds.xform(Sel,cpc=True,ws=True)
    #MySelPos = cmds.xform(Sel,q=True,ws=True,piv=True)
    #print(MySelPos)
    #cmds.move(0.5,1,0.6)
    cmds.scale(0.1,0.1,0.1,r=True,componentSpace=True)
    
    ##rescale des faces par componenetr, c a d par arapport a la eurs propre centre de pivot
    
#for i in range(1,len(componentsWithMaterial)-1,2):
    #Sel = cmds.select(componentsWithMaterial[i],add=True)
    #cmds.scale(0.5,0.5,0.5)
    #cmds.xform(Sel,cpc=True,ws=True)
    #MySelPos = cmds.xform(Sel,q=True,ws=True,piv=True)
    #print(MySelPos)
    #cmds.move(0.5,1,0.6)    
    
    
    
    
    
    
    
    #pos = cmds.xform(componentsWithMaterial[i],q=True,t=True,ws=True)
    #cmds.xform(s=[0.001,1,0.001])
    #cmds.scale(0.98,0.98,0.98,r=True,componentSpace=True)
    
    #cmds.scaleComponents(10,0.1,0.5)
    #cmds.select(cl=True)
    
 
#for i in range(len(componentsWithMaterial)):
   #cmds.select(componentsWithMaterial[i])    
    #pos=cmds.xform(componentsWithMaterial[i],q=True,t=True,ws=True)
   # cmds.move(25,pos[1],25)
   # cmds.scale(0.9,0.5,0.5)
  
  
for i in range(0,len(componentsWithMaterial)):
    Sel = cmds.select(componentsWithMaterial[i])
    FaceSel = cmds.polyChipOff(dup=False)
    #cmds.move(0,1,0)
    
    #resepare les faces 
    
    #cmds.rename('Cel'+str(i+1))
    

cmds.select(all=True)
cmds.polySeparate()

    #cree des objets pour chaque face

'''cmds.delete(ch = True)

materialName = 'sol'
shadingGroup = cmds.listConnections(materialName, type='shadingEngine')
print(shadingGroup)
componentsWithMaterial = cmds.sets(shadingGroup, q=True)
print(componentsWithMaterial)



for i in range(0,len(componentsWithMaterial)):
    Sel = cmds.select(componentsWithMaterial[i])
    cmds.rename('Cel'+str(i+1))'''
    
  


'''for i in range(0,len(componentsWithMaterial)):
    cmds.select('polySurface'+str(i+1))'''
    


