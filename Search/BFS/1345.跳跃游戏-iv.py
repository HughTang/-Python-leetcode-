#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    # 解题思路：题目要求很容易理解，根据某位置可以跳到的位置，两者之间相当于可以连通，故整个问题可以看做为一个无向图的中节点间的最短路径问题
    # 求无向图两点间的最短路径可以用BFS来解，时间复杂度为O(V+E)，其中V为图的顶点数，E为图的边数
    # 本题中，V显然等于arr的长度n,但是E可能达到n^2的复杂度(比如，数组中值全部是相等的元素，每个位置都可与其他所有位置直接连通)
    # 这点是本题的一个坑(也是设置为困难的地方)，用普通的BFS解题是完全正确的，不过在该题中会超时(你可以自己试试咯)
    # 超时的主要原因就是，普通的BFS搜索时 相同值之间构成的子图的所有边都会访问一次，但其实没必要
    # 因为第一次访问到这个子图中的某个节点时，即会将这个子图的所有其他未在队列中的节点都放入队列
    # 在第二次访问到这个子图中的节点时，就不需要去考虑这个子图中的其他节点了，因为所有其他节点都已经在队列中或者已经被访问过了
    # 所有处理方法就是，将相同值的节点提前放在一个哈希表(字典)中，在第一次遇到该值时就把所有节点都进队，并清空该值构成的列表，就不会重复访问该子图的其他边了
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # 长度为1，直接返回0
        if n == 1:
            return 0
        # 用来存相同值的字典，键为该值，值为该值对应的所有下标组成的列表
        dic = defaultdict(list)
        for i,v in enumerate(arr):
            dic[v].append(i)
        
        # BFS模板
        # 初始时，起点下标和已经跳的步数都为0
        node = (0,0)
        # queue使用普通的list会超时，所以这里选择用deque()
        queue = deque()
        queue.append(node)
        visited = {node[0]}
        while queue:
            idx, step = queue.popleft()
            targets = []
            # 先等值跳
            for i in dic[arr[idx]]:
                if i != idx:
                    targets.append(i)
            # 清空该值对应的下标列表
            # del dic[arr[idx]]
            dic[arr[idx]] = []
            
            # 往左跳
            if idx-1 >= 0:
                targets.append(idx-1)
            
            # 往右跳
            if idx+1 < n:
                targets.append(idx+1)
            
            # targets中的值的判断
            for target in targets:
                if target == n-1:
                    return step + 1
                if target not in visited:
                    visited.add(target)
                    queue.append((target, step+1))
