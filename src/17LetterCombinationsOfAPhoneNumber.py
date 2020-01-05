class Solution:
    def letterCombinations(self, digits):
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
        self.generate_combination(len_number, number_letter, result)

        return result

    def generate_combination(self, digits, len_number, number_letter, result):
        for i in range(len_number):
            current_len = number_letter[digits[i]]


