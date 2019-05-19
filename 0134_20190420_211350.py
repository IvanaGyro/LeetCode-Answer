class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        earnings = [gas[i] - cost[i] for i in range(len(gas))]
        earnings += earnings
        remainder, r = 0, 0
        for l in range(len(gas)):
            while remainder >= 0 and r - l < len(gas):
                remainder += earnings[r]
                r += 1
            if remainder < 0:
                remainder -= earnings[l]
            elif r - l == len(gas):
                return l
        return -1
    