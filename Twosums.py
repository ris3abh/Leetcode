class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = 0
        for i in nums:
            j = target - i
            k += 1
            nums2 = nums[k:]
            if j in nums2:
                return [k - 1, nums2.index(j) + k]

