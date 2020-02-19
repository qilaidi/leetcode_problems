# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/18
import collections
import string


class Solution:
    def findAnagrams_1(self, s, p):
        """超时"""
        return [index for index in range(len(s)) if sorted(s[index:index+len(p)]) == sorted(p)]

    def findAnagrams_2(self, s, p):
        res, target, current, counter = [], collections.defaultdict(int), collections.defaultdict(int), 0
        for i in p:
            target[i] += 1
        for index in range(len(s)):
            while counter < len(p):
                current[s[index]] += 1
                counter += 1
                break
            if current == target:
                res.append(index - len(p) + 1)
            if counter == len(p):
                if current[s[index - len(p) + 1]] == 1:
                    del current[s[index - len(p) + 1]]
                else:
                    current[s[index - len(p) + 1]] -= 1
                counter -= 1
        return res

    def findAnagrams(self, s, p):
        def counter(s):
            return [s.count(c) for c in string.ascii_lowercase]
        ord_a = ord('a')
        counts = counter(s[:len(p)])
        target = counter(p)
        if counts == target:
            yield 0
        for i, c in enumerate(s[len(p):]):
            counts[ord(s[i]) - ord_a] -= 1
            counts[ord(c) - ord_a] += 1
            if counts == target:
                yield i + 1



if __name__ == '__main__':
    test = Solution()
    (test.findAnagrams("cbaebabacd", "abc"))
    (test.findAnagrams("abab", "ab"))
    (test.findAnagrams("abaacbabc", "abc")) #3, 4, 6
