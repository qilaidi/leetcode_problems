from typing import List


class Solution:
    def removeDuplicates_old(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1
        return nums

    def removeDuplicates(self, nums: List[int]) -> int:
        dup_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[dup_index-1]:
                nums[dup_index] = nums[i]
                dup_index += 1
        return dup_index

if __name__ == '__main__':
    test = Solution()
    print(test.removeDuplicates([1,1,2]))
    print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(test.removeDuplicates([1,1]))