class Solution:
    def fib(self, N):
        a = [0, 1] + [None] * (N-1)
        for i in range(2, N+1):
            a[i] = a[i-2] + a[i-1]
        return a[N]

if __name__ == '__main__':
    test = Solution()
    print(test.fib(2))