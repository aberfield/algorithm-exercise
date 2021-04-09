class Solution:
    def findMin2(self, nums:[]) -> int:

        left = 0
        right = len(nums) - 1
        while(left < right) {
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid;
            else:
                right -= 1
        }
        return nums[left]