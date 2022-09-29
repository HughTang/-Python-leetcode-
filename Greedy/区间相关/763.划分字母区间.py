#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    # 由于同一个字母只能出现在同一个片段，显然同一个字母的第一次出现的下标位置和最后一次出现的下标位置必须出现在同一个片段。因此需要遍历字符串，得到每个字母最后一次出现的下标位置。
    # 在得到每个字母最后一次出现的下标位置之后，可以使用贪心的方法将字符串划分为尽可能多的片段，具体做法如下。
    # 
    # (1)从左到右遍历字符串，遍历的同时维护last_seen字典用于存储每个字母的结尾下标。
    # (2)初始化result=[], max_last_seen=0，count=0。max_last_seen用于存储当前片段的最大结束下标，count统计片段的长度，每次遍历一个字母后都+1。
    # (3)再次从左到右遍历字符串，对于每个访问到的字母c，得到当前字母的最后一次出现的下标位置last_seen[c]，则取之前已访问字母的结束下标与当前元素的结束下标的最大值，即max_last_seen = max(max_last_seen, last_seen[c])，并使count+=1。
    # (4)当访问到下标i == max_last_seen时，当前片段访问结束，长度为count的值，将count添加到返回值，然后令count = 0，继续寻找下一个片段。
    # (5)重复上述过程，直到遍历完字符串。
    # 
    # 上述做法使用贪心的思想寻找每个片段可能的最小结束下标，因此可以保证每个片段的长度一定是符合要求的最短长度，如果取更短的片段，则一定会出现同一个字母出现在多个片段中的情况。由于每次取的片段都是符合要求的最短的片段，因此得到的片段数也是最多的。
    # 由于每个片段访问结束的标志是访问到下标max_last_seen，因此对于每个片段，可以保证当前片段中的每个字母都一定在当前片段中，不可能出现在其他片段，可以保证同一个字母只会出现在同一个片段。
    def partitionLabels(self, s: str) -> List[int]:
        result, last_seen, max_last_seen, count = [], {}, 0, 0
        for i,c in enumerate(s):
            last_seen[c] = i
        for i,c in enumerate(s):
            max_last_seen = max(max_last_seen, last_seen[c])
            count += 1
            if i == max_last_seen:
                result.append(count)
                count = 0
        return result
    
    
    # 方法二：个人解答思路，定义哈希表记录每个字母的开始和结束下标，
    # 然后对dict.values()按照每个字母的起始下标作为关键字进行升序排列，
    # 然后按照区间相关的贪心思路进行解题即可。
    def partitionLabels(self, s: str) -> List[int]:
        hash = dict()
        for i,c in enumerate(s):
            if c in hash:
                hash[c][1] = i
            else:
                hash[c] = [i, i]
        nums = sorted(hash.values(), key = lambda x: x[0])
        nums.append([float('inf'), float('inf')])
        ans = list()
        pre_min, pre_max = nums[0][0], nums[0][1]
        for i in range(1, len(nums)):
            if pre_max > nums[i][0]:
                pre_max = max(pre_max, nums[i][1])
            else:
                ans.append(pre_max-pre_min+1)
                pre_min, pre_max = nums[i][0], nums[i][1]
        return ans
# @lc code=end