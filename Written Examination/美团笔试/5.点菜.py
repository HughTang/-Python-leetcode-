def dfs(customs, res, visited):
    global ans
    if not customs:
        ans = max(ans, res)
        return
    for i in range(len(customs)):
        if customs[i][0] != customs[i][1] and customs[i][0] not in visited and customs[i][1] not in visited:
            dfs(customs[i+1:], res+1, visited+[customs[i][0],customs[i][1]])



# 点菜
if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    customs = []
    for _ in range(n):
        x,y = input().split()
        customs.append((x,y))
    ans = 0
    print(customs)
    dfs(customs, 0, [])
    print(ans)