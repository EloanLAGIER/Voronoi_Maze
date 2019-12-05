import re
cmds.file(new=True,f=True)
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
        cmds.move(0.0,-1,0.0)
    cmds.xform(p=True)
    
for i in range(len(ListV)):
    cmds.select("V"+str(i))
    pos=cmds.xform('V'+str(i),q=True,t=True,ws=True)
    cmds.move(25,pos[1],25)
    cmds.xform(s=[0.01,1,0.01],p=True,cp=True)

        


        
