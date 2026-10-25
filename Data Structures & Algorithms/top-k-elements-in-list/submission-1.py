class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        bucket = []
        res = []
        for _ in range(len(nums) + 1):
            bucket.append([])
        for num, freq in c.items():
            bucket[freq].append(num)
        for i in range(len(nums), 0, -1):
            while not bucket[i] == []:
                if len(res) == k:
                    break;
                res.append(bucket[i][-1])
                bucket[i].pop()
        return res