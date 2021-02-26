# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def Bst(l,r):
            if l>r:
                return None
            m=(l+r)//2
            root =  TreeNode(nums[m])
            root.left = Bst(l,m-1)
            root.right = Bst(m+1,r)
            return root
        
        return Bst(0,len(nums)-1)