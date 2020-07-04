import heapq
class Node:
    def __init__ (self, v, n, w):
        self.val = v
        self.next = n
        self.time = w

    def gval(self):
        print(self.val)

class graph:
    def __init__ (self, size):
        self.l = [None]*(size+1)
    def add_edge (self, a, b, w): # from a to b time w
        n = Node(b, 0, w)
        n.next = self.l[a]
        self.l[a] = n

    def get_aj (self, a): # a is node num
        ne = []
        n = self.l[a]
        while n != None:
            ne.append((n.val, n.time))
            n = n.next
        return ne

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        aj = graph(N)
        shortest = [] #shortest times
        heap = [] #min heap
        shortest.append(0)
        #0th index to make calls line up nicely
        for i in range(N): # putting in nodes
            if i+1 == K:
                shortest.append(0)
                heap.append((0,i+1))
            else:
                shortest.append(float('inf'))
                heap.append((float('inf'),i+1))
        heapq.heapify(heap)
        for i in times:
            aj.add_edge(i[0], i[1], i[2])
# djiktras

        while len(heap) != 0:
            (dist, Min) = heapq.heappop(heap)
            # print(Min)
            for val, time in aj.get_aj(Min):
                totaltime = dist + time
                # print("  ",val,", ",totaltime)
                # print(shortest)
                if totaltime < shortest[val]:
                    shortest[val] = totaltime
                    #change heap
                    for i,b in enumerate(heap):
                        #b is (weight, val/node num)
                        if b[1] == val:
                            heap[i] = (totaltime,val)
                            break
            #relax
            heapq.heapify(heap)

        time = max(shortest)
        #if infinity then signal will never reach node
        #specification said to print -1 in this case
        if time == float('inf'):
            return -1
        return time

        
