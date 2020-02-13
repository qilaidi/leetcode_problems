class Solution:
    def fib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

if __name__ == '__main__':
    test = Solution()
    print(test.fib(2)) #1
    print(test.fib(3)) #2
    print(test.fib(0)) #0
    print(test.fib(1)) #1
    print(test.fib(4)) #3
    print(test.fib(30))

