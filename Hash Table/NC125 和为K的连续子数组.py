# 腾讯CSIG测开面试题目
# 面经网址：https://www.nowcoder.com/discuss/722881?source_id=discuss_experience_nctrack&channel=-1
# 题目网址：https://www.nowcoder.com/practice/704c8388a82e42e58b7f5751ec943a11?tpId=117

# 题目描述
# 给定一个无序数组 arr , 其中元素可正、可负、可0。给定一个整数 k ，求 arr 所有连续子数组中累加和为k的最长连续子数组长度。保证至少存在一个合法的连续子数组。
# [1,2,3]的连续子数组有[1,2]，[2,3]，[1,2,3] ，但是[1,3]不是。
# 进阶：空间复杂度 O(n) ， 时间复杂度 O(n)

# max length of the subarray sum = k
# @param arr int整型一维数组 the array
# @param k int整型 target
# @return int整型
#
class Solution:
    # 重点在于dic的初始化
    # 官方思路如下：
    # 1.最关键的点在于累计和列表，这个累计和列表在后续中可以隐去，但是解决问题的关键在于考虑累计和列表。累计和列表即求到当前id下数组的和 s[i] = a[0]+a[1]+...a[i-1]
    # 2.那么任意的一个子数组都可以由累计和列表推出 s[j]-s[i] 想要满足子数组的和等于k 即满足s[j]-s[i]=k即可
    # 3.接下来就是求j-i最大就是最大的长度 引入哈希表，每个位置存储s[j]-k 这个值第一次出现（这样可以保证得到的长度是最长的）的位置 （也就是 值对应id）
    # 4.最后再遍历一遍累计和数组，每一个值就是s[j] 从哈希表中找到s[j]-k对应的id，找出最大的长度即可
    # 5.写的时候可以把累计和数组隐去，不需要实际构建出来，只要每次能获取到每个位置的累计和就可以了，把哈希表的存取放在同一个循环里，满足了复杂度的要求。
    def maxlenEqualK(self , arr: List[int], k: int) -> int:
        # 字典初始化为{0:-1}是为了涵盖数组中的最长子数组是从第一个元素就开始的情况
        dic = {0:-1}
        # ans存储最终长度结果，cur存储前i项和
        ans = cur = 0
        for i,v in enumerate(arr):
            cur += v
            ans = max(ans, i - dic.get(cur-k,i))
            dic[cur] = dic.get(cur,i)
        return ans