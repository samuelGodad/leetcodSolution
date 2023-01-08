# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false



class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words=s.split(' ')
        map1={}
        map2={}
        if len(words)!=len(pattern):
            return False
        for word,char in zip(words,pattern):
            if word not in map1 and char not in map2:
                map1[word]=char
                map2[char]=word
            elif map1.get(word)==char and map2.get(char)==word:
                pass
            else:
                return False
        return True