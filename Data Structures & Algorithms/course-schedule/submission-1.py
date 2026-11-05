class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        # adjList building
        for firstC, secondC in prerequisites:
            lst = adjList.get(firstC, [])
            lst.append(secondC)
            adjList[firstC] = lst

        visiting = set()

        # dfs detecting cycle
        def dfs(i):
            # if course is in seen, cycle detected and reject
            if i in visiting:
                return False
            # if course has no postrequisite, no cycle will be detected
            if i not in adjList.keys():
                return True
            # add it in visiting
            visiting.add(i)
            # loop through all the postrequisite, run dfs each
            for course in adjList[i]:
                if not dfs(course):
                    return False
            # if no loop, we know that the course can be completed, backtrack to the previous course
            visiting.remove(i)
            # if we run into the same course, the next time running will be true trivially
            adjList[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# 0: 1

# seen: {0} course: 1
