class Solution1:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums[:] + [0] * counts

class Solution2:
    def moveZeroes(self, nums):
        zero_indexs = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_indexs.append(i)
            elif nums[i] != 0:
                if zero_indexs:
                    nums[zero_indexs.pop(0)], nums[i] = nums[i], 0
                    zero_indexs.append(i)
        return nums

class Solution:
    def moveZeroes(self, nums):
        """执行用时 :32 ms, 在所有 Python3 提交中击败了98.38%的用户"""
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                if zero_index != i:
                    nums[i] = 0
                zero_index += 1
        return nums

if __name__ == '__main__':
    test = Solution()
    print(test.moveZeroes([0,1,0,3,12]))