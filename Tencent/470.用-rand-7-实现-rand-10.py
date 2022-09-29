#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    # 该类问题的核心：(randX() - 1)*Y + randY() 可以等概率的生成[1, X * Y]范围的随机数。
    # 若已知randX()，求randY()。分为以下三种情况：
    # （1）如果X>Y且X是Y的倍数，那么只需要利用randX() % Y + 1即可获得randY()； 
    # （2）如果X>Y但X不是Y的倍数，那么就需要找到[1,X]中的某个值N作为基准点，使得N是Y的倍数，那么就可以舍弃(N,X]区间的值，获取randN()的实现方法，这个过程又被称为拒绝采样。然后，①若N==Y，则直接可以获取randY()；②若N>Y，则利用randN() % Y + 1即可获得randY()。
    # （3）如果X<Y，那么利用(randX()-1) * X + randX()获取randX²()的实现方法，然后对其拒绝采样获得基准点N，就变成了第（2）种情况进行处理。
    # 注：由于拒绝采样所丢弃的区间范围越大，程序得到预期结果所需要的时间就越长，因此，由于拒绝采样区间(N,Y]的数值生成都是等概率的，所以可以对其进行二次处理，即(rand(Y-N]() - 1) * X + randX()，然后再进行拒绝采样，使得最终丢弃的区间范围越来越小。
    # 参考网址：https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/cong-zui-ji-chu-de-jiang-qi-ru-he-zuo-dao-jun-yun-/
    # 
    # 方法一：未进行拒绝采样
    def rand10(self):
        """
        :rtype: int
        """
        # num的等概率值可取范围为[1,49]
        num = (rand7() - 1) * 7 + rand7()
        while num > 10:
            num = (rand7() - 1) * 7 + rand7()
        return num

    # 方法二：拒绝采样一次
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7() - 1) * 7 + rand7()
        # 由于40是10的倍数，且最接近右边界值49，所以将40作为拒绝采样的基准值
        while num > 40:
            num = (rand7() - 1) * 7 + rand7()
        return num % 10 + 1

    # 方法三：拒绝采样三次
    def rand10(self):
        """
        :rtype: int
        """
        # while True循环放置在最前面
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1
            
            # 进行第二次拒绝采样
            # num的等概率值可取范围变为[1,9]
            num = num - 40
            # num的等概率值可取范围变为[1,63]
            num = (num - 1) * 7 + rand7()
            # 选择60作为基准值
            if num <= 60:
                return num % 10 + 1

            # 进行第三次拒绝采样
            # num的等概率值可取范围变为[1,3]
            num = num - 60
            # num的等概率值可取范围变为[1,21]
            num = (num - 1) * 7 + rand7()
            # 选择60作为基准值
            if num <= 20:
                return num % 10 + 1
# @lc code=end

