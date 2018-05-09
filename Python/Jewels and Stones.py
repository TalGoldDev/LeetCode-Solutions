"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

"""
solution using dictionary.
"""
class Solution:
    def numJewelsInStonesDictionary(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        stones = dict()
        for j in range(len(J)):
            stones[J[j]] = j
        for i in range(len(S)):
            if S[i] in stones:
                    counter += 1
                
        return counter

"""
Solution using for-loops.
"""
class Solution2:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        for i in range(len(S)):
            for j in range(len(J)):
                if (J[j] == S[i]):
                    counter += 1
                
        return counter
