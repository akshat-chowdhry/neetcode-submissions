class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                res.extend([hashmap[diff],i])
            else:
                hashmap[nums[i]] = i

        return res
            

        