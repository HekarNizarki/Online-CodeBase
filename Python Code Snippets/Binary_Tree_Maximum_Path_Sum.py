class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def maxPathSum(root):
    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        left=max(helper(node.left),0)
        right=max(helper(node.right),0)
        max_sum=max(max_sum,left+right+node.val)
        return max(left,right)+node.val
    max_sum=float('-inf')
    helper(root)
    return max_sum