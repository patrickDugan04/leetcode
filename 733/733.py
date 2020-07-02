class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        que = [(sr, sc)]
        oldC = image[sr][sc]
        while len(que) != 0:
            cur = que.pop()
            if image[cur[0]][cur[1]] == oldC:
                image[cur[0]][cur[1]] = newColor
                if cur[0] != 0:
                    que.append((cur[0]-1, cur[1]))
                if cur[0] != len(image)-1:
                    que.append((cur[0]+1, cur[1]))
                if cur[1] != 0:
                    que.append((cur[0], cur[1]-1))
                if cur[1] != len(image[0])-1:
                    que.append((cur[0], cur[1]+1))
        return image
