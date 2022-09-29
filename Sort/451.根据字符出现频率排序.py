#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    # 本题与「347. 前k个高频元素」的解题方法一致，都是使用桶排序，
    # 唯一有区别的就是最后两行代码，由于要保留所有的重复和非重复字符，
    # 所以需要在往ans列表中添加元素时元素与频率相乘，即c*i，最后利用
    # join()函数返回ans转换过后的字符串
    def frequencySort(self, s: str) -> str:
        hash = dict()
        fre = dict()
        ans = list()

        for c in s:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = int(1)
        
        for k,v in hash.items():
            if v in fre:
                fre[v].append(k)
            else:
                fre[v] = [k]
        
        for i in range(len(s),0,-1):
            if i in fre:
                for c in fre[i]:
                    # ans中需要加入对应频率的字符c
                    ans.append(c*i)
        # 使用join()函数将ans转化为字符串后返回
        return ''.join(ans)
# @lc code=end

