#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    # zip()与zip_longest()的使用方法
    # zip(list1,list2)：当list1与list2长度不一致时，zip和较短的保持一致。
    # zip_longest(list1,list2)：当list1与list2长度不一致时，zip_longest和较长的保持一致。此外，还可以使用fillvalue参数来指定长度短的列表的缺失值。
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1,v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue = 0):
            x, y = int(v1), int(v2)
            if x != y:
                return 1 if x > y else -1
        return 0
# @lc code=end

