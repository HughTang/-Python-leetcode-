/*
 * @lc app=leetcode.cn id=371 lang=java
 *
 * [371] 两整数之和
 */

// @lc code=start
/**
 *     本题不用Python编写的原因是因为python整数类型为Unifying Long Integers, 
 * 即无限长整数类型，没有办法保证一直循环左移而溢出，在递归条件中会出现错误结果，
 * 因此改为Java。
 *     本题思路在于a ^ b可以用于表示没有考虑进位的情况下两数的和，而(a & b) << 1就是进位。
 * 所以运用递归左移，递归会终止的原因是(a & b) << 1最右边会多一个0，那么继续递归，进位最
 * 右边的0会慢慢增多，最后进位会变为0，递归终止。
 */
class Solution {
    public int getSum(int a, int b) {
        return b == 0 ? a : getSum((a ^ b), (a & b) << 1);
    }
}
// @lc code=end

