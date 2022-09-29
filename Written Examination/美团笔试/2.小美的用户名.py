# 题目链接：https://www.nowcoder.com/questionTerminal/953d5a1426654a79923feba626ebf1a9

def is_digit(c):
    return ord('0') <= ord(c) <= ord('9')

def is_letter(c):
    return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')
    
def jugde(s: str):
    if len(s) <= 1:
        return 'Wrong'
    if not is_letter(s[0]):
        return 'Wrong'
    digit_flag = False
    for c in s:
        if is_digit(c):
            digit_flag = True
        if not (is_letter(c) or is_digit(c)):
            return 'Wrong'
    return 'Accept' if digit_flag else 'Wrong'
        

if __name__ == '__main__':
    n = int(input())
    ls = [input() for _ in range(n)]
    # print(ls)
    for s in ls:
        print(jugde(s))
