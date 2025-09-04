def Neighbours(current):
    neighboursnodes=[]
    new=current[:]
    if(new[0][0]==0):
        new[0][0],new[1][0]=new[1][0],new[0][0]
        neighboursnodes.append(new)
        new[0][0],new[1][0]=new[1][0],new[0][0]
        new[0][0],new[0][1]=new[0][1],new[0][0]
        neighboursnodes.append(new)
    elif(new[0][1]==0):
        new[0][0],new[1][0]=new[1][0],new[0][0]
        neighboursnodes.append(new)
        new[0][0],new[1][0]=new[1][0],new[0][0]
        new[0][1],new[1][1]=new[1][1],new[0][1]
        neighboursnodes.append(new)
        new[0][1],new[1][1]=new[1][1],new[0][1]
        new[0][1],new[0][2]=new[0][2],new[0][1]
        neighboursnodes.append(new)
    elif(new[0][2]==0):
        new[0][1],new[0][2]=new[0][2],new[0][1]
        neighboursnodes.append(new)
        new[0][1],new[0][2]=new[0][2],new[0][1]
        new[0][2],new[1][2]=new[1][2],new[0][2]
        neighboursnodes.append(new)
    elif(new[1][0]==0):
        new[0][0],new[1][0]=new[1][0],new[0][0]
        neighboursnodes.append(new)
        new[0][0],new[1][0]=new[1][0],new[0][0]
        new[1][0],new[1][1]=new[1][1],new[1][0]
        neighboursnodes.append(new)
        new[1][0],new[1][1]=new[1][1],new[1][0]
        new[1][0],new[2][0]=new[2][0],new[1][0]
        neighboursnodes.append(new)
    elif(new[1][1]==0):
        new[1][1],new[1][0]=new[1][0],new[1][1]
        neighboursnodes.append(new)
        new[1][1],new[1][0]=new[1][0],new[1][1]
        new[1][1],new[1][2]=new[1][2],new[1][1]
        neighboursnodes.append(new)
        new[1][1],new[1][2]=new[1][2],new[1][1]
        new[1][1],new[0][1]=new[0][1],new[1][1]
        neighboursnodes.append(new)
        new[1][1],new[0][1]=new[0][1],new[1][1]
        new[1][1],new[2][1]=new[2][1],new[1][1]
        neighboursnodes.append(new)
    elif(new[1][2]==0):
        new[0][2],new[1][2]=new[1][2],new[0][2]
        neighboursnodes.append(new)
        new[0][2],new[1][2]=new[1][2],new[0][2]
        new[1][2],new[1][1]=new[1][1],new[1][2]
        neighboursnodes.append(new)
        new[1][2],new[1][1]=new[1][1],new[1][2]
        new[1][2],new[2][2]=new[2][2],new[1][2]
        neighboursnodes.append(new)
    elif(new[2][0]==0):
        new[2][0],new[1][0]=new[1][0],new[2][0]
        neighboursnodes.append(new)
        new[2][0],new[1][0]=new[1][0],new[2][0]
        new[2][0],new[2][1]=new[2][1],new[2][0]
        neighboursnodes.append(new)
    elif(new[2][1]==0):
        new[2][1],new[1][1]=new[1][1],new[2][1]
        neighboursnodes.append(new)
        new[2][1],new[1][1]=new[1][1],new[2][1]
        new[2][1],new[2][2]=new[2][2],new[2][1]
        neighboursnodes.append(new)
        new[2][1],new[2][2]=new[2][2],new[2][1]
        new[2][1],new[2][0]=new[2][0],new[2][1]
        neighboursnodes.append(new)
    else:
        new[2][1],new[2][2]=new[2][2],new[2][1]
        neighboursnodes.append(new)
        new[2][1],new[2][2]=new[2][2],new[2][1]
        new[2][2],new[1][2]=new[1][2],new[2][2]
        neighboursnodes.append(new)
    return neighboursnodes
def Solve(current,goal):
    explored=[]
    explored.append(current)
    g=0
    while(g<10):
        g+=1
        newnodes=Neighbours(current)
        count=[]
        for i in newnodes:
            c=0
            for k in range(3):
                for j in range(3):
                    if i[k][j]!=k+j+1:
                        c+=1
            if i[2][2]==0:
                c-=1
            count.append(c)
        min=count[0]
        index=0
        for i in range(1,len(count)):
            if(min<count[i]):
                min=count[i]
                index=i
        explored.append(newnodes[index])
        current=newnodes[index]
        print(current)
    for i in explored:
        print(i[0])
        print(i[1])
        print(i[2])
puzzle=[[int(input("The Current state of the Puzzle")) for i in range(3)] for j in range(3)]
Solve(puzzle,[[1,2,3],[4,5,6],[7,8,0]])
