#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
#
# 并查集（Union-Find Set）：https://zhuanlan.zhihu.com/p/93647900
#
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 初始化并查集，其中的每个元素为相应下标节点所属集合的代表节点，初始时每个元素所属集合的代表结点为本身
        parent = list(range(len(edges)+1))
        # 查询并返回给定元素所属集合的代表节点
        def find(index: int) -> int:
            # 如果代表结点为本身，则直接返回；否则，递归查询代表结点
            if parent[index] == index:
                return index
            else:
                return find(parent[index])
        
        # 合并两个元素所属集合的代表结点：这里把index1所属集合的代表结点改为index2所属集合的代表结点
        def union(index1: int, index2: int) -> None:
            parent[find(index1)] = find(index2)
        
        for x, y in edges:
            # 如果两个元素所属集合的代表结点不相同，则将两个集合合并
            if find(x) != find(y):
                union(x,y)
            # 如果两个元素所属集合的代表结点相同，说明无向图存在环，返回该边
            else:
                return [x,y]
        # 无环则返回空列表
        return []
# @lc code=end

