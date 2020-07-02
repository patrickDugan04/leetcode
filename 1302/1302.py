class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        i = 0
        stack = [(root,0)]
        big = 0
        down = 0
        while len(stack) != 0:
            branch = False
            o = stack.pop()
            down = o[1]
            n = o[0]
            if n.left != None:
                stack.append((n.left, down+1))
                branch = True
            if n.right != None:
                stack.append((n.right, down+1))
                branch = True
            if not branch:
                if big < down:
                    big = down
                    i = n.val
                elif big == down:
                    i += n.val
        return i
