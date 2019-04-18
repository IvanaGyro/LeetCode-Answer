class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
       
        for i in range(len(height)-1):
            height[~i] -= height[~i-1]
        height[0] = 0
        
        water = 0
        stack = []
        for i in range(len(height)):
            if height[i] > 0:
                h = height[i]
                while h and stack:
                    slope, idx = stack.pop()
                    if h + slope >= 0:
                        water += -slope * (i - idx)
                        h += slope
                    else:
                        water += h * (i - idx)
                        stack.append((h + slope, idx))
                        h = 0
                    
            elif height[i] < 0:
                stack.append((height[i], i))
        
        return water
    
    # ,2,1,2,5
        