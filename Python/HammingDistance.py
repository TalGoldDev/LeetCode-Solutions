"""
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231. 
"""
class Solution(object):
    def intToBinary(self,x):
        string_x = ""
        n = 31
        while n > 0:
            if (x < 2 ** n):
                string_x += "0"
            if (x >= 2 ** n):
                string_x += "1"
                x -= 2 ** n
            n -= 1
        if x == 1:
            string_x += "1"
        else:
            string_x += "0"
        return string_x

    def hammingDistance(self,x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        string_x = self.intToBinary(x)
        string_y = self.intToBinary(y)

        print(string_x)
        print(string_y)

        for item in range(32):
            if string_x[item] != string_y[item]:
                count += 1

        print(count)
        return count

    
