class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class ajL:
    def __init__(self, nodes):
        self.Al = [None]*nodes

    def add_edge(self, start, fin):
        n = Node(fin)
        n.next = self.Al[start]
        self.Al[start] = n

    def get_kid(self, val):
        temp = self.Al[val]
        l = []
        while temp != None:
            l.append(temp.val)
            temp = temp.next
        return l


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        aj = ajL(numCourses)
        leadins = [0]*numCourses
        for i in prerequisites:
            aj.add_edge(i[1], i[0])
            leadins[i[0]] += 1

        queue = []
        for i,n  in enumerate(leadins):
            if n == 0:
                queue.append(i)


        order = []
        while len(queue) != 0:
            n = queue.pop(0)
            order.append(n)
            for i in aj.get_kid(n):
                leadins[i] -= 1
                if leadins[i] == 0:
                    queue.append(i)
                elif leadins[i] < 0:
                    return []

        if len(order) != numCourses:
            return []

        return order
