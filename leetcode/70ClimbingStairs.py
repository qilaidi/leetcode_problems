from functools import lru_cache

from leetcode_problems.utils.timer import timethis


class Solution1:
    @lru_cache(None)
    @timethis
    def climbStairs_fool_recursive(self, n):
        """recursive"""
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    @timethis
    def climbStairs(self, n):
        a, b, res = 1, 2, 0
        if n <= 2:
            return n
        for i in range(3, n + 1):
            res = a + b
            a, b = b, res
        return res

    @timethis
    @lru_cache(None)
    def climbStairs_3_recursive(self, n):
        """1, 2, 3步的情况"""
        if n < 3:
            return n
        elif n == 3:
            return 4
        else:
            return self.climbStairs_3_recursive(n - 1) + \
                   self.climbStairs_3_recursive(n - 2) + \
                   self.climbStairs_3_recursive(n - 3)

    def climbStairs_3(self, n):
        a, b, c = 1, 2, 4
        if n < 3:
            return n
        elif n == 3:
            return 4
        for i in range(4, n + 1):
            res = a + b + c
            a, b, c = b, c, res

    # ---------------相邻两步不相同-------------- #
    def climbStairs_3_recent_diff_recursive(self, n):
        """3种步伐，相邻步伐不能一样"""
        count = 0
        def generate_one_steps(recent, res):
            nonlocal count
            if res == 0:
                count += 1
                return
            if recent != 1 and res >= 1:
                generate_one_steps(1, res - 1)
            if recent != 2 and res >= 2:
                generate_one_steps(2, res - 2)
            if recent != 3 and res >= 3:
                generate_one_steps(3, res - 3)
        generate_one_steps(0, n)
        return count

    def climbStairs_second_time(self, n):
        """第二遍递归"""
        if n < 3:
            return n
        return self.climbStairs_second_time(n - 1) + self.climbStairs_second_time(n - 2)

    def climbStairs_2(self, n: int) -> int:
        """第二遍"""
        temp, res = 2, 3
        if n <= 3:
            return n
        for i in range(4, n + 1):
            temp, res = res, (temp + res)
        return res

class Solution:
    def climbStairs1(self, n: int) -> int:
        if n < 3:
            return n
        prev, current = 1, 2
        for i in range(3, n + 1):
            temp = current
            current += prev
            prev = temp
        return current

    @lru_cache(128)
    def climbStairs2(self, n: int) -> int:
        """加缓存的"""
        if n <= 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs3(self, n: int) -> int:
        """手动加缓存的"""
        memo = {1: 1, 2: 2}
        def helper(n, memo):
            if n in memo:
                return memo[n]
            else:
                memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
                return memo[n]
        return helper(n, memo)

    def climbStairs4(self, n: int) -> int:
        """顺推"""
        if n < 4:
            return n
        prev, res = 2, 3
        for i in range(4, n + 1):
            prev, res = res, (prev + res)
        return res

    @lru_cache(10)
    def climbStairs5(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs5(n - 1) + self.climbStairs5(n - 2)

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        x, y = 2, 3
        for i in range(4, n + 1):
            x, y = y, (x + y)
        return y




if __name__ == '__main__':
    test = Solution()
    print(test.climbStairs(1))
    print(test.climbStairs(2))
    print(test.climbStairs(3))
    print(test.climbStairs(4))
    print(test.climbStairs(5))
