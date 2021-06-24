# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个图算法类，主要实现了图的拓扑排序和DFS算法
"""
模块介绍
-------

这是一个图算法类，主要实现了图的拓扑排序和DFS算法

    功能：    

        （1）拓扑排序算法                                                       

        （2）DFS算法                                                                                                                                                                                                                                                                                                            

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from AlgorithmManager.GraphDataFrame.linkedstack import LinkedStack 



####### 图算法函数 #############################################################
### 功能：                                                                 ###
### （1）拓扑排序算法                                                       ###
### （2）DFS算法                                                           ###
##############################################################################



####### 拓扑排序算法 ##############################################################################
##################################################################################################



def topoSort(g,startlabel = None):
    """
    函数功能：

        定义一个图的图拓扑排序算法
    """

    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs(g,v,stack)
    return stack

    

####### DFS算法 ####################################################################################
####################################################################################################



def dfs(g,v,stack):
    """
    函数功能：

        定义一个图的DFS算法
    """
    
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g,w,stack)
    stack.push(v)



####### 最短路径算法 ####################################################################################
########################################################################################################



def shortestPaths(g,startLabel):
    return ["Under development"]



####### 最小生成树 ######################################################################################
########################################################################################################



def spanTree(g,startLabel):
    return ["Under development"]



#########################################################################################################
#########################################################################################################

