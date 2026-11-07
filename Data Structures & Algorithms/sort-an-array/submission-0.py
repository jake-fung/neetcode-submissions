class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # find max, min of nums, build bucket of size max(nums) - min(nums)
        # assign each number into its index relative to min of nums (e.g. number 1 min 0 -> index 1)
        # res array, loop the bucket and build the res array
        lo, hi = min(nums), max(nums)
        bucket = [[] for _ in range(hi - lo + 1)]
        for num in nums:
            bucket[num - lo].append(num)
        res = []
        for i in range(len(bucket)):
            for bNum in bucket[i]:
                res.append(bNum)
        return res
