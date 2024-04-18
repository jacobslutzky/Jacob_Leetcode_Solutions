class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        size = sum(matchsticks) //4
        matchsticks.sort(reverse = True)

        def recurse(i, sum1, sum2, sum3,sum4):
            if i == len(matchsticks) and sum1 == size and sum2 == size and sum3 == size and sum4 == size:
                print(sum1)
                print(sum2)
                print(sum3)
                print(sum4)
                return True
            if i >=  len(matchsticks):
                return False
            if sum1 > size or sum2  > size or sum3 > size or sum4 > size:
                return False
            
            if recurse(i+1,sum1+matchsticks[i],sum2,sum3,sum4):
                return True
            if sum1 > 0 and recurse(i+1,sum1,sum2+matchsticks[i],sum3,sum4):
                return True
            if sum2 > 0 and recurse(i+1,sum1,sum2,sum3+matchsticks[i],sum4):
                return True
            if sum3 > 0 and recurse(i+1,sum1,sum2,sum3,sum4+matchsticks[i]):
                return True
        
            return False
        
        return recurse(0,0, 0, 0, 0)
                    
