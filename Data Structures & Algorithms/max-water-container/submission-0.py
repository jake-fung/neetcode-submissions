class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            lHeight = heights[l]
            rHeight = heights[r]
            height = min(lHeight, rHeight)
            width = r - l
            maxArea = max(maxArea, height*width)
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1
        return maxArea