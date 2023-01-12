# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
# the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        summ=0
        temp=x

        
        if temp>0:
            while temp!=0:
                last=temp%10
                summ=summ*10+last
                temp=temp//10
            if summ > (int(math.pow(2,31)-1)):
                return 0
            else:
                return summ
            
        else:
            temp=abs(temp)
            while temp!=0:
                last=temp%10
                summ=summ*10+last
                temp=temp//10
            if -summ<(int(math.pow(-2,31)-1)):
                return 0
            return -summ
