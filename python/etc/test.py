# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) :
        arr_result = []
        arr_tmp = getChild(root)
        arr_result.append(arr_tmp)
        arr_val = [arr_node[0].val, arr_node[1].val]
        print(arr_val)

def getChild(node) :
    return [node.left, node.right]



if __name__ == '__main__' :
    node1 = TreeNode(9)
    node2 = TreeNode(15)
    node3 = TreeNode(7)
    node4 = TreeNode(20, node2, node3)
    tree = TreeNode(3, node1, node4)
    result = Solution()

    print(result.zigzagLevelOrder(tree))


