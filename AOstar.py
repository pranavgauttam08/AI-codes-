graph={'A':[['B', 'C'], ['D']],
       'B':[['G'], ['H']],
       'D':[['E','F']]}

node_cost={'B':6, 'C':12, 'D':10, 'E':4, 'F':4, 'G':5, 'H':7}

edge_cost=1

head_node='A'

def solve(currs):
  flag=0
  for curr in currs:
    if curr in graph.keys():
      flag=1

  if not flag:
    return 0

  min_cost=1000000
  for curr in currs:
    if curr in graph.keys():
      for path in graph[curr]:
        cost=0
        for node in path:
          cost=cost + node_cost[node]+edge_cost
          if min_cost>cost:
            min_cost=cost
            next_nodes=path
  print(f"{next_nodes}, {min_cost}")
  return [next_nodes, min_cost]


def driver():
  cost=0
  curr = head_node
  moves=0
  while True:
    for node in curr:
      result=solve(node)
      if not result:
        print(f"moves:{moves}")
        print(f"cost:{cost}")
        return cost
      cost += result[1]
      curr = result[0]
    moves += 1


if __name__=="__main__":
  driver()