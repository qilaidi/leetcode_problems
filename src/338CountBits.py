# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/9

class Solution:
    def countBits_bit(self, num):
        """132ms"""
        result = []
        for i in range(num+1):
            res = 0
            while i != 0:
                res += 1
                i &= i - 1
            result.append(res)
        return result

    def countBits_1(self, num):
        """96ms"""
        result = []
        for i in range(num+1):
            result.append(bin(i).count("1"))
        return result

    def countBits(self, num):
        result = [0] * (num + 1)
        for i in range(1, num+1):
            result[i] += result[i & (i - 1)] + 1 # 去掉最低位的1那一个值一定知道，在那个基础上加上去掉的这一个，真是聪明
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.countBits(2)) # [0, 1, 1]
    print(test.countBits(5)) # [0, 1, 1, 2, 1, 2]
