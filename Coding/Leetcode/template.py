'''
Leetcode Daily Challenge
Date: 2nd Feb, 2022
Link: https://leetcode.com/problems/verifying-an-alien-dictionary/description/
Solution Link:

'''

# ==============================================================
'''
NOTES:
Hashmap {key1: value1, keys: value2}
Here: index, character

MISTAKES:
if num1>num2:
    return False

- loop termination before iteration
'''
# ==============================================================
class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        #define hashmap
        lookup = {}
        orderN = len(order)
        for i in range(orderN):
            index = i+1
            character = order[i]
            lookup[ character ] = index
        
        # assumption: word1 < word2
        def checkOrder(word1, word2):
            #word1 is small
            # swap = False
            N1 , N2 = len(word1), len(word2)
            
            for i in range(N1):
                if i>=N2:
                    break

                if word1[i]==word2[i]:
                    continue
                
                num1 = lookup[ word1[i] ]
                num2 = lookup[ word2[i] ]

                if num1>num2:
                    return False
                
                return True
            
            if N1>N2:
                 return False
            
            return True

        wordN = len(words)

        for i in range(1, wordN):
            w1 = words[i-1]
            w2 = words[i]

            if checkOrder(w1, w2)==False:
                return False
 
        return True


# ================================================================
'''
TestCases
'''
# # ================================================================
if __name__=='main':
    s = Solution()
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    # order = "abcdefghijklmnopqrstuvwxyz"
    res = s.isAlienSorted(words,order)
    print(f"This is the result: {res}")