class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        curr_gas = 0
        answer = 0
        for i in range(len(gas)):
            net = gas[i]-cost[i]
            total_gas += net
            curr_gas += net

            if curr_gas < 0:
                answer = i+1
                curr_gas=0
        if total_gas < 0:
            answer = -1
        return answer

