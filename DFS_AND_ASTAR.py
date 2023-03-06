import random


print("DFS\n")

#Creating the 6 by 6 maze
X=6
Y=6

maze = []
for i in range(0, Y):
    line = []
    for j in range(0, X):
        line.append(0)
    maze.append(line)

#initializing starting point and End point
Starting_point=5
Goal_point=9

#Randomly Selecting a position for start point and end point
Start_colum=random.randint(0,1)
Start_row=random.randint(0,5)
Goal_column=random.randint(4,5)
Goal_row=random.randint(0,5)

#insitialzing Starting point and end point to randomply selected position
maze[Start_row][Start_colum]=Starting_point
maze[Goal_row][Goal_column]=Goal_point
position=(Start_row,Start_colum)
wall_count=0

#Creating wall
while wall_count<4:
    wall_row = random.randint(0,5)
    wall_colum=random.randint(0,5)

#Check if the position is a already a wall or staring point or end point
    if(maze[wall_row][wall_colum]==5)or maze[wall_row][wall_colum]==9 or maze[wall_row][wall_colum]==1:
      continue
    maze[wall_row][wall_colum] = 1
    wall_count+=1

for i in maze:
    print(i)


#Function for moves in DFS
def move(A,B,maze):

    next_move=[]#storing every move to this Stack
    if A-1>=0 and maze[A-1][B]!=1:
        next_move.append((A-1,B))

    if A+1<len(maze) and maze[A+1][B]!=1:
        next_move.append((A + 1, B))

    if B+1<len(maze) and maze[A][B+1]!=1:
        next_move.append((A, B+1))

    if B-1>=0 and maze[A][B-1]!=1:
        next_move.append((A, B-1))

    if (A-1>=0 and B-1>=0)and(maze[A-1][B-1]!=1):
        next_move.append((A-1, B-1))

    if (A+1<len(maze)and B+1<len(maze))and(maze[A + 1][B + 1] != 1):
        next_move.append((A+1, B+1))

    if (A+1<len(maze)and B-1>=0)and(maze[A + 1][B - 1] != 1):
        next_move.append((A+1, B-1))

    if (A-1>=0and B+1<len(maze))and(maze[A -1][B + 1] != 1):
        next_move.append((A-1, B+1))

    return next_move


#Fucktion for DFS
def DFS(maze,stack,visited):
    #Initialzing Starting position and End point for varialbes
    start=(Start_row,Start_colum)
    Goal=(Goal_row,Goal_column)
    stack.append(start)#append above positon to the Stack
    while stack:
        n= stack.pop()
        print("Popping",n)#popping the positon that on top of the stack

        if n==Goal:#Checks if the popped item is  the goal positiion
            print("Goal found")
            print("This is the Final path",visited)
            Total_Node=len(visited)
            print("The time taken to find the goal is",Total_Node,"minutes")
            return
#initialzing index num 1 and 2 to A,B
        A=n[0]
        B=n[1]
        next_steps = move(A,B, maze)
        print("Next Steps is",next_steps)
        for x in next_steps:
            if x in visited:
                print(x," is already visited, skipping...")#If that positiion is in Visited list skip that node
                print("\n")
                continue
            visited.add(x)
            stack.append(x)
            print("Visited nodes:",visited)
            print("Stack",stack)
stack=[]
visited=set()

move(Start_row,Start_colum,maze)
DFS(maze,stack,visited)




print("************************************************************************************************************************************************")

print("Astar search")


def Heuristc_Cost_Calculater():
    GR=Goal_row
    GC=Goal_column
    global heuristic_Values
    heuristic_Values={}

    for row in range(0, 6):
        for colum in range(0, 6):
            Position = ((GR - row, GC - colum))
            Chebyshev_Distance = max(Position)
            heuristic_Values[row,colum]=abs(Chebyshev_Distance)


    print("These are the heuristic Value",heuristic_Values)


Heuristc_Cost_Calculater()

def move(A,B,maze):
    next_minimum_move ={}  # storing every move to this Stack
    if A - 1 >= 0 and maze[A - 1][B] != 1:
        Heuristic_cost=heuristic_Values.get((A-1,B))
        F_cost=Heuristic_cost+1
        next_minimum_move[(A-1,B)]=F_cost
    if B + 1 < len(maze) and maze[A][B + 1] != 1:
        Heuristic_cost = heuristic_Values.get((A , B+1))
        F_cost = Heuristic_cost + 1

        next_minimum_move[(A , B+1)] = F_cost
    if A + 1 < len(maze) and maze[A + 1][B] != 1:
            Heuristic_cost = heuristic_Values.get((A + 1, B))
            F_cost = Heuristic_cost + 1
            next_minimum_move[(A + 1, B)] = F_cost

    if B - 1 >= 0 and maze[A][B - 1] != 1:
        Heuristic_cost = heuristic_Values.get((A, B-1))
        F_cost = Heuristic_cost + 1
        next_minimum_move[(A, B-1)] = F_cost

    if (A - 1 >= 0 and B - 1 >= 0) and (maze[A - 1][B - 1] != 1):
        Heuristic_cost = heuristic_Values.get((A - 1, B - 1))
        F_cost = Heuristic_cost + 1
        next_minimum_move[(A - 1, B - 1)] = F_cost

    if (A + 1 < len(maze) and B + 1 < len(maze)) and (maze[A + 1][B + 1] != 1):
        Heuristic_cost = heuristic_Values.get((A + 1, B + 1))
        F_cost = Heuristic_cost + 1
        next_minimum_move[(A + 1, B + 1)] = F_cost

    if (A + 1 < len(maze) and B - 1 >= 0) and (maze[A + 1][B - 1] != 1):
        Heuristic_cost = heuristic_Values.get((A + 1, B - 1))
        F_cost = Heuristic_cost + 1
        next_minimum_move[(A + 1, B - 1)] = F_cost

    if (A - 1 >= 0 and B + 1 < len(maze)) and (maze[A - 1][B + 1] != 1):
        Heuristic_cost = heuristic_Values.get((A - 1, B + 1))
        F_cost = Heuristic_cost + 1
        next_minimum_move[(A - 1, B + 1)] = F_cost

    minimum_path=min(next_minimum_move,key=next_minimum_move.get)

    return minimum_path


def AStarSearch(maze,stack,visited):
    start = (Start_row, Start_colum)
    Goal = (Goal_row, Goal_column)
    stack.append(start)
    while stack:
        n = stack.pop()
        print("Popping", n)
        if n==Goal:#Checks if the popped item is  the goal positiion
            print("Goal found")
            print("This is the Final path",visited)
            Total_Node=len(visited)
            print("The time taken to find the goal is",Total_Node,"minutes")
            return
        A=n[0]
        B=n[1]
        next_steps = move(A,B, maze)
        print("Next minimum path is ", next_steps)
        visited.add(next_steps)
        stack.append(next_steps)
        print("Visited nodes:", visited)
        print("Stack", stack)

stack=[]
visited=set()

move(Start_row,Start_colum,maze)
AStarSearch(maze,stack,visited)