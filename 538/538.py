def get_m(n,b):
    if n != None:
        m = n.val
        m += get_m(n.right,b)
        n.val = m + b
        m += get_m(n.left,n.val)
        return m
    return 0
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        get_m(root,0)
        return root
