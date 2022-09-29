def judge(ls):
    # 将麻将牌放入字典中
    dic = {'T':[], 'B':[], 'W':[]}
    mjs = ls.split()
    for mj in mjs:
        dic[mj[1]].append(int(mj[0]))

    # 特殊情况：某个花色的牌大于三张则不符合条件
    for x in dic.values():
        if len(x) > 3:
            return 'NO'
    
    # 判断每种花色是否为隔3或者6
    for values in dic.values():
        if len(values) > 1:
            values.sort()
            for i in range(len(values)-1):
                if values[i+1] - values[i] != 3 and values[i+1] - values[i] != 6:
                    return 'NO'
    
    # 判断各种花色元素对3取模是否互相独立
    remainder = set()
    for values in dic.values():
        for v in values:
            remainder.add(v%3)
    if len(remainder) == 3:
        return 'YES'
    else:
        return 'NO'
                
if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        data.append(input())
    
    for ls in data:
        print(judge(ls))
    
    
