#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    # 无向图邻接矩阵的DFS
    #  城市关系可以看成是一个无向图，例如第0个城市与第1个城市是直接相连，那么isConnected[0][1]和isConnected[1][0]的值都为1。
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # （1）处理不符合条件的特殊情况
        if not isConnected:
            return 0
        
        # （2）初始化visited集合与结果ans值
        visited = set()
        ans = 0
        
        # （3）对每个城市所指示的直接相连列表进行遍历（即遍历每个嵌入列表）
        for i in range(len(isConnected)):
            # 如果城市i未被遍历过，那么以城市i所指示的直接相连列表进行DFS
            if i not in visited:
                # DFS，分别传入二维列表、城市i、visited记录集合
                self.dfs(isConnected, i, visited)
                # 省份数量+1
                ans += 1
        # （4）返回最终结果
        return ans
    
    # 递归DFS遍历邻接矩阵
    def dfs(self, isConnected: List[List[int]], row: int, visited: set):
        # 将当前遍历的城市row加入visited集合中
        visited.add(row)
        # 对当前遍历的城市row所指示的直接相连列表进行遍历
        for i,v in enumerate(isConnected[row]):
            # 如果找到与城市row直接相连且未加入visited中的城市，那么对其进行DFS递归
            if v == 1 and i not in visited:
                self.dfs(isConnected, i, visited)
# @lc code=end

