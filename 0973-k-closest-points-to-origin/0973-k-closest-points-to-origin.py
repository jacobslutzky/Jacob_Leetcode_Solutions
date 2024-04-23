import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        return self.quickselect(points, k, 0, len(points)-1)
    
    def quickselect(self, points, k, l, r):

        if l < r:
             
            pivot = random.randrange(l, r)
            
            temp = points[r]
            points[r] = points[pivot]
            points[pivot] = temp
            
            i = l
            for j in range(l, r):
                if self.get_dist(points[j]) <= self.get_dist(points[r]):
                    temp = points[i]
                    points[i] = points[j]
                    points[j] = temp
                    i+=1
            temp = points[i]
            points[i] = points[r]
            points[r] = temp
            
            if i == k-1:
                return points[:k]
            elif i < k:
                return self.quickselect(points, k, i, r)
            else:
                return self.quickselect(points, k, 0, i)

    
    def get_dist(self, point):
        return (point[0]**2 + point[1]**2)**.5



