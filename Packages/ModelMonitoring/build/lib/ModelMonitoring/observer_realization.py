# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个模型监控模块的实现类，主要提供观察者和被观察者的具体实现类，继承自模型监控模块基础类，采用有限状态机技术
"""
模块介绍
-------

这是一个模型监控模块的实现类，主要提供观察者和被观察者的具体实现类，继承自模型监控模块基础类，采用有限状态机技术

功能
----

    设计模式：  

        （1）监控模式                                                         

    关键技术：

        （1）有限状态机                                                        

    功能：

        （1）监控器                                                           

        （2）控制器                                                           

        （3）执行器                                                                                                                                                                            

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from ModelMonitoring.observer_base import *
from transitions import Machine



####### 模型监控模块具体实现类 ###############################################
### 设计模式：                                                            ###
### （1）监控模式                                                         ###
### 关键技术：                                                            ###
### （1）有限状态机                                                        ###
### 功能：                                                                ###
### （1）监控器                                                           ###
### （2）控制器                                                           ###
### （3）执行器                                                           ###
############################################################################



####### 模型监控模块观察者基础类 ##########################################################################
#########################################################################################################



class ModelMonitoring(Observable):
    """
    类介绍：

        这是一个模型监控器类，主要用于监控模型是否需要重新训练，该监控器采用有限状态机技术，调用transitions包,实现有限状态机的控制器，并将该类修改成执行器。
            
        关键技术：（1）有限状态机.功能：（1）监控器（2）控制器（3）执行器
    """


    states = ['idle','training','trained']
    transitions = [
        {'trigger':'start','source':'idle','dest':'training'},
        {'trigger':'restart','source':'*','dest':'training'},
        {'trigger':'stop','source':'*','dest':'idle'},
        {'trigger':'done','source':'training','dest':'trained'}
    ]


    def __init__(self):
        """
        属性方法功能：

            定义一个初始化方法，主要用来指标数据存储和有限状态机扩展

        参数：
            __index (float)：指标
            machine (object)：有限状态机
        """

        super().__init__()
        self.__index = 0
        self.machine = Machine(model = self,states = ModelMonitoring.states,transitions = ModelMonitoring.transitions,initial = 'idle')


    def getIndex(self):
        """
        方法功能：

            定义一个获取当前指标的方法
            
        返回  
            返回 (float)：指标
        """

        return self.__index


    def setIndex(self,index):
        """
        方法功能：

            定义一个设置当前指标的方法，该输入主要从数据库中扫描得到
            
        参数：   
            index (float)：指标

        返回：
            返回：无返回
        """

        self.__index = index
        print("现在的指标是",self.__index)
        self.notifyObservers()



####### 模型监控模块观察者基础类 ##########################################################################
#########################################################################################################



class UpdateMode(Observer):
    """
    类介绍：

        这是一个更新模型类，主要用于根据事件转换状态，有限状态机事件状态转换

    参数：
        start (str): idle->training
        restart (str): *->training
        stop (str): *->idle
        done (str)：training->trained
    """


    def update(self,observable,object):
        """
        方法功能：

            定义一个更新动作实现的方法

        参数：
            observable (object)：被观察者对象
            object (object)：占位对象

        返回：
            返回：无返回
        """

        if isinstance(observable,ModelMonitoring) and observable.getIndex() >= 0.6:
            observable.start()
        


###########################################################################################################
###########################################################################################################


