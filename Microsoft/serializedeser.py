"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serial = []
        def preorder(root):
            if not root:
                return 
            serial.append(str(root.val))
            for child in root.children:
                preorder(child)
            serial.append('#')
            return serial
        preorder(root)
        return ' '.join(serial)
        
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        tokens =deque(data.split())
        root = Node(int(tokens.popleft()),[])
        def helper(node):
            if not tokens:
                return
            while tokens[0]!="#":
                val =int(tokens.popleft())
                child = Node(val,[])
                node.children.append(child)
                helper(child)
            tokens.popleft()
        helper(root)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left)+postorder(root.right)+[root.val] if root else []
        return ' '.join(map(str,postorder(root)))
            

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = [int(x) for x in data.split(' ') if x]
        def helper(data,low, hig):
            if not data or data[-1]<=low or data[-1]>hig:
                return None
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(data,val,hig)
            root.left = helper(data,low,val)
            return root
        return helper(data,float('-inf'),float('inf'))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rser(root,string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) +','
                string = rser(root.left,string)
                string = rser(root.right,string)
            return string
        return rser(root,'')
       
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = list(data.split(','))
        def dser(data):
            if data[0]=='None':
                data.pop(0)
                return
            val = int(data[0])
            data.pop(0)
            
            root = TreeNode(val)
            root.left = dser(data)
            root.right = dser(data)
            return root
        return dser(data)
                
        
       
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))