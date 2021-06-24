# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个图数据结构类，主要包括链接边，链接顶点和链接图三个功能类，使用链接表技术。
"""
模块介绍
-------

这是一个图数据结构类，主要包括链接边，链接顶点和链接图三个功能类，使用链接表技术。

    功能：             

        （1）链接边      

        （2）链接顶点    
                                                                 
        （1）链接图                                                                                                                                                                                                                                                                                                                                                                         

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from AlgorithmManager.GraphDataFrame.abstractcollection import AbstractCollection



####### 图数据结构类 #############################################################
### 功能：                                                                    ###
### （1）链接边                                                               ###
### （2）链接顶点                                                             ###
### （1）链接图                                                               ###
################################################################################



####### 链接边类 ##################################################################################
##################################################################################################



class LinkedEdge(object):
    """
    类介绍：

        这是一个链接表实现的图边类
    """
    

    def __init__(self,fromVertex,toVertex,weight = None):
        """
        属性方法功能：

            定义一个初始化函数
        
        参数：
            fromVertex (str)：起点
            toVertex (str)：终点
            weight (str)：权重
            _mark (str)：标记
        """         

        self._vertex1 = fromVertex
        self._vertex2 = toVertex
        self._weight = weight 
        self._mark = False
    

    def clearMark(self):
        """
        方法功能：

            定义一个清空标记的方法
        """

        self._mark = False
    

    def __eq__(self,other):
        """
        属性方法功能：

            定义一个等式判断的魔法方法
        """

        if self is other: return True
        if type(self) != type(other):
            return False
        return self._vertex1 == other._vertex1 and \
               self._vertex2 == other._vertex2
    

    def getOtherVertex(self,thisVertex):
        """
        方法功能：

            定义一个获取其他顶点的方法
        """

        if thisVertex == None or thisVertex == self._vertex2:
            return self._vertex1
        else:
            return self._vertex2


    def getToVertex(self):
        """
        方法功能：

            定义一个获取目标顶点的方法
        """

        return self._vertex2
    

    def getWeight(self):
        """
        方法功能：

            定义一个获取权重的方法
        """

        return self._weight
    

    def isMarked(self):
        """
        方法功能：

            定义一个判断标记的方法
        """

        return self._mark
    

    def setMark(self):
        """
        方法功能：

            定义一个设置标记的方法
        """

        self._mark = True
    

    def setWeight(self,weight):
        """
        方法功能：

            定义一个设置权重的方法
        """

        self._weight = weight     
          

    def __str__(self):
        """
        属性方法功能：

            定义一个字符串函数
        """

        return str(self._vertex1) + ">" + \
               str(self._vertex2)   + ":" + \
               str(self._weight)



####### 链接顶点类 #######################################################################################
#########################################################################################################



class LinkedVertex(object):
    """
    类介绍：

        这是一个链接表实现的图顶点类
    """


    def __init__(self,label):
        """
        属性方法功能：

            定义一个初始化函数

        参数：
            label (str)：顶点标签
            _edgeList (str)：边列表
            _mark (str)：标记
        """

        self._label = label
        self._edgeList = list()
        self._mark = False


    def clearMark(self):
        """
        方法功能：

            定义一个清空标记的函数
        """

        self._mark = False
    

    def getLabel(self):
        """
        方法功能：

            定义一个获取标识的函数
        """

        return self._label
    

    def isMarked(self):
        """
        方法功能：

            定义一个判断是否标记的函数
        """

        return self._mark
    

    def setLabel(self,label,g):
        """
        方法功能：

            定义一个设置标签的函数
        """

        g._vertices.pop(self._label, None)
        g._vertices[label] = self
        self._label = label          


    def setMark(self):
        """
        方法功能：

            定义一个设置标识的函数
        """

        self._mark = True
    

    def __str__(self):
        """
        属性方法功能：

            定义一个字符串魔法方法
        """

        return str(self._label)


    def __eq__(self,other):
        """
        属性方法功能：

            复写一个等式判断的魔法方法
        """

        if self is other: return True
        if type(self) != type(other): return False
        return self.getLabel() == other.getLabel()

    
    def addEdgeTo(self,toVertex,weight):
        """
        方法功能：

            定义一个向顶点链接边的函数
        """

        edge = LinkedEdge(self, toVertex, weight)
        self._edgeList.append(edge)
    

    def getEdgeTo(self,toVertex):
        """
        方法功能：

            定义一个获取目标顶点连接边的函数
        """

        edge = LinkedEdge(self, toVertex)
        try:
            return self._edgeList[self._edgeList.index(edge)]
        except:
            return None


    def incidentEdges(self):
        """
        方法功能：

            定义一个经过一个顶点的边的迭代器
        """

        return iter(self._edgeList)
        
    def neighboringVertices(self):
        """
        方法功能：

            定义一个返回一个顶点临近边的迭代器
        """

        vertices = list()
        for edge in self._edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)
            
    def removeEdgeTo(self,toVertex):
        """
        方法功能：

            定义一个删除目标顶点边的的函数
        """

        edge = LinkedEdge(self, toVertex)
        if edge in self._edgeList:
            self._edgeList.remove(edge)
            return True
        else:
            return False



####### 链接顶点类 #######################################################################################
#########################################################################################################



class LinkedDirectedGraph(AbstractCollection):
    """
    类介绍：

        定义一个链接表实现的图数据结构类
    """


    def __init__(self,sourceCollection = None):
        """
        属性方法功能：

            定义一个初始化函数

        参数：
            _edgeCount (int)：边的个数
            _vertices （Dict)：顶点字典
            AbstractCollection (object)：继承抽象数据类型的属性
        """

        self._edgeCount = 0
        self._vertices = {}
        AbstractCollection.__init__(self, sourceCollection)
        

    def clear(self):
        """
        方法功能：

            定义一个清空图的方法
        """

        self._size = 0
        self._edgeCount = 0
        self._vertices = {}        


    def clearEdgeMarks(self):
        """
        方法功能：

            定义一个清空图标标记的方法
        """

        for edge in self.edges():
            edge.clearMark()
    

    def clearVertexMarks(self):
        """
        方法功能：

            定义一个清空顶点的方法
        """

        for vertex in self.vertices():
            vertex.clearMark()
    

    def sizeEdges(self):
        """
        方法功能：

            定义一个获取边数据量的方法
        """

        return self._edgeCount
    

    def sizeVertices(self):
        """
        方法功能：

            定义一个获取顶点个数的方法
        """

        return len(self)
    

    def __str__(self):
        """
        方法功能：

            复写一个字符串魔法方法
        """

        result = str(self.sizeVertices()) + " Vertices: "
        for vertex in self._vertices:
            result += " " + str(vertex)
        result += "\n";
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result


    def add(self,label):
        """
        方法功能：

            定义一个添加顶点的方法
        """

        self.addVertex(label)

    
    def addVertex(self,label):
        """
        方法功能：

            定义一个添加顶点的具体实现函数
        """

        self._vertices[label] = LinkedVertex(label)
        self._size += 1
        

    def containsVertex (self,label):
        """
        方法功能：

            定义一个是否包含顶点的函数
        """

        return label in self._vertices
    

    def getVertex(self,label):
        """
        方法功能：

            定义一个获取顶点的函数
        """

        return self._vertices[label]
    

    def removeVertex(self,label):
        """
        方法功能：

            定义一个删除顶点的函数
        """

        removedVertex = self._vertices.pop(label, None)
        if removedVertex is None: 
            return False
        
        for vertex in self.vertices():
            if vertex.removeEdgeTo(removedVertex): 
                self._edgeCount -= 1
        for edge in removedVertex.incidentEdges():
            self._edgeCount -= 1           
        self._size -= 1
        return True
    

    def addEdge(self,fromLabel,toLabel,weight):
        """
        方法功能：

            定义一个添加边的函数
        """

        fromVertex = self.getVertex(fromLabel)
        toVertex   = self.getVertex(toLabel)
        fromVertex.addEdgeTo(toVertex, weight)
        self._edgeCount += 1
    

    def containsEdge(self,fromLabel,toLabel):
        """
        方法功能：

            定义一个是否包含边的函数
        """

        return self.getEdge(fromLabel, toLabel) != None
    

    def getEdge(self,fromLabel,toLabel):
        """
        方法功能：

            定义一个获取边的方法
        """

        fromVertex = self.getVertex(fromLabel)
        toVertex   = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)
    

    def removeEdge(self,fromLabel,toLabel): 
        """
        方法功能：

            定义一个删除边的方法
        """

        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)     
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg: 
            self._edgeCount -= 1
        return edgeRemovedFlg

    
    def __iter__(self):
        """
        属性方法功能：

            定义一个实现迭代器的魔法方法
        """

        return self.vertices()


    def edges(self):
        """
        方法功能：

            定义一个实现迭代器的具体方法
        """

        result = list()
        for vertex in self.vertices():
            result += list(vertex.incidentEdges())
        return iter(result)
    

    def vertices(self):
        """
        方法功能：

            定义一个顶点迭代器实现方法
        """

        return iter(self._vertices.values())


    def incidentEdges(self,label):
        """
        方法功能：

            定义一个获取经过顶点的边的函数
        """

        return self.getVertex(label).incidentEdges()
    

    def neighboringVertices(self,label):
        """
        方法功能：

            定义一个获取顶点附近顶点的函数
        """

        return self.getVertex(label).neighboringVertices()



#############################################################################################################
#############################################################################################################


