class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        d = {}

        for numPassengers, from_i, to_i in trips:
            if from_i in d:
                d[from_i] += numPassengers
            else:
                d[from_i] = numPassengers
            if to_i in d:
                d[to_i] -= numPassengers
            else:
                d[to_i] = -numPassengers
        
        currNumPassengers = 0
        for i in range(0, max(d.keys())+1):
            if i in d:
                currNumPassengers += d[i]
                if currNumPassengers > capacity:
                    return False
        return True