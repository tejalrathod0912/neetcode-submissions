from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)

        sort_nums = sorted(dic,key = lambda x:dic[x],reverse=True)

        return sort_nums[:k]
    



