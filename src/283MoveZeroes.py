class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums[:] + [0] * counts


if __name__ == '__main__':
    test = Solution()
    print(test.moveZeroes([0,1,0,3,12]))
