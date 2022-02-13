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
for i in range(0,10):
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
            if (frontier[0][0]+1,frontier[0][1]) in prev:
                print("trueeee")
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
            a=(frontier[0][0])-1
            b=(frontier[0][1])-1
            pos=[a,b]
            frontier.append(pos)
            prev[tuple(pos)]=frontier[0]
            if pos==end:
                break
    frontier.pop(0)


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


#print
for i in m:
    for j in i:
        print(j,end="")
    print()
