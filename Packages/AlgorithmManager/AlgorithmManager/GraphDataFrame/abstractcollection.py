# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个抽象数据类，定义了数据结构的一系列基础公共属性和方法
"""
模块介绍
-------

这是一个抽象数据类，定义了数据结构的一系列基础公共属性和方法

    功能：               

        （1）提供基础数据结构的功能                                                                                                                                                                                                      

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



####### 抽象数据类 #############################################################
### 功能：                                                                 ###
### （1）提供基础数据结构的功能                                              ###
##############################################################################



####### 抽象数据类 ##################################################################################
####################################################################################################



class AbstractCollection(object):
    """
    类介绍：

        这是一个抽象数据类，定义了数据结构的一系列基本属性和方法（1）计算长度（2）判空（3）字符串（4）相加（5）相等
    """


    def __init__(self,sourceCollection):
        """
        属性方法功能：

            定义一个从源数据结构种复制元素的初始化方法

        参数：
            sourceCollection (object)：源数据结构
        """

        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)


    def __len__(self):
        """
        属性方法功能：

            定义一个计算数据结构长度的方法
        """

        return self._size


    def isEmpty(self):
        """
        方法功能：

            定义一个判断数据结构是否为空的方法
        """

        return len(self) == 0 
    

    def __str__(self):
        """
        属性方法功能：

            定义一个展示数据结构字符串功能的方法
        """

        return "[" + "，".join(map(str,self)) + "]"


    def __add__(self,other):
        """
        属性方法功能：

            定义一个数据结构相加的方法

        参数：
            other (object)：判断对象

        返回：
            返回 (object)：result相加后结果
        """

        result = type(self)(self)
        for item in other:
            result.add(item)
        return result


    def __eq__(self,other):
        """
        属性方法功能：

            定义一个判断两个数据结构是否相等的方法

        参数：
            other (object)：判断对象

        返回：
            返回 (bool)：True/False
        """
        
        if self is other:
            return True
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        otherItems = iter(other)
        for item in self:
            if item != next(otherItems):
                return False
        return True



####################################################################################################
####################################################################################################


