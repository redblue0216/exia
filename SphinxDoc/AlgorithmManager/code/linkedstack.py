# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个链接栈类，主要用于顺序存储图的排序结果
"""
模块介绍
-------

这是一个链接栈类，主要用于顺序存储图的排序结果

    功能：              

        （1）提供顺序存储功能                                                                                                                                                                                                                                                                                                                                                                                                                          

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from node import Node
from abstractstack import AbstractStack



####### 链接栈类 #############################################################
### 功能：                                                                 ###
### （1）提供顺序存储功能                                                    ###
##############################################################################



####### 链接栈类 ##################################################################################
##################################################################################################



class LinkedStack(AbstractStack):
    """
    类介绍：

        这是一个链接栈，主要用于顺序存储图的排序结果
    """


    def __init__(self,sourceCollection = None):
        """
        属性方法功能：

            定义一个初始化函数
        
        参数：
            _items (object)：栈中元素
        """

        self._items = None
        AbstractStack.__init__(self,sourceCollection)


    def __iter__(self):
        """
        属性方法功能：

            定义一个迭代器的魔法方法
        """

        def visitNodes(node):
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList = list()
        visitNodes(self._items)
        return iter(tempList)

    
    def peek(self):
        """
        方法功能：

            定义一个选择栈顶的方法
        """

        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self._items.data


    def clear(self):
        """
        方法功能：

            定义一个清空栈的方法
        """

        self._size = 0
        self._items = None


    def push(self,item):
        """
        方法功能：

            定义一个入栈的方法
        """

        self._items = Node(item,self._items)
        self._size += 1


    def pop(self):
        """
        方法功能：

            定义一个出栈的方法
        """

        if self.isEmpty():
            raise KeyError("The stack is empty.")
        data = self._items.data
        self._items = self._items.next
        self._size -= 1
        return data



###########################################################################################################
###########################################################################################################


