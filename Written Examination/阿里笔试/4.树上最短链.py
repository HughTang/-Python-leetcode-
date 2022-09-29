def dfs(node,visited,deep):
    global ans,level,tree,n,root
    if len(visited) == n and level[node] == level[root]:
        ans = min(deep, ans)
        return
    for x in tree[node]:
        if x not in visited:
            dfs(x, visited+[x], deep+1)

if __name__ == '__main__':
    n = int(input())
    level = [int(x) for x in input().split()]
    tree = {i:[] for i in range(n)}
    for _ in range(n-1):
        ls = input().split()
        x, y = int(ls[0]), int(ls[1])
        tree[x-1].append(y-1)
        tree[y-1].append(x-1)
    ans = float('inf')
    for node in tree:
        root = node
        dfs(node, [node], 0)
    if ans < float('inf'):
        print(ans)
    else:
        print(-1)

