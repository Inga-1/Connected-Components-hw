def dfs(g, node):
    if node in visited:
        return
    visited.add(node)
    c.add(node + 1)
    for n in g[node]:
        dfs(g, n - 1)

def print_(s):
    st = ''
    for e in s:
        st += str(e) + ' '
    print(st)

inp = input()
inp = inp.split()
verts, edges = int(inp[0]), int(inp[1])

g = []
for _ in range(verts):
    g.append([])

for _ in range(edges):
    edge = input().split()
    vert1, vert2 = int(edge[0]), int(edge[1])
    g[vert1 - 1].append(vert2)
    g[vert2 - 1].append(vert1)

v = 0
visited = set()
c = set()

while True:
    if v < verts:
        if v in visited:
            v += 1
        else:
            dfs(g, v)
            print_(c)
            c = set()
            v += 1
    else:
        break