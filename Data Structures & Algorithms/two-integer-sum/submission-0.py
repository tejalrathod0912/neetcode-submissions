class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            
            if nums[i] not in dic:
                result = target - nums[i]
                dic[result] = i
            else:
                print(dic)
                return [dic[nums[i]],i]
            

        