## 判断图是否联通
```python
def dfs(graph, visited, v):
    visited[v] = 0
    for x in graph[v]:
        if visited[x] == 1:
            dfs(graph, visited, x)

def jugde(graph):
    global n
    visited = [1] * n
    # 随机选择一个点进行DFS，这里选择标号为0的点
    dfs(graph, visited, 0)
    if sum(visited) > 0:
        return False
    return True
```

```python
def jugde(graph):
    global n
    queue = [0]
    visited = {0}
    while queue:
        node = queue.pop(0)
        targets = [x for x in graph[node]]
        for target in targets:
            if target not in visited:
                visited.add(target)
                queue.append(target)
    if len(visited) != n:
        return False
    return True
```