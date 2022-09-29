def judge(idx):
    global n,formal,now,m,full,reduce
    sum_formal = sum(formal[:idx+1])
    x = sum(now[:idx+1])
    l, r = -1, m
    while l + 1 < r:
        mid = l + (r-l) // 2
        if full[mid] <= sum_formal:
            l = mid
        else: 
            r = mid
    y = sum_formal - reduce[l] if l != -1 else sum_formal
    print(x,y)
    # 折扣划算
    if x < y:
        return 'Z'
    # 满减划算
    elif x > y:
        return 'M'
    # 折扣与满减相同
    else:
        return 'B'


if __name__ == '__main__':
    # 商品数量
    n = int(input())
    # 原价
    formal = [int(x) for x in input().split()]
    # 折扣价
    now = [int(x) for x in input().split()]
    # 满减条目数量
    m = int(input())
    # 满
    full = [int(x) for x in input().split()]
    # 减
    reduce = [int(x) for x in input().split()]
    ans = ''
    for i in range(n):
        ans += judge(i)
    print(ans)