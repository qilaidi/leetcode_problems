import math

from leetcode_problems.utils.timer import timethis


class Solution:
    def uniquePaths_stupid_recursive(self, m: int, n: int) -> int:
        """递归，超时了"""
        paths = 0
        def generate_path(m_steps, n_steps):
            nonlocal paths
            if m_steps == 0 and n_steps == 0:
                paths += 1
                return
            if m_steps > 0:
                generate_path(m_steps - 1, n_steps)
            if n_steps > 0:
                generate_path(m_steps, n_steps - 1)

        generate_path(m-1, n-1)
        return paths

    def uniquePaths_forloop(self, m, n):
        """排列组合"""
        # c(N, k) = N!/(k!(N-k)!)
        # c((m+n-2), m) = (m+n-2)!/((n-2)!m!)
        # = ((m+n-2)-1)*((m+n-2)-2))*..*(n-2+1)/m!
        path = 1
        for i in range(1, m):
            path = path * (n - 1 + i) / i
        return int(path)

    @timethis
    def uniquePaths_factorial(self, m, n):
        """排列组合-使用阶乘函数"""
        # c(N, k) = N!/(k!(N-k)!)
        # N = m+n-2, k = m-1
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))

    @timethis
    def uniquePaths(self, m, n):
        """动态规划"""
        process = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                process[j] += process[j-1]
        return process[-1]

if __name__ == '__main__':
    test = Solution()
    print(test.uniquePaths_factorial(3, 2)) #3
    print(test.uniquePaths_factorial(7, 3)) #28
    print(test.uniquePaths_factorial(99,99))
