#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    # 方法一：回溯递归（推荐）
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],\
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],\
            '8':['t','u','v'], '9':['w','x','y','z']}
        ans = list()
        # digits不为空，则进入dfs回溯
        if digits:
            self.dfs(digits, '', ans)
        return ans
    
    def dfs(self, digits, tmp, ans):
        if len(digits) == 0:
            ans.append(tmp)
            return 0
        for x in self.dic[digits[0]]:
            self.dfs(digits[1:], tmp+x, ans)

    # 方法二：正向递归
    def letterCombinations(self, digits: str) -> List[str]:
        # 建立映射字典
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],\
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],\
            '8':['t','u','v'], '9':['w','x','y','z']}
        
        # 处理特殊情况
        if not digits or len(digits) == 0:
            return []
        
        # 递归出口
        if len(digits) == 1:
            return dic[digits]
        
        # 定义结果列表
        ans = []
        # 正向递归
        for x in dic[digits[0]]:
            for c in self.letterCombinations(digits[1:]):
                ans.append(x+c)
        return ans

    # 方法三：逆向递归
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],\
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],\
            '8':['t','u','v'], '9':['w','x','y','z']}
        
        if not digits or len(digits) == 0:
            return []
        if len(digits) == 1:
            return dic[digits]
        
        prev = self.letterCombinations(digits[:-1])
        tails = dic[digits[-1]]
        return [p + t for p in prev for t in tails]
# @lc code=end

