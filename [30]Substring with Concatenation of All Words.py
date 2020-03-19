# You are given a string, s, and a list of words, words, that are all of the sam
# e length. Find all starting indices of substring(s) in s that is a concatenation
#  of each word in words exactly once and without any intervening characters. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" re
# spectively.
# The output order does not matter, returning [9,0] is fine too.
#  
# 
#  Example 2: 
# 
#  
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []
#  
#  Related Topics Hash Table Two Pointers String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
# leetcode submit region end(Prohibit modification and deletion)
