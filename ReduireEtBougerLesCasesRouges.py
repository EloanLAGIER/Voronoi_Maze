import random





















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
    cmds.scale(0.6,0.6,0.6,r=True,componentSpace=True)
    cmds.move(random.uniform(0, 0.2) ,0,random.uniform(0, 0.2) ,r=True)
    
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
    


