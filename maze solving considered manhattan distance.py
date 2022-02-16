#maze
m=[['#','#','#','#','#','#','#','#','B','#'],
['#','#','#','#',' ','#','#',' ',' ','#'],
['#','#',' ',' ',' ','#','#',' ','#','#'],
['#','#',' ','#','#','#','#',' ','#','#'],
['#','#',' ',' ',' ',' ',' ',' ','#','#'],
['#','#',' ','#','#','#','#','#','#','#'],
['#','#',' ','#','#','#','#','#','#','#'],
['#','#',' ',' ',' ',' ',' ',' ',' ','#'],
['#','#',' ','#','#','#','#','#','#','#'],
['#','#','A','#','#','#','#','#','#','#']]

#add another row
row=[]
for i in range(0,len(m[0])):
    row.append("#")
m.append(row)

#setting up the initial states
initial=[]
end=[]
frontier=[]
for i in range(0,len(m)):
    if "A" in m[i]:
        a=m[i].index("A")
        initial.append(i)
        initial.append(a)
    if "B" in m[i]:
        b=m[i].index("B")
        end.append(i)
        end.append(b)
frontier.append(initial)
prev={}

#manhattan distance
def manhattan(i):
    
    if end[0]>i[0]:
        v=end[0]-i[0]
    else:
        v=i[0]-end[0]
    
    if end[1]>i[1]:
        h=end[1]-i[1]
    else:
        h=i[1]-end[1]
    dist=h+v
    return dist

#explore
while True:
    #check above
    if (frontier[0][0]-1,frontier[0][1]) not in prev:
        if m[(frontier[0][0]-1)][frontier[0][1]] == " " or m[(frontier[0][0])-1][frontier[0][1]] == "B":
            a=(frontier[0][0])-1
            b=frontier[0][1]
            pos=[a,b]
            frontier.append(pos)
            prev[tuple(pos)]=frontier[0]
            if pos==end:
                break
    #check below
    if (frontier[0][0]+1,frontier[0][1]) not in prev:
        if m[(frontier[0][0])+1][frontier[0][1]] == " " or m[(frontier[0][0])+1][frontier[0][1]] == "B":
            a=(frontier[0][0])+1
            b=frontier[0][1]
            pos=[a,b]
            frontier.append(pos)
            prev[tuple(pos)]=frontier[0]
            if pos==end:
                break
    #check right
    if (frontier[0][0],frontier[0][1]+1) not in prev:
        if m[frontier[0][0]][(frontier[0][1])+1] == " " or m[frontier[0][0]][(frontier[0][1])+1] == "B":
            a=frontier[0][0]
            b=(frontier[0][1])+1
            pos=[a,b]
            frontier.append(pos)
            prev[tuple(pos)]=frontier[0]
            if pos==end:
                break
    #check left
    if (frontier[0][0],frontier[0][1]-1) not in prev:
        if m[frontier[0][0]][(frontier[0][1])-1] == " " or m[frontier[0][0]][(frontier[0][1])-1] == "B" :
            a=(frontier[0][0])
            b=(frontier[0][1])-1
            pos=[a,b]
            frontier.append(pos)
            prev[tuple(pos)]=frontier[0]
            if pos==end:
                break
    frontier.pop(0)
    
    if len(frontier)>1:
        dist=[]
        for i in frontier:
            dist.append(manhattan(i))
        for i in range(0,len(dist)-1):
            for j in range(0,len(dist)-1-i):
                if dist[j]>dist[j+1]:
                    dist[j],dist[j+1]=dist[j+1],dist[j]
                    frontier[j],frontier[j+1]=frontier[j+1],frontier[j]

#backtrack
frontier=[]
frontier.append(end)
while True:
    pos=prev[tuple(frontier[0])]
    if pos != initial:
        m[pos[0]][pos[1]]="."
        frontier.pop(0)
        frontier.append(pos)
    else:
        break

m.pop(-1)

#print
for i in m:
    for j in i:
        print(j,end="")
    print()
