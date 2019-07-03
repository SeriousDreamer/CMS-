class TreeNode:
    def __init__(self, data=None, first_child=None, next_sibling=None):
        self.data = data
        # 第一个孩子节点
        self.first_child = first_child
        # 右兄弟
        self.next_sibling = next_sibling


class Tree:
    def __init__(self, root=None):
        # 树的根节点
        self.root = root
        self.pre_order_result = []

    def is_empty(self):
        """
        判断树是否为空
        :return: bool类型，True代表为空，False代表不为空
        """
        if self.root is None:
            return True
        else:
            return False

    def pre_order(self, node):
        # 树的先根遍历
        if node is None:
            return
        print(node.data, end=" ")
        self.pre_order_result.append(node.data)
        self.pre_order(node.first_child)
        self.pre_order(node.next_sibling)

    def clear(self):
        """
        清空树
        :return:
        """
        self.root = None
        self.pre_order_result = None

# if __name__ == "__main__":
#     e = TreeNode(data="e")
#     k = TreeNode(data='k')
#     h = TreeNode(data='h', next_sibling=k)
#     g = TreeNode(data='g', next_sibling=h)
#     f = TreeNode(data='f', first_child=g)
#     c = TreeNode(data='c', first_child=f)
#     b = TreeNode(data='b', next_sibling=c)
#     d = TreeNode(data='d', next_sibling=e)
#     a = TreeNode(data='a', first_child=d, next_sibling=b)
#     r = TreeNode(data='r', first_child=a)
#
#     bt = Tree(root=r)
#     bt.pre_order(bt.root)
