# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个构建模式的基础类，主要包含构建者，指挥者和产品三个关键点。
"""
模块介绍
-------

    这是一个构建模式的基础类，主要包含构建者，指挥者和产品三个关键点。

功能
----

    设计模式：

        （1）构建者模式

        （2）组合模式(需要接入的)                                             
    关键点：    

        （1）建构类的管理类（指挥者）       

        （2）具体的构建类（构建者）   

        （3）实现具体功能的组件模式   

    具体实现的功能：          

        （1）DataBaseConnect      
                                                
        （2）StoreProcedureCall                                                                     

类说明
-----

"""



####### 载入程序包 #########################################################
############################################################################



from abc import ABCMeta,abstractmethod
from builder_mode_realization import *



####### 构建者模式类 #######################################################
### 设计模式：                                                           ###
### （1）构建者模式                                                      ###
### （2）组合模式(需要接入的)                                             ###
### 关键点：                                                             ###
### （1）建构类的管理类（指挥者）                                         ###
### （2）具体的构建类（构建者）                                           ###
### （3）实现具体功能的组件模式                                          ###
### 具体实现的功能：                                                     ###
### （1）DataBaseConnect                                                 ###
### （2）StoreProcedureCall                                              ###
############################################################################



####### 构建管理类 ###########################################################
#############################################################################



class BuildManger(object):
    """
    类介绍：

        这是一个构建模式的管理类，充当指挥者的角色

            主要功能：

            （1）DataBaseConnect

            （2）数据库接入
    """


    def __init__(self):
        """
        属性方法功能：

            定义一个初始化属性的函数，目前功能类

            （1）DataBaseConnect

            （2）数据库
        """

        self.__DataBaseConnectBuilder = DataBaseConnectBuilder()
        self.__StoreProcedureCallBuilder = StoreProcedureCallBuilder()


    def buildDataBaseConnect(self):
        """
        方法功能：

            定义一个构建DataBaseConnect最终产品的函数，主要由组合模式中的各个组件和组合配件提供功能支持
        """


        DataBaseConnectProduct = self.__DataBaseConnectBuilder.buildProduct()
        
        return DataBaseConnectProduct


    def buildStoreProcedureCall(self):
        """
        方法功能：

            定义一个构建StoreProcedureCall最终产品的函数，主要由组合模式中的各个组件和组合配件提供功能支持
        """


        StoreProcedureCallProduct = self.__StoreProcedureCallBuilder.buildProduct()

        return StoreProcedureCallProduct



########################################################################################
########################################################################################


