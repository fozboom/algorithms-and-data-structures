from collections import namedtuple

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

node = namedtuple("node", ["amount_if_rob_this", "amount_if_not_rob_this"])

class Solution(object):
    def dfs(self, root):
        if not root:
            return node(0, 0)
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        rob_this = root.val + left.amount_if_not_rob_this + right.amount_if_not_rob_this
        
        not_rob_this = max(left.amount_if_not_rob_this, left.amount_if_rob_this) + max(right.amount_if_rob_this, right.amount_if_not_rob_this)
        
        return node(rob_this, not_rob_this)
    
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = self.dfs(root)
        
        return max(res.amount_if_rob_this, res.amount_if_not_rob_this)
        
        
        
        