#
# lang=python3
#
# 2021年腾讯校招笔试题
# 
# 朋友圈
# 题目网址：https://www.nowcoder.com/practice/11ee0516a988421abf40b315a2b28d08?tab=note
#

# 并查集
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


if __name__ == '__main__':
    # 接收测试用例组数
    n = int(input())
    for _ in range(n):
        # 接收关系对的数量
        relations = int(input())
        # 初始化邻接表为字典
        grid = list()
        dataset = set()
        for _ in range(relations):
            # 接收每个关系对，并组建邻接表
            ls =  input().split()
            x, y = int(ls[0]), int(ls[1])
            dataset.add(x)
            dataset.add(y)
            grid.append((x,y))
        # 对于每个测试用例，对其进行解答，并打印结果
        s = UnionFindSet()
        s.uf(dataset)
        for x,y in grid:
            s.union(x, y)
        print(max(s.size.values()))