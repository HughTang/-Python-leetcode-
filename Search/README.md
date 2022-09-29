## 搜索（Search）

### 1、BFS（Breadth First Search）
#### （1）BFS的含义及举例
##### 含义：广度优先搜索一层一层地进行遍历，每层遍历都是以上一层遍历的结果作为起点，遍历一个距离能访问到的所有节点。需要注意的是，遍历过的节点不能再次被遍历。
##### 举例说明：对于下图给定的无权图，若采用BFS的遍历方式，那么，
![avator](https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/95903878-725b-4ed9-bded-bc4aae0792a9.jpg)

##### 第一层：
> 0 -> {6,2,1,5}

##### 第二层:
> 6 -> {4}

> 2 -> {}

> 1 -> {}

> 5 -> {3}
##### 第三层：
> 4 -> {}

> 3 -> {}

#### （2） BFS的适用场景
##### 每一层遍历的节点都与根节点距离相同。设 di 表示第 i 个节点与根节点的距离，推导出一个结论：对于先遍历的节点 i 与后遍历的节点 j，有 di <= dj。
##### 利用这个结论，可以求解最短路径等 最优解 问题：第一次遍历到目的节点，其所经过的路径为最短路径。
##### 应该注意的是，使用 BFS 只能求解 无权图 的最短路径，无权图是指从一个节点到另一个节点的代价都记为 1。

#### （3）在程序实现 BFS 时需要考虑的问题
- 队列queue：用来存储每一轮遍历得到的节点，广度优先搜索一层一层遍历，每一层得到的所有新节点，要用队列存储起来以备下一层遍历的时候再遍历。
- 标记visited：对于遍历过的节点，应该将它标记，防止重复遍历。

#### （4）BFS问题的编程策略
```python
    # 初始化节点，前面的n为初始节点的值，后面的0为step，可以理解为步骤或者到达路径长度
    node = (n, 0)
    # 初始化队列
    queue = [node]
    # 初始化已访问集合，避免队列中插入重复的值
    visited = {node[0]}

    while queue:
        # 弹出队首节点
        value, step = queue.pop(0)
        # 对弹出的节点进行操作（以279.完全平方数为例）
        targets = [value-i*i for i in range(1, int(value**0.5+1))]
        # 判断一堆节点是否符合业务条件，若符合，则return；若不符合，且不在已访问集合，则追加到队尾，并加入已访问集合
        for target in targets:
            if target == 0:
                return step + 1
            if target not in visited:
                queue.append((target,step+1))
                visited.add(target)
    # 若以上遍历完成仍未return，返回-1
    return -1
```
> 参考网址：https://leetcode-cn.com/problems/perfect-squares/solution/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/

---
### 2、DFS（Breadth First Search）
#### （1）DFS的含义及举例
##### 含义：深度优先遍历主要思路是从图中一个未访问的顶点 V 开始，沿着一条路一直走到底，然后从这条路尽头的节点回退到上一个节点，再从另一条路开始走到底…，不断递归重复此过程，直到所有的顶点都遍历完成，它的特点是不撞南墙不回头，先走完一条路，再换一条路继续走。而且每个节点只能访问一次。
##### 举例说明：对于下图给定的无权图，若采用DFS的遍历方式，那么，
![avator](https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/74dc31eb-6baa-47ea-ab1c-d27a0ca35093.png)
##### 深度优先搜索在得到一个新节点时立即对新节点进行遍历：从节点 0 出发开始遍历，得到到新节点 6 时，立马对新节点 6 进行遍历，得到新节点 4；如此反复以这种方式遍历新节点，直到没有新节点了，此时返回。返回到根节点 0 的情况是，继续对根节点 0 进行遍历，得到新节点 2，然后继续以上步骤。

#### （2）DFS的适用场景
##### 从一个节点出发，使用 DFS 对一个图进行遍历时，能够遍历到的节点都是从初始节点可达的，DFS 常用来求解这种 可达性 问题。

#### （3）在程序实现 DFS 时需要考虑的问题
- 栈stack：用栈来保存当前节点信息，当遍历新节点返回时能够继续遍历当前节点。可以使用递归栈。
- 标记visited：和 BFS 一样同样需要对已经遍历过的节点进行标记。
#### （4）DFS问题的编程策略
##### ①当数据结构为邻接表时
```python
    # 只需要简单遍历连通图的所有顶点并标记时 
    def dfs(self, grid: dict, x: int, visited: set) -> int:
        # 将当前顶点加入visited中
        visited.add(x)
        # 遍历当前顶点所指示的列表
        for v in grid[x]:
            # 如果顶点v未被访问过，则进行DFS
            if v not in visited:
                self.dfs(grid,v,visited)
```

