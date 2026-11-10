class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for index, point in enumerate(points):
            dist = point[0]**2 + point[1]**2
            heap.append((dist, index))
        heapq.heapify(heap)
        res = []
        for i in range(k):
            dist, index = heapq.heappop(heap)
            res.append(points[index])
        return res


        # res =[[0,2],[2,0]]