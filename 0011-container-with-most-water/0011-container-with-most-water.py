class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_length=0
        l=0
        r=len(height)-1
        
        while l<r:
            area = (r - l) * min(height[r], height[l])
            max_length=max(area,max_length)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_length
        