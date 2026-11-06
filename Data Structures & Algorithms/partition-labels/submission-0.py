class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #abc -> [1,1,1]
        # loop through the array, record each c first index and last index
        # [[0,3],[1,4],[2,5]]
        # interval merge
        # [[0,5]] take the length 6
        # [[0,3],[1,4],[5,7],[6,9],[10,10],[11,11],[12,12]]
        # [[0,4],[5,9],[10,10],[11,11],[12,12]]
        # 5 + 5 + 1 + 1 + 1

        cIndex = {}
        for i, c in enumerate(s):
            first, last = cIndex.get(c, [i,i])
            cIndex[c] = [first, i]
        print(cIndex)
        intervals = list(cIndex.values())
        merged = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])
        ans = []
        for s, e in merged:
            ans.append(e - s + 1)
        return ans



            

