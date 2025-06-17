class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Codec:
    def serialize(self,root):
        def helper(node):
            if not node:
                return 'None,'
            return str(node.val)+','+helper(node.left)+helper(node.right)
        return helper(root)
    def deserialize(self,data):
        def helper(nodes):
            val=next(nodes)
            if val=='None':
                return None
            node=TreeNode(int(val))
            node.left=helper(nodes)
            node.right=helper(nodes)
            return node
        nodes=iter(data.split(','))
        return helper(nodes)