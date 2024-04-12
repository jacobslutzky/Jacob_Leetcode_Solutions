class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        output = [0]*len(queries)
        i = 0
        for x, y, r in queries:
            for point_x, point_y in points:
                if ((x-point_x)**2+(y-point_y)**2)**(1/2) <= r:
                    output[i]+=1
            i+=1
        return output