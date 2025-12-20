class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        l, r = 0, len(height) - 1

        while l < r:
            x = r - l # this here is basically the width right
            area = min(height[l], height[r]) * x # have to use the min as how are you gonna fill up a water bowl to the max wall? it does only till the min wall

            ans = max(area, ans)
            # below is the main 'alegbraic' algo that this q is testing us on, basically area = (r - l) * min(h1, h2)
            # to maximise the area we can either increase the  r - l term or the min() term 
            # now the r - l term will be decreasing right but the min term can increase, and will only increase if we up the lower of the h1 and h2
            # thats what we do here, if height[l] is smaller then the l pointer goes up and vice versa, hoping to get max area

            # Furthermore, the minimum of the l and r is acc what determines the area so the only way to see if area 'increases' is to move the lower of the both
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return ans

        
