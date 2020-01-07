class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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

if __name__ == '__main__':
    test = Solution()
    print(test.uniquePaths(3, 2))
    print(test.uniquePaths(7, 3))
