class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0 
        right = len(height)-1
        while left < right:
            water = min(height[left],height[right])*(right-left)
            max_water = max(water, max_water)

            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
                left += 1

        return max_water 