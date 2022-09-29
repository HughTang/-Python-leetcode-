#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    # 解题方法：使用桶排序
    # 设置若干个桶，每个桶存储出现频率相同的数。把数都放到桶之后，
    # 从后向前遍历桶，最先得到的k个数就是出现频率最多的的k个数。
    # 时间复杂度为O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash中的key存储nums中的值，value存储nums中每个值出现的个数
        hash = dict()

        # frequent中的key存储nums中每个值出现的个数，
        # value存储nums中出现次数相同的值的列表，
        # frequent是通过遍历hash并反转键值位置而得到的。
        frequent = dict()
        
        # ans用于存储出现频率前k高的元素
        ans = list()

        # 遍历nums中的每个值，统计每个值出现的次数，构建hash字典
        for value in nums:
            if value in hash:
                hash[value] += 1
            else:
                hash[value] = int(1)
        
        # 遍历hash字典，将原有键值反转，存储在frequent中
        # 该部分也给出了一种如何通过值获取键的方法，即构建一个新的字典进行键值的反转即可，只不过每个键对应的值为一个列表
        for key,value in hash.items():
            if value in frequent:
                frequent[value].append(key)
            else:
                frequent[value] = [key]
        
        # 利用range从nums的长度（单个值可能出现的最大频率）开始反向遍历
        for x in range(len(nums),0,-1):
            # 如果该频率在frequent的键中，则将其对应的列表中的元素加入到ans中
            if x in frequent:
                for value in frequent[x]:
                    ans.append(value)
        
        # 返回ans列表中的前k个值
        return ans[0:k]
# @lc code=end

