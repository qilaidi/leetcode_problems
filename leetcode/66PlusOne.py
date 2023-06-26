# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/4/26
from typing import List


class Solution:
    def plusOne1(self, digits: List[int]) -> List[int]:
        len_digit = len(digits)
        ori_digit = 0
        for x in digits:
            ori_digit += 10 ** (len_digit - 1) * x
            len_digit -= 1
        result_str = str(ori_digit + 1)
        result = [int(x) for x in result_str]
        return result

    def plusOne2(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        if digits[index] + 1 == 10:
            digits[index] = 0
            left = 1
            index -= 1
        else:
            digits[index] += 1
            left = 0

        while index >= 0 and left > 0:
            if digits[index] + 1 == 10:
                digits[index] = 0
                left = 1
                index -= 1
            else:
                digits[index] += 1
                left = 0

        if index == -1 and left > 0:
            digits.insert(0, 1)
        return digits

    def plusOne3(self, digits: List[int]) -> List[int]:
        str_digits = ""
        for i in digits:
            str_digits += str(i)
        result = str(int(str_digits) + 1)
        return [int(x) for x in result]

    def plusOne(self, digits: List[int]) -> List[int]:
        len_digits = len(digits) - 1
        while True:
            if digits[len_digits] == 9 and len_digits == 0:
                digits[len_digits] = 0
                digits.insert(0, 1)
                break
            elif digits[len_digits] == 9:
                digits[len_digits] = 0
                len_digits -= 1
            else:
                digits[len_digits] += 1
                break
        return digits

    def plus_one(self, digits: List[int]) -> List[int]:
        digits.reverse()
        dlen = len(digits)
        i = 0
        while i < dlen:
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                digits.reverse()
                return digits
            else:
                digits[i] = 0
                i += 1
        if i == dlen:
            digits.append(1)
        digits.reverse()
        return digits






if __name__ == '__main__':
    test = Solution()
    print(test.plusOne([1,2,3]))
    print(test.plusOne([9,9,9]))
    print(test.plusOne([4,3,2,1]))
    print(test.plusOne([4,3,2,9]))