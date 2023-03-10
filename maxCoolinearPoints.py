# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
import sys
from collections import defaultdict, Counter

# from typing import DefaultDict, List, Tuple
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def getAngles(p1,p2):
            y=p2[1]-p1[1]
            x=p2[0]-p1[0]
            
            if x==0:
                return sys.maxsize
            return float(y)/float(x)
            if angles<360:
                angles+=360
            return angles
        answer=0
        n=len(points)
        for i in range(n):
            p1=points[i]
            same=0
            angles=[]
            for j in range(n):
                if i!=j:
                    p2=points[j]
                    if p1==p2:
                        same+=1
                    else:
                        angles.append(getAngles(p1,p2))
            counter = Counter(angles)
            max1=0
            if counter.values():
                max1= max(counter.values())
            answer=max(answer,max1+1+same)
        return answer

    
