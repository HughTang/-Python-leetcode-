# 题目链接：https://www.nowcoder.com/questionTerminal/a9980f73060545ca923344098750af18

# 方法一：BFS
# 花店到所有客户地址的距离之和是ans1，只需要将从节点1到所有节点的路径之和相加即可，通过BFS即可实现
# 骑手实际走的路程是ans2-max_path，即只需要将所有边的长度之和*2-从节点1到叶子结点的最长的一条路径长度即可
def BFS(node: int, path: int, dis: dict):
    global ans1, max_path
    ans1 += path
    if node not in dis:
        max_path = max(max_path, path)
    else:
        for n, p in dis[node]:
            BFS(n,path+p,dis)


if __name__ == '__main__':
    # 此处的ans1，ans2，max_path即为全局变量，不必再使用global声明
    ans1 = ans2 = max_path = 0
    n = int(input())
    dis = dict()
    for _ in range(n-1):
        start, end, p = [int(x) for x in input().split()]
        if start not in dis:
            dis[start] = [(end,p)]
        else:
            dis[start].append((end,p))
        ans2 += p * 2
    BFS(1,0,dis)
    print(ans1, ans2-max_path)


# 方法二：图的BFS
# 这里的BFS使用的是非递归方式，而且dis存储的是图的邻接表形式，适用范围更广
def BFS(node: int, path: int, dis: dict):
    global ans1, max_path
    queue = [(node,path)]
    visited = {node}
    while queue:
        nd, step = queue.pop(0)
        targets = [x for x in dis[nd]]
        for target in targets:
            if target[0] not in visited:
                max_path = max(max_path,target[1] + step)
                ans1 += target[1] + step
                visited.add(target[0])
                queue.append((target[0], target[1] + step))


if __name__ == '__main__':
    # 此处的ans1，ans2，max_path即为全局变量，不必再使用global声明
    ans1 = ans2 = max_path = 0
    n = int(input())
    dis = {i:[] for i in range(1,n+1)}
    for _ in range(n-1):
        start, end, p = [int(x) for x in input().split()]
        dis[start].append((end,p))
        dis[end].append((start,p))
        ans2 += p * 2
    BFS(1,0,dis)
    print(ans1, ans2-max_path)



# 方法三：动态规划
# 根据题设，考虑树状结构。求：
# sum1：从花店到所有客户地址的距离之和;
# sum2：骑手实际走的最短路程，且最后一趟不需再返回。

# 求sum1：
# 根据输入的u、v、w，对于任意节点都能写出dp[v]=dp[u]+w，从而得到sum1为sum(dp)。

# 求sum2：
# 要求最短路径，根据最后一趟不需返回，可知最后一趟一定是从花店到最远的客户地址处，这部分距离只需计算一次，其余的到其他客户地址的距离需要计算往返路程。因此sum2+=2×w，还要-maxlen，其中maxlen是dp中的最大值。
if __name__ == '__main__':
    paths = 0
    n = int(input())
    dp = [0] * (n + 1)
    for _ in range(n-1):
        start, end, path = [int(x) for x in input().split()]
        dp[end] = dp[start] + path
        paths += path * 2
    print(sum(dp), paths - max(dp))