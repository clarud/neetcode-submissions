from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # the prerequisite can be represented in a dag where a -> b meaning a is a prerequisite of b, with the nodes being the courses and the edges being the prerequisites

        # represent the graph as a adjacency list O(V+E) at the minimum with no edges V and E edges for populated
        edges = {i: [] for i in range(numCourses)}
        
        # number of prereqs per course
        prereqs = [0] * numCourses

        for a, b in prerequisites:
            edges[b].append(a)
            prereqs[a] += 1

        # do a bfs topo sort
        queue = deque([course for course, count in enumerate(prereqs) if count == 0])
        processed = 0
        while queue:
            current = queue.popleft()
            processed += 1
            
            for nextc in edges[current]:
                prereqs[nextc] -= 1
                if prereqs[nextc] == 0:
                    queue.append(nextc)

        print(processed)
        return processed == numCourses

