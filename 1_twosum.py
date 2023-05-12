class Solution:
    def twoSum(self, nums, target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i
        return self.nums


input_list = [1, 2, 3]
solve = Solution()
print(solve.twoSum(input_list, 5))
