# 第二题，输入n个1或-1，求子序列乘积为1的序列个数
if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]
    # sums[i]表示nums前i的乘积和
    sums = [nums[0]] + [0] * (n-1)
    ans = 0
    for i in range(1,n):
        sums[i] = sums[i-1] * nums[i]
        for j in range(i):
            if sums[i]//sums[j] == 1:
                ans += 1
    ans += sums.count(1)
    print(ans)