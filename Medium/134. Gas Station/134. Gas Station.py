# https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # If total gas is less than total cost, we cannot complete the circuit
        if total_gas < total_cost:
            return -1
        
        current_gas = 0
        start = 0
        
        for current_station in range(len(gas)):
            current_gas += gas[current_station] - cost[current_station]
            
            # If current gas falls below 0, we cannot start from 'start'
            if current_gas < 0:
                start = current_station + 1  # Set start to the next station
                current_gas = 0  # Reset current gas balance
                
        return start