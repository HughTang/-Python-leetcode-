#
# @lc app=leetcode.cn lang=python3
#
# 最大公约数和最小公倍数
#

# @lc code=start
class Solution:
    # 最大公约数的求解采用辗转相除法：两个整数的最大公约数等于其中较小的数和两数相除余数的最大公约数。
    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)
    
    # 最小公倍数为两数的乘积除以最大公约数
    def lcm(self, a: int, b: int) -> int:
        return a * b // self.gcd(a, b)