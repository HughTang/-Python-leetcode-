def jugde(case):
    ls = [0] * (len(case)//2+1)
    for line in case:
        t,e,s = line[0],line[1],line[2]
        if s == 0:
            ls[e] = t
        else:
            ls[e] = t - ls[e]
    return ls.index(max(ls))

if __name__ == '__main__':
    # 接收输入用例数量
    n = int(input())
    cases = []
    for _ in range(n):
        # 接收当前用例的行数
        rows = int(input())
        case = []
        for _ in range(rows):
            ls = []
            # 将每行存储在ls中，再将ls存放在case中
            for x in input().split():
                ls.append(int(x))
            case.append(ls)
        # 把当前case放入最终的cases中
        cases.append(case)
    # print(cases)
    for case in cases:
        print(jugde(case))
            


