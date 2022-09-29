#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
# 
# 本题是一道经典的「拓扑排序」问题，题解见「210.课程表-ii」，思路是一样的。
# 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 初始化逆邻接表
        graph = [[] for _ in range(numCourses)]
        # 初始化节点访问列表visit，0表示未访问，-1表示正在访问，1表示已访问
        visit = [0] * numCourses
        # 将每个节点及其前驱结点加入到graph中
        for x, y in prerequisites:
            graph[x].append(y)
        # 对每个未访问节点进行深度优先搜索
        for i in range(numCourses):
            if visit[i] == 0 and not self.dfs(i, visit, graph):
                return False
        # 返回结果栈ans
        return True

    # 深度优先搜索函数
    def dfs(self, i: int, visit: List[int], graph: List[List[int]]) -> bool:
        # 如果节点i的visit[i]的值为-1，即搜索中，则说明该有向图存在环，返回False
        if visit[i] == -1:
            return False
        # 如果节点i的visit[i]的值为1，即已搜索，则直接返回True
        elif visit[i] == 1:
            return True
        # 如果节点i的visit[i]的值为0，即未搜索，则将其状态改为-1，即搜索中
        visit[i] = -1
        # 对节点i的前驱结点列表进行递归遍历，如果在递归过程中出现环，则返回False
        for j in graph[i]:
            if not self.dfs(j, visit, graph):
                return False
        # 将当前节点i的visit[i]的值改为1，表示已搜索
        visit[i] = 1
        # 该轮深度优先搜索结束，返回True
        return True
# @lc code=end

