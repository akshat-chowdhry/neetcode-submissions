class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res = []

        for i in nums:
            hashmap[i] += 1
        
        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        temp = list(sorted_hashmap.keys())
        
        for i in range(k):
            res.append(temp[i])

        return res

        