# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/22
import collections





class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        mask_dict, res = collections.defaultdict(list), None
        word_len = len(endWord)
        for word in wordList:
            for i in range(word_len):
                mask_dict[word[:i] + "*" + word[i+1:]].append(word)

        beginq = [(beginWord, 1)]
        endq = [(endWord, 1)]

        begin_visited = {beginWord: 1}
        end_visited = {endWord: 1}

        def trans_word(queue, queue_visited, other_visited):
            current_word, level = queue.pop(0)
            for i in range(word_len):
                mask_word = current_word[:i] + "*" + current_word[i+1:]
                for word in mask_dict[mask_word]:
                    if word in other_visited:
                        return level + other_visited[word]
                    if word not in queue_visited:
                        queue_visited[word] = level + 1
                        queue.append((word, level + 1))
            return None

        while beginq and endq:
            res = trans_word(beginq, begin_visited, end_visited)
            if res:
                return res
            res = trans_word(endq, end_visited, begin_visited)
            if res:
                return res
        return 0

