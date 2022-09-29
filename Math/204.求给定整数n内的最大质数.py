class Solution:
    def max_prime(self, n: int):
        for v in range(n,1,-1):
            if self.is_prime(v):
                return v
        return -1    

    def is_prime(self, m: int):
        sqrt = m**0.5 + 1
        for i in range(2,sqrt):
            if m % i == 0:
                return False
        return True