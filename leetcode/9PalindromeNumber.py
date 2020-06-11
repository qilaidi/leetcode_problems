# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return ("".join(reversed(str(x)))) == str(x)




if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome(121))
    print(test.isPalindrome(-121))
    print(test.isPalindrome(10))