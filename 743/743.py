import heapq
class Node:
    def __init__ (self, v, n):
        self.val = v
        self.next = n

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        AjL = [node()]*N
