# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个参数管理器构建类
"""
模块介绍
-------

这是一个参数管理器构建类

    功能：    

        （1）参数管理构建                                                       

        （2）参数收集                                                          

        （3）参数存储                                                                                                                                                                 

类说明
------

"""


####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractmethod



####### 参数管理器 ###########################################################
### 功能：                                                                 ###
### （1）参数管理构建                                                       ###
### （2）参数收集                                                          ###
### （3）参数存储                                                          ###
#############################################################################



####### 参数存储基础类 ################################################################################
######################################################################################################



class ParameterStorage(object):
    """
    类介绍：

        这是一个参数存储类
    """


    def __init__(self,name):
        """
        属性方法功能：

            这是一个初始化方法

        参数：
            name (str)：参数存储器名称
        """

        self._name = name
        self.components = dict()


    def getName(self):
        """
        方法功能：

            定义一个获取参数存储器的名称
        """

        return self._name


    def addComponent(self,component,component_name):
        """
        方法功能：

            定义一个添加组件的方法
        """

        self.components[component_name] = component


    @abstractmethod
    def feature(self):
        """
        方法功能：

            定义一个特征抽象方法
        """

        pass



####### 参数存储构建类 ################################################################################
######################################################################################################



class ParameterStorageBuilder(metaclass = ABCMeta):
    """
    类介绍：

        这是一个参数管理器构建类
    """


    @abstractmethod
    def buildProduct(self):
        """
        方法功能：

            定义一个构建逻辑方法
        """

        pass



####### 构建管理器类 ##################################################################################
######################################################################################################



class BuilderManager(object):
    """
    类介绍：

        这是一个构建管理器类
    """


    def __init__(self):
        """
        属性方法功能：

            定义一个初始化方法
        """

        self.__ObjectDagBuilder = ObjectDagBuilder()


    def buildObjectDag(self,eval_dict,tmp_rep,startLabel,outputLabel):
        """
        方法功能：

            定义一个构建对象DAG方法
        """

        ObjectDag = self.__ObjectDagBuilder.buildProduct(eval_dict,tmp_rep,startLabel,outputLabel)
        return ObjectDag



####### 对象DAG参数存储类 #############################################################################
######################################################################################################



class ObjectDagParameterStorage(ParameterStorage):
    """
    类介绍：

        这是一个对象DAG参数存储器具体实现类
    """


    def feature(self):
        """
        方法功能：

            定义一个特征具体实现类
        """

        return self.components



####### 对象DAG参数存储类 #############################################################################
######################################################################################################



class ObjectDagBuilder(ParameterStorageBuilder):
    """
    类介绍：

        这是一个对象DAG构建类
    """


    def buildProduct(self,eval_dict,tmp_rep,startLabel,outputLabel):
        """
        方法功能：

            定义一个构建实际对象的具体逻辑方法
        """

        ObjectDag = ObjectDagParameterStorage('对象DAG参数存储')
        ObjectDag.addComponent(eval_dict,'eval_dict')
        ObjectDag.addComponent(tmp_rep,'tmp_rep')
        ObjectDag.addComponent(startLabel,'startLabel')
        ObjectDag.addComponent(outputLabel,'outputLabel')
        return ObjectDag


#######################################################################################################
#######################################################################################################


