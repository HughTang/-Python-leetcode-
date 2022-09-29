if __name__ == '__main__':
    n = int(input())
    things = []
    ans = []
    for _ in range(n):
        motion = [int(x) for x in input().split()]
        if motion[0] == 2:
            if not things:
                ans.append('no reliquaries.')
            else:
                ans.append(things.pop(0))
        else:
            things.append([motion[1], motion[2]])
    for x in ans:
        if x != 'no reliquaries.':
            print(x[0], x[1])
        else:
            print(x)