```python
    # 需要统计某个连通图的所有顶点个数时
    def dfs(self, grid: dict, x: int, visited: set) -> int:
        # 将当前顶点加入visited中
        visited.add(x)
        # 重点1：初始化ans为1
        ans = 1
        # 遍历当前顶点所指示的列表
        for v in grid[x]:
            # 如果顶点v未被访问过，则进行DFS，并且递增ans
            if v not in visited:
                ans += self.dfs(grid,v,visited)
        # 返回最终结果
        return ans

```

##### ②当数据结构为邻接矩阵时
```python
    # 只需要简单遍历连通图的所有顶点并标记时
    def dfs(self, isConnected: List[List[int]], row: int, visited: set):
        # 将当前遍历的顶点row加入visited集合中
        visited.add(row)
        # 对当前遍历的顶点row所指示的直接相连列表进行遍历
        for i,v in enumerate(isConnected[row]):
            # 如果找到与顶点row直接相连且未加入visited中的顶点，那么对其进行DFS递归
            if v == 1 and i not in visited:
                self.dfs(isConnected, i, visited)
```

> 参考网址：https://leetcode-cn.com/problems/clone-graph/solution/zhan-fei-di-gui-dfs-xin-shou-jiao-cheng-by-zi-lai-/

#### （5）DFS题目分类
##### 二维矩阵中的元素相邻：
- 200.岛屿数量
- 695.岛屿的最大面积
##### 二维矩阵中需要从边界开始处理：
- 130.被围绕的区域
- 417.太平洋大西洋水流问题
##### 图的邻接矩阵/邻接表/UnionFind：
- 547.省份数量
- 朋友圈

---
### 3、在解决二维矩阵搜索的问题时，BFS与DFS适用场景的比较
- 如果只是要**找到某一个结果是否存在（可达性）**，那么**DFS更高效**。因为DFS会首先把一种可能的情况尝试到底，才会回溯去尝试下一种情况，只要找到一种情况，就可以返回了。但是BFS必须所有可能的情况同时尝试，在找到一种满足条件的结果的同时，也尝试了很多不必要的路径；
- 如果是要**找所有可能路径中的最短路径**，那么**BFS更高效**。因为DFS是一种一种的尝试，在把所有可能情况尝试完之前，无法确定哪个是最短，所以DFS必须把所有情况都找一遍，才能确定最终答案（DFS的优化就是剪枝，不剪枝很容易超时）。而BFS从一开始就是尝试所有情况，所以只要找到第一个达到的那个点，那就是最短的路径，可以直接返回了，其他情况都可以省略了，所以这种情况下，BFS更高效。


