from collections import deque,defaultdict
import math

A = int(input("Enter the quantity of Jug A : "))
B = int(input("Enter the quantity of Jug B : "))
goal = int(input("Enter the final quantity : "))

visited=defaultdict(lambda:False)

def solver(a1,a2):
  if(a1==goal and a2==0) or(a1==0 and a2==goal):
    print(f"Reached the goal state:({a1},{a2})")
    return True

  if not visited[(a1,a2)]:
    print(f"Step :({a1},{a2})")
    visited[(a1,a2)]=True

    return (
      solver(0,a2) or
      solver(a1,0) or
      solver(A,a2) or
      solver(a1,B) or
      solver(a1+min(a2,A-a1),a2-min(a2,A-a1)) or
      solver(a1-min(a1,B-a2),a2+min(a1,B-a2))
    )
  
  return False

print("\nSteps:")
if not solver(0, 0):
 print("No solution found.")


# if goal%math.gcd(A,B)!=0:
#   print("Cannot solve the problem")


# start=(0,0)

# visited=[]
# queue=deque()
# path=[]

# visited.append(start)
# queue.append((start,[start]))

# while queue:
#   state,path=queue.popleft()
#   a,b=state
#   if G in state:
#     print("Success")
#     for i in path:
#       print([i])
#     break

#   newstate=[]
#   newstate.append((A,b))
#   newstate.append((a,B))
#   newstate.append((0,b))
#   newstate.append((a,0))

#   m=min(a,B-b)
#   newstate.append((a-m,b+m))

#   m=min(A-a,b)
#   newstate.append((a+m,b-m))

#   for i in newstate:
#     if i not in visited:
#       visited.append(i)
#       queue.append((i,path+[i]))

