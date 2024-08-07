#maze
m=[
    ['#','#','#','#','#','#','#','#','B','#'],
    ['#','#','#','#',' ','#','#',' ',' ','#'],
    ['#','#',' ',' ',' ','#','#',' ','#','#'],
    ['#','#',' ','#','#','#','#',' ','#','#'],
    ['#','#',' ',' ',' ',' ',' ',' ','#','#'],
    ['#','#',' ','#','#','#','#','#','#','#'],
    ['#','#',' ','#','#','#','#','#','#','#'],
    ['#','#',' ',' ',' ',' ',' ',' ',' ','#'],
    ['#','#',' ','#','#','#','#','#','#','#'],
    ['#','#','A','#','#','#','#','#','#','#']
]

#add another row
row=[]
for i in range(0,len(m[0])):
    row.append("#")
m.append(row)

#setting up the initial states
initial=()
end=()
frontier=[]
for i in range(0,len(m)):
    if "A" in m[i]:
        a=m[i].index("A")
        initial=(i,a)
    if "B" in m[i]:
        b=m[i].index("B")
        end=(i,b)

frontier.append(initial)

path={}

#explore
while True:
    #check above
    current=frontier[0]
    if (current[0]-1,current[1]) not in path:
        if m[current[0]-1][current[1]] == " " or m[(current[0])-1][current[1]] == "B":
            a=(current[0])-1
            b=current[1]
            pos=(a,b)
            frontier.append(pos)
            path[pos]=current
            if pos==end:
                break
    #check below
    if (current[0]+1,current[1]) not in path:
        if m[current[0]+1][current[1]] == " " or m[current[0]+1][current[1]] == "B":
            a=(current[0])+1
            b=current[1]
            pos=(a,b)
            frontier.append(pos)
            path[pos]=current
            if pos==end:
                break
    #check right
    if (current[0],current[1]+1) not in path:
        if m[current[0]][(current[1])+1] == " " or m[current[0]][(current[1])+1] == "B":
            a=current[0]
            b=(current[1])+1
            pos=(a,b)
            frontier.append(pos)
            path[pos]=current
            if pos==end:
                break
    #check left
    if (current[0],current[1]-1) not in path:
        if m[current[0]][(current[1])-1] == " " or m[current[0]][(current[1])-1] == "B" :
            a=(current[0])
            b=(current[1])-1
            pos=(a,b)
            frontier.append(pos)
            path[pos]=current
            if pos==end:
                break
    frontier.pop(0)


#backtrack
current=end
while True:
    pos=path[current]
    if pos != initial:
        m[pos[0]][pos[1]]="."
        current=pos
    else:
        break

m.pop(-1)

#print
for i in m:
    for j in i:
        print(j,end="")
    print()
