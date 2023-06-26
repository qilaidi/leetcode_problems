class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            nlen = len(nums)
            i = nlen // 2
            if target > nums[i]:
                i += 1
                while i < nlen:
                    if target < nums[i]:
                        return i
                    else:
                        i += 1
            else:
                i -= 1
                while i >= 0:
                    if target > nums[i]:
                        return i + 1
                    else:
                        i -= 1
            return i if i >= 0 else 0


if __name__ == '__main__':
    test = Solution()
    assert test.searchInsert([1,3,5,6], 5) == 2
    assert test.searchInsert([1,3,5,6], 2) == 1
    assert test.searchInsert([1,3,5,6], 7) == 4