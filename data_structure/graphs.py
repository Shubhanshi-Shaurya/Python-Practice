from collections import defaultdict,deque
graph = defaultdict(list)
n = int(input("Enter number of vertices: "))

for _ in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input(f"Enter neighbors of {vertex}: ").split()
    graph[vertex] = neighbors

print("\nGraph:")
print(dict(graph))

def bfs(graph,start):
  visited=[]
  queue=deque()
  visited.append(start)
  queue.append(start)
  while queue:
    n=queue.popleft()
    print(n)
    for neighbor in graph[n]:
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)

start=input("Enter the starting node for BFS : ")
print("\nBFS of the graph from A node :")
bfs(graph,start)