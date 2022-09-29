if __name__ == '__main__':
    n = int(input())
    results = []
    for _ in range(n):
        length = int(input())
        p1 = input().split()
        p2 = input().split()
        if p1 == p2:
            results.append(0)
            continue
        ans1 = 0
        for i in range(length):
            tmp = p1[i+1:] + p1[:i+1]
            ans1 += 1
            if tmp == p2:
                break
        ans2 = 0
        for i in range(length):
            tmp = p2[i+1:] + p2[:i+1]
            ans2 += 1
            if tmp == p1:
                break
        results.append(min(ans1,ans2))
    for x in results:
        print(x)