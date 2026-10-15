class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0,(len(heights)-1)
        max_h = 0
        while right>left:
            w = right - left
            h = w*min(heights[left],heights[right])
            if h > max_h:
                max_h = h
            if heights[left]>heights[right]:
                right -= 1
            else:
                left += 1
        return max_h

        