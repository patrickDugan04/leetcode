import heapq
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        heap = []
        for i, n in enumerate(arr):
            heap.append((n, i))

        heapq.heapify(heap)

        s = 0
        while len(heap) > 1:

            # get the min
            small = heapq.heappop(heap)
            minI = arr.index(small[0])

            # check its suroundings to make smallest pairs
            neighbors = []
            if(minI-1 >= 0):
                neighbors.append(arr[minI-1])
            if(minI+1 < len(arr)):
                neighbors.append(arr[minI+1])

            neighbor = min(neighbors)

            # get min out of arr
            arr.pop(minI)

            #sum
            s += neighbor * small[0]

        return s



            
