class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: abs(x[0]-x[1]),reverse=True)
        costs_1 = []
        costs_2 = []
        i = 0
        n = len(costs) //2
        while len(costs_1) < len(costs)//2 and len(costs_2) < len(costs)//2:
            if costs[i][0] < costs[i][1]:
                costs_1.append(costs[i][0])
            else:
                costs_2.append(costs[i][1])
            i+=1
        if len(costs_1) < n:
            costs = sorted(costs[i:], key=lambda x: x[0],reverse=True)
            for cost in costs[:n-len(costs_1)+1]:
                costs_1.append(cost[0])
        if len(costs_2) < n:
            costs = sorted(costs[i:], key=lambda x: x[1],reverse=True)
            for cost in costs[:n-len(costs_2)]:
                costs_2.append(cost[1])
        
        return sum(costs_1) + sum(costs_2)
