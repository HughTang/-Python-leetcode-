#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    # 按照BFS的编程策略进行编写即可。
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 获取二维数组的行长度和列长度 
        m, n = len(grid), len(grid[0])

        # 由于后面的步骤无法处理以下特殊情况，所以需要对其提前进行处理1
        # （1）gird不存在、grid中无元素、grid的左上角元素不为0，那么需要返回-1
        if not grid or m == n == 0 or grid[0][0] != 0:
            return -1
        # （2）grid的左上角元素为0且仅有这一个元素，那么需要返回1（其实由于前面已经判断过了grid[0][0]是否为0的情况，所以这里也可以只判断长度是否为1）
        # if m == n == 1:
        if grid[0][0] == 0 and m == n == 1:
            return 1
        
        # directions数组用于存储节点路径的八个方向，以供后面while循环中能够借助directions生成targets数组
        directions = ((1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))

        # 定义初始节点，其中存储初始节点的坐标和路径长度
        node = ((0, 0), 1)
        # 初始化队列
        queue = [node]
        # 初始化访问集合
        visited = {node[0]}
        
        # 对队列中的元素进行遍历
        while queue:
            # 出栈当前节点的坐标值index和路径长度step
            index, step = queue.pop(0)
            # 分别获取当前节点坐标值的横坐标x和纵坐标y
            x,y = index[0], index[1]
            # 定义targets数组
            targets = []
            # 利用directions中的八个方向来获取当前节点可以通过的路径节点
            for i,j in directions:
                # 判断该方向的节点坐标是否越界，以及该方向节点的值是否为0，只有满足上述条件的节点才能放入targets中
                if 0 <= x+i < m and 0 <= y+j < n and grid[x+i][y+j] == 0:
                    targets.append((x+i, y+j))
            # 遍历targets数组中的节点
            for target in targets:
                # 如果该节点恰好是右下角的节点，那么直接返回step+1
                if target[0] == m-1 and target[1] == n-1:
                    return step + 1
                # 如果该节点不是右下角的节点且未被访问过，那么将其加入queue和visited中
                if target not in visited:
                    queue.append((target, step+1))
                    visited.add(target)
        # 上面的循环没有满足条件的路径，返回-1
        return -1   
# @lc code=end

