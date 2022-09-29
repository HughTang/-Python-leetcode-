#
# lang=python3
#
# 2021年腾讯校招笔试题
# 
# 朋友圈
# 题目网址：https://www.nowcoder.com/practice/11ee0516a988421abf40b315a2b28d08?tab=note
#

# 方法一：DFS
# 该方法的运用是为了熟悉如何使用DFS计算无向邻接表中连通图中的最多顶点数
class Solution:
    # 此函数传入邻接表（字典），打印最终结果
    def friend_cycles(self, grid: dict) -> int:
        # 定义已访问集合
        visited = set()
        # 初始化最终结果为0
        max_ans = 0
        # 遍历邻接表的每个顶点
        for i in grid:
            # 如果该顶点未被访问，则进行DFS
            if i not in visited:
                max_ans = max(self.dfs(grid,i,visited), max_ans)
        print(max_ans)
    
    # DFS的实现（重点！！！）
    # 其功能在于统计顶点x所在的连通图的顶点总数
    def dfs(self,grid: dict, x: int, visited: set) -> int:
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


if __name__ == '__main__':
    # 接收测试用例组数
    n = int(input())
    for _ in range(n):
        # 接收关系对的数量
        relations = int(input())
        # 初始化邻接表为字典
        grid = dict()
        for _ in range(relations):
            # 接收每个关系对，并组建邻接表
            ls =  input().split()
            x, y = int(ls[0]), int(ls[1])
            if x in grid:
                grid[x].append(y)
            else:
                grid[x] = [y]
            if y in grid:
                grid[y].append(x)
            else:
                grid[y] = [x]
        # 对于每个测试用例，对其进行解答，并打印结果
        s = Solution()
        s.friend_cycles(grid)
        