---
### 4、Backtracking
#### （1）解题思路
##### 回溯一般采用DFS递归的方法，DFS中的重要参数是ans，path和idx，其中ans是最终的结果列表，path用于保存递归路径的实时结果，idx一般用于存储递归深度。如果搜索的对象是二维矩阵，一般还需要定义visited二维数组（79.单词搜索）。如果是组合类题目，一般还需要将idx改为start参数，用于标识上一层递归的初始下标值，如果能够重复组合，则传入i（39.组合总和）；不能重复组合，则传入i+1（77.组合）。如果是子集类题目，其解法与求解组合类题目类似，只是需要保留每层递归的所有path实时路径结果，然后再判断递归出口。
#### （2）关于回溯中的剪枝操作（目的是对相同路径或组合结果去重）
以「40.组合总和-ii」为例，该问题旨在对candidates中找寻和为target的不同组合方案，其中candidates中存在重复数字且每个数字在每个组合中只能使用一次。
![avator](https://pic.leetcode-cn.com/1599718525-iXEiiy-image.png)
![avator](https://pic.leetcode-cn.com/1599716342-gGiISM-image.png)
数组candidates有序是深度优先遍历过程中实现「剪枝」的前提，因此需要先对candidates进行升序排序，**重复的元素一定不是排好序以后相同的连续数组区域的第1个元素**。也就是说，**剪枝发生在：同一层数值相同的结点第2、3 ... 个结点，因为数值相同的第1个结点已经搜索出了包含了这个数值的全部结果，同一层的其它结点，候选数的个数更少，搜索出的结果一定不会比第1个结点更多，并且是第1个结点的真子集**。
> 参考题解：https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/

#### （3）题目分类
##### 字符串等的单向回溯
- 17.电话号码的字母组合
- 93.复原IP地址
- 剑指offer 38.字符串的排列
- 46.数字的全排列
- 47.数字的全排列-ii（存在重复数字，需要提前排序，再在DFS循环中加if语句判断数字是否重复，本质上是剪枝+回溯）
##### 二维矩阵回溯
- 79.单词搜索
##### 二叉树回溯
- 257.二叉树的所有路径
##### 组合回溯
- 77.组合
- 39.组合总和
- 40.组合总和-ii（存在重复数字，需要提前排序，再在DFS循环中加if语句判断数字是否重复，本质上是剪枝+回溯）
- 216.组合总和-iii
##### 子集回溯（本质上是组合）
- 78.子集
- 90.子集-ii
##### 分割回文串（本质上是单向回溯）
- 131.分割回文串（本题与93.复原IP地址类似）
##### 其他
- 37.解数独（python中内置函数any的使用）
- 51.N皇后（同一元素的45度线有无该某元素的判断方式为row-col==x-y，row+col==x+y）

---
### 5、UnionFind
#### （1）并查集的含义及举例
- 并查集(Disjoint-Set)是一种可以动态维护若干个不重叠的集合，并支持合并与查询两种操作的一种数据结构。

#### （2）并查集的适用场景
- DFS的替代方案，例如「130.被围绕的区域」，**二维坐标 (x,y) 可以转换成 x * n + y 这个数（m 是行数，n 是列数）。这是将二维坐标映射到一维的常用技巧**。
- 判定合法等式
##### 使用 Union-Find 算法，主要是如何把原问题转化成图的动态连通性问题。对于算式合法性问题，可以直接利用等价关系，对于棋盘包围问题，则是利用一个虚拟节点，营造出动态连通特性。

#### （3）并查集的编程策略
##### 在并查集的初始化过程中，可以使用字典存储，也可以使用列表存储，所传入的参数不同：
- 当使用字典存储并查集时，需要传入所有顶点的集合
```python
class UnionFindSet(object):
    def __init__(self):
        # 初始化parent字典，保存每个节点的父节点
        self.parent = {}
        # 初始化parent字典，保存每个节点所在连通分量的节点总数
        self.size = {}
        # 初始化size，保存并查集中连通分量的总个数
        self.num = 0
    
    # 初始化并查集，参数dataset的数据类型为集合
    def uf(self, dataset: set):
        # 初始阶段，每个节点的父节点就是其本身，且每个节点所在连通分量的节点总数初始为1，则并查集中连通分量的总个数为传入的dataset的长度
        self.num = len(dataset)
        for v in dataset:
            self.parent[v] = v
            self.size[v] = 1
    
    # 查询节点x所在连通分量的根节点
    def find(self, x):
        # 一直循环，直到找到某个节点的父节点为本身时才停止，那么此时所找到的即为根节点
        while self.parent[x] != x:
            # 为了使find函数能够以O(1)的时间复杂度找到某一节点的根节点，下面的一行属于进一步压缩每棵树的高度，使树高始终保持为常数
            self.parent[x] = self.parent[self.parent[x]]
            # 将parent[x]赋值为x，继续进行下次循环或跳出循环时保证x为根节点的值
            x = self.parent[x]
        # 返回根节点
        return x

    # 合并节点x与节点y所在的连通分量
    def union(self, x, y):
        # 获取两个节点的根节点
        x_root = self.find(x)
        y_root = self.find(y)
        # 如果两个根节点相同，说明x和y处于同一个连通分量中，不做处理，直接返回
        if x_root == y_root:
            return

        # 如果两个根节点不同，说明x和y处于两个不同连通分量中，需要对两个连通分量进行合并
        # 节点少的连通分量（小树）接到节点多的连通分量（大树）下面，保持树的高度平衡
        if self.size[x_root] > self.size[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        else:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        
        # 两个连通分量合并成一个连通分量，因此并查集中连通分量的总个数减一
        self.num -= 1

    # 判断节点x与节点y是否处在同一个连通分量中
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    # 返回并查集中的连通分量总数
    def count(self):
        return self.num
```

- 当使用列表存储并查集时，需要传入顶点集合中的最大值
```python
class UnionFindSet(object):
    def __init__(self):
        # 初始化parent列表，保存每个节点的父节点
        self.parent = []
        # 初始化parent列表，保存每个节点所在连通分量的节点总数
        self.size = []
        # 初始化size，保存并查集中连通分量的总个数
        self.num = 0
    
    # 初始化并查集，参数dataset的数据类型为集合
    def uf(self, n):
        # 初始阶段，每个节点的父节点就是其本身，且每个节点所在连通分量的节点总数初始为1
        self.num = n
        # 注意此处为n+1，是为了能够保存最大的节点，防止越界
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)
    
    # 其他的方法与字典存储时相同
    .......
```
并查集参考网址1：https://labuladong.gitee.io/algo/2/19/37/
并查集参考网址2：https://labuladong.gitee.io/algo/2/19/38/