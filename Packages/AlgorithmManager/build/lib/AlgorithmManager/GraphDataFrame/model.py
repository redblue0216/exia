# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个图模型类，主要用于管理功能对象生产过程的DAG，使用的技术有描述符技术。
"""
模块介绍
-------

这是一个图模型类，主要用于管理功能对象生产过程的DAG，使用的技术有描述符技术。

    功能： 

        （1）创建图        

        （2）获取图         

        （3）获取初始端点                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from AlgorithmManager.GraphDataFrame.graph import LinkedDirectedGraph
from AlgorithmManager.utils.descriptor import *



####### 图数据结构类 #############################################################
### 功能：                                                                    ###
### （1）创建图                                                               ###
### （2）获取图                                                               ###
### （3）获取初始端点                                                         ###
################################################################################



####### 图模型类类 ################################################################################
##################################################################################################



@entity
class GraphDemoModel(object):
    """
    类介绍：

        这是一个图模型类，主要用于管理功能对象生产过程的DAG，使用的技术有描述符技术。
    """


    eval_dict = Descriptor()


    def __init__(self,eval_dict):
        """
        属性方法功能：

            定义一个初始化函数

        参数：
            _graph (object)：图对象
            _startlabel (object)：开始的节点
        """

        self._graph = None
        self._startLabel = None
        self.eval_dict = eval_dict


    def createGraph(self,rep,startLabel):
        """
        方法功能：

            定义一个创建图的方法
        """

        self._graph = LinkedDirectedGraph()
        self._startLabel = startLabel
        edgeList = rep.split()
        for edge in edgeList:
            if not '>' in edge:
                if not self._graph.containsVertex(edge):
                    self._graph.addVertex(edge)
                else:
                    self._graph = None
                    return "Duplicate vertex"
            else:
                bracketPos = edge.find('>')
                colonPos = edge.find(':')
                if bracketPos == -1 or colonPos == -1 or \
                   bracketPos > colonPos:
                    self._graph = None
                    return "Problem with > or :"
                fromLabel = edge[:bracketPos]
                toLabel = edge[bracketPos + 1:colonPos]
                weight = edge[colonPos + 1:]
                if weight.isdigit():
                    weight = int(weight)
                if not self._graph.containsVertex(fromLabel):
                    self._graph.addVertex(fromLabel)
                if not self._graph.containsVertex(toLabel):
                    self._graph.addVertex(toLabel)
                if self._graph.containsEdge(fromLabel, toLabel):
                    self._graph = None
                    return "Duplicate edge"
                self._graph.addEdge(fromLabel, toLabel, weight)
        vertex = self._graph.getVertex(startLabel)
        if vertex is None:
            self._graph = None
            return "Start label not in graph"
        else:
            vertex.setMark()
            return "Graph created successfully"


    def getGraph(self):
        """
        方法功能：

            定义一个获取图的方法
        """

        if not self._graph:
            return None
        else:
            return str(self._graph)


    def getStartLabel(self):
        """
        方法功能：

            定义一个获取开始标签的方法
        """

        return self._startLabel

    def run(self,algorithm):
        """
        方法功能：

            定义一个运行一种图算法的方法
        """

        if self._graph is None:
            return None
        else:
            return algorithm(self._graph, self._startLabel)



#############################################################################################
#############################################################################################


