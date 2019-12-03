from tkinter import *
from random import *
import copy
def creer_grille(n):
    graph={}
    for i in range(n):
        for j in range(n):
            nu = i*n+j

            graph[nu]=[i,j,False]
            if (i!=0):
                graph[nu].append((i-1)*n+j)

            else : graph[nu].append(-1)
            if (j!=(n-1)):
                graph[nu].append(nu+1)

            else : graph[nu].append(-1)
            if (i!=(n-1)):
                graph[nu].append((i+1)*n+j)

            else : graph[nu].append(-1)
            if (j!=0):

                graph[nu].append(nu-1)
            else : graph[nu].append(-1)
            graph[nu].append(nu)
    return(graph)




def gener_algo(murs,cellules,t):

    case=randint(0,len(cellules)-1)

    list_mur=[]
    maze=copy.deepcopy(murs)
    cellules[case][2]=True
    x=cellules[case][0]*2+1
    y=cellules[case][1]*2+1
    num=x*(t*2+1)+y

    ta=t*2+1
    if cellules[case][3]!=-1:
        list_mur.append([case,cellules[case][3],murs[num-ta]])
    if cellules[case][4]!=-1:
        list_mur.append([case,cellules[case][4],murs[num+1]])
    if cellules[case][5]!=-1:
        list_mur.append([case,cellules[case][5],murs[num+ta]])
    if cellules[case][6]!=-1:
        list_mur.append([case,cellules[case][6],murs[num-1]])

    while(list_mur!=[]):
        mur=choice(list_mur)
        if cellules[mur[0]][2]+ cellules[mur[1]][2] == 1:
           
            maze.pop(mur[2][-1])
            if cellules[mur[0]][2] == False:
                cellules[mur[0]][2] = True
                x=cellules[mur[0]][0]*2+1
                y=cellules[mur[0]][1]*2+1
                num=x*(ta)+y
                if cellules[mur[0]][3]!=-1:
                    list_mur.append([mur[0],cellules[mur[0]][3],murs[num-ta]])
                if cellules[mur[0]][4]!=-1:
                    list_mur.append([mur[0],cellules[mur[0]][4],murs[num+1]])
                if cellules[mur[0]][5]!=-1:
                    list_mur.append([mur[0],cellules[mur[0]][5],murs[num+ta]])
                if cellules[mur[0]][6]!=-1:
                    list_mur.append([mur[0],cellules[mur[0]][6],murs[num-1]])
            else :
                cellules[mur[1]][2] = True
                x=cellules[mur[1]][0]*2+1
                y=cellules[mur[1]][1]*2+1
                num=x*(ta)+y
                if cellules[mur[1]][3]!=-1:

                    list_mur.append([mur[1],cellules[mur[1]][3],murs[num-ta]])
                if cellules[mur[1]][4]!=-1:

                    list_mur.append([mur[1],cellules[mur[1]][4],murs[num+1]])
                if cellules[mur[1]][5]!=-1:

                    list_mur.append([mur[1],cellules[mur[1]][5],murs[num+ta]])
                if cellules[mur[1]][6]!=-1:

                    list_mur.append([mur[1],cellules[mur[1]][6],murs[num-1]])
        list_mur.remove(mur)
    return maze
        
def gener(ta,val):
    t=int(ta)
    for c in fenetre.winfo_children():
        c.destroy()

    taille=int(val)
    cellules=creer_grille(taille)
    murs=creer_grille((taille)*2+1)
    maze=gener_algo(murs,cellules,taille)
    canvas = Canvas(fenetre, width=(taille+1)*t,height= (taille+1)*t, background='yellow')
    mo=t/2
    for i in range(0,len(murs)):
        if i%2==0:
            maze.pop(i)
        if i in maze.keys():

            x=(maze[i][1])//2
            y=(maze[i][0])//2

            if maze[i][0]%2==0:


                canvas.create_line(mo+t*x,mo+t*y,mo+t*(x+1),mo+t*y)
                
            else :

                canvas.create_line(mo+x*t,mo+t*y,mo+x*t,mo+t*(y+1))
    canvas.pack()
    taill= StringVar()
    taill.set(ta)
    entree0= Entry(fenetre, textvariable=taill,width=3)

    value.set(val)
    entree = Entry(fenetre, textvariable=value, width=3)
    entree0.pack()
    entree.pack()
    bouton=Button(fenetre,text="Generer",command=lambda : gener(entree0.get(),entree.get()) )
    bouton.pack()
    fenetre.mainloop()
    
taille=10
cellules=creer_grille(taille)
print(cellules)
murs=creer_grille((taille)*2+1)

maze=gener_algo(murs,cellules,taille)
print(maze)
fenetre = Tk()
canvas = Canvas(fenetre, width=500,height= 500, background='yellow')



taill= StringVar()
taill.set("40")
entree0= Entry(fenetre, textvariable=taill,width=3)
value = StringVar() 
value.set("5")
entree = Entry(fenetre, textvariable=value, width=3)

bouton=Button(fenetre,text="Generer",command=lambda : gener(entree0.get(),entree.get()))
canvas.pack()
entree0.pack()
entree.pack()
bouton.pack()

fenetre.mainloop()

                
            

