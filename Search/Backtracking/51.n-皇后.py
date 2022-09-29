#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start

class Solution:
    # 定义queens为由'Q'所在的纵坐标组成的列表，那么当queens的长度等于n时，
    # 即皇后的数量等于n时，就能找到解。在这个问题中，当一个位置(x, y)被'Q'占用时，
    # 任何其他位置(row, col)的row + col == x + y或row - col == x - y都是无效的。
    # 我们可以使用这个信息来跟踪无效位置的列表(xy_diff和xy_sum)，然后只对有效位置递归地调用DFS。
    # 最后，我们转换结果ans中的每个符合要求的queens列表下标，将其转换成所需的字符串格式。
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化保存符合要求queens的结果列表
        ans = []
        # DFS传入n，ans，queens（空），xy_diff（空），xy_sum（空）
        self.dfs(n, ans, [], [], [])
        # 转化为字符串列表的格式
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in path] for path in ans]
    
    # DFS回溯递归
    def dfs(self, n: int, ans: List[List[int]], queens: List[int], xy_diff: List[int], xy_sum: List[int]):
        # 这里的row取queens的长度，是因为其既代表了当前行坐标，又代表了已放置皇后的个数
        row = len(queens)
        # 当已放置皇后的个数等于n时，则将当前queens列表加入结果下标列表ans中
        if row == n:
            ans.append(queens)
            return 
        # 对纵坐标进行遍历
        for col in range(n):
            # 如果纵坐标col不在queens中，且行列的差值及和都不在相应列表中，则进行DFS递归
            if col not in queens and row-col not in xy_diff and row+col not in xy_sum:
                # 将符合要求的col加入queens中，行列的差值及和也加入到相应列表中
                self.dfs(n, ans, queens+[col], xy_diff+[row-col], xy_sum+[row+col])
# @lc code=end

