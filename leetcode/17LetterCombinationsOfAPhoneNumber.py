class Solution:
    def letterCombinations_1(self, digits):
        number_letter = {"2": "abc",
                         "3": "def",
                         "4": "ghi",
                         "5": "jkl",
                         "6": "mno",
                         "7": "pqrs",
                         "8": "tuv",
                         "9": "wxyz"}
        result = []
        len_number = len(digits)
        self.generate_combination_1(len_number, number_letter, result)

        return result

    def generate_combination_1(self, digits, len_number, number_letter, result):
        for i in range(len_number):
            current_len = number_letter[digits[i]]

    def letterCombinations(self, digits):
        number_letter = {"2": "abc",
                         "3": "def",
                         "4": "ghi",
                         "5": "jkl",
                         "6": "mno",
                         "7": "pqrs",
                         "8": "tuv",
                         "9": "wxyz"}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(number_letter[digits])
        return [x+y for x in self.letterCombinations(digits[0]) for y in self.letterCombinations(digits[1:])]


if __name__ == '__main__':
    test = Solution()
    print(test.letterCombinations("23"))


