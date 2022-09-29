#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    # 此题的关键在于广度优先搜索的基础上，进行建图优化，在构建targets列表时需要判断x是否已经在visited中，避免超时
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        node = (beginWord, 1)
        queue = [node]
        visited = {node[0]}

        while queue:
            s, step = queue.pop(0)
            # 这里必须加上对x是否在visited中的判断，不然会超时
            targets = [x for x in wordList if x not in visited and self.differ(s,x)]
            for target in targets:
                if target == endWord:
                    return step + 1 
                if target not in visited:
                    queue.append((target, step+1))
                    visited.add(target)
        return 0

    # 判断两个字符串是否只有一个字符不相同
    def differ(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return False
        res = 0
        for x, y in zip(str1,str2):
            if x != y:
                res += 1
        return res == 1
# @lc code=end

