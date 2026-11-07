class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we initialise the bucket, from 0 to nums, as numbers could appear as few as one time and as much as all the nums, the index of the bucket indicates the frequency of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        # initialise a counter which keeps track of the freq
        c = Counter(nums)
        # put each num in frequency index
        for num, freq in c.items():
            buckets[freq].append(num)
        res = []
        # loop through array backwards, appending number to res
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                # if length of res is enough, return it
                if len(res) == k:
                    return res


