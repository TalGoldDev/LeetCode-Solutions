"""
 Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):

    # a function to find the maximum num in a list.
    def findMax(self,nums):
        current_max = 0
        for item in range(len(nums)):
            if nums[item] > nums[current_max]:
                current_max = item
        return current_max

    # creating a heap using
    def createHeap(self, nums):
        rootNode = TreeNode(nums[0])
        nums[0].pop
        for item in nums:
            if item > rootNode.val:
                new_node = TreeNode(nums[rootNode.val])
                rootNode.val = item

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.findMax(nums)
        rootNode = TreeNode(nums[root])
        left_list = nums[:root]
        right_list = nums[root+1:]
        nums.pop(root)
       # root.left = createHeap(left_list)
