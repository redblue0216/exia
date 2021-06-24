# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个具体的构建者模式实现类，主要用于实现具体的功能。
"""
模块介绍
-------

    这是一个具体的构建者模式实现类，主要用于实现具体的功能。

功能
----

    具体实现的功能：   

        （1）DataBaseConnect       

        （2）StoreProcedureCall                                                                                                                 

类说明
-----

"""



####### 载入程序包 #########################################################
############################################################################



from abc import ABCMeta,abstractmethod
from composite_mode_base import *
from composite_mode_realization import *



####### 构建者模式实现类 #####################################################
### 具体实现的功能：                                                      ###
### （1）DataBaseConnect                                                 ###
### （2）StoreProcedureCall                                               ###
############################################################################



###### 构建者模式具体实现抽象类 ################################################
##############################################################################



class ProductBuilder(metaclass = ABCMeta):
    """
    类介绍：

        这是一个构建抽象类
    """


    @abstractmethod
    def buildProduct(self):
        pass



###### 数据库连接具体实现类 ######################################################
################################################################################



class DataBaseConnectBuilder(ProductBuilder):
    """
    类介绍：

        这是一个DataBaseConnect构建者具体实现类，主要用于组合各种配件
    """


    def buildProduct(self):
        """
        方法功能：

            定义一个组合各种功能配件的函数,主要用于返回数据库
        """

        print("DataBaseConnectComposite build done!")
        DataBaseConnectComposite = Composite_DataBaseConnect('DataBaseConnect')
        DataBaseConnectComposite.addComponent(Component_DataBaseConnect)

        return DataBaseConnectComposite



###### 存储过程调用具体实现类 #######################################################
###################################################################################



class StoreProcedureCallBuilder(ProductBuilder):
    """
    类介绍：

        这是一个StoreProcedureCall构建者具体实现类，主要用于组合各种配件
    """


    def buildProduct(self):
        """
        方法功能：
        
            定义一个组合各种功能配件的函数,主要用于返回存储过程调用
        """

        print("StoreProcedureCallComposite build done!")
        StoreProcedureCallComposite = Composite_StoreProcedureCall('StoreProcedureCall')
        StoreProcedureCallComposite.addComponent(Component_StoreProcedureCall)

        return StoreProcedureCallComposite



########################################################################################
########################################################################################


