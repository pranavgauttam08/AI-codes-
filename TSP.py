dst=[]
def travel(g, v, pos, n, count, cost):
    if(count==n and g[pos][s]):
        cost+=g[pos][s]
        dst.append(cost)
        return
    for i in range(0,n):
        if(v[i]==False and g[pos][i]):
            v[i]=True
            travel(g,v,i,n,count+1,cost+g[pos][i])
            v[i]=False
n=4
g=[[0, 10, 15, 20],[10, 0, 35, 25],[15, 35, 0, 30],[20, 25, 30, 0]]
s=int(input("Enter a number between 1 and 4: "))
v=[False for i in range(0,n)]
s-=1
v[s]=True
travel(g,v,s,n,1,0)
print(dst)
print(min(dst))