class Solution:
    def threeSum_baoli(self, nums):
        """暴力，超时"""
        result = set()
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if i != j != k and nums[i] + nums[j] + nums[k] == 0:
                        res.append(nums[i])
                        res.append(nums[j])
                        res.append(nums[k])
                        result.add(tuple(sorted(res)))
                        res = []
                        break
        return [list(item) for item in result]

    def threeSum_no(self, nums):
        result = {}
        a = [0] * len(nums) #[1, 0, -1, -2, 1, 4]
        nums = sorted(nums)

        for i in range(len(nums)):
            a[i] = 0 - nums[i]

        for i in range(len(a)):
            target = a[i]
            b = {}
            for j in range(len(nums)):
                if i != j:
                    if (nums[i], nums[j]) in result:
                        continue
                    c = target - nums[j]

                    if nums[j] in b:
                        if j != b[nums[j]] != i:
                            res = tuple(sorted([nums[i], nums[j], nums[b[nums[j]]]]))
                            result[res[0:2]] = res[-1]
                    else:
                        b[c] = j
        return [list(k)+[v] for k, v in result.items()]

        # for k, v in result.items():
        #     a = list(k)
        #     b = list(v)
        #     result += a + b

    def threeSum(self, nums):
        result = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i+1, length-1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if res < 0:
                    left += 1
                elif res > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result





if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    test = Solution()
    print(test.threeSum(nums))
    #[
  #[-1, 0, 1],
  #[-1, -1, 2]
#]