# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个组合模式的基础类，主要包含单个组件和组合配件两个关键点。
"""
模块介绍
-------

    这是一个组合模式的基础类，主要包含单个组件和组合配件两个关键点。

功能
----

    设计模式：            

        （1）组合模式                                                       
    关键点：             

        （1）单个功能组件      

        （2）综合功能复合组件      

    具体实现的功能：             

        （1）DataBaseConnect        
                                               
        （2）StoreProcedureCall                                                                                                                                                            

类说明
-----

"""



####### 载入程序包 #########################################################
############################################################################



from abc import ABCMeta,abstractmethod
import pymysql



####### 组合模式类 ########################################################
### 设计模式：                                                          ###
### （1）组合模式                                                       ###
### 关键点：                                                           ###
### （1）单个功能组件                                                   ###
### （2）综合功能复合组件                                               ###
### 具体实现的功能：                                                    ###
### （1）DataBaseConnect                                               ###
### （2）StoreProcedureCall                                            ###
##########################################################################



####### 单个功能组件类 ###########################################################
#################################################################################



class Component(metaclass = ABCMeta):
    """
    类介绍：

        这是一个组件类，提供单个功能。
    """


    def __init__(self,name):
        """
        属性方法功能：

            定义一个初始化组件名称的属性函数
        """

        self._name = name


    def getName(self):
        """
        方法功能：

            定义一个获取组件类名称的函数
            返回：组件名称
        """

        return self._name


    def isComposite(self):
        """
        方法功能：

            定义一个判断是否是组合配件的函数
            返回：True or False
        """

        return False


    @abstractmethod
    def feature(self):
        """
        方法功能：

            定义一个组件功能实现的抽象函数接口
        """

        pass



####### 综合功能复合组件类 ############################################################
#####################################################################################



class Composite(Component):
    """
    类介绍：

        这是一个复合组件类，提供组合的综合功能
    """


    def __init__(self,name):
        """
        属性方法功能：

            定义一个初始化组件名称的属性函数
        """

        super().__init__(name)
        self._components = []
        self._result = {}


    def addComponent(self,component):
        """
        方法功能：

            定义一个添加单个功能组件类的函数
        
        参数：   	
            component (object)：单个功能组件类
        
        返回：
               返回：无返回
        """

        self._components.append(component)


    def removeComponent(self,component):
        """
        方法功能：

            定义一个删除单个功能组件类的函数

        参数：   	
            component (object)：单个功能组件类

        返回：
               返回：无返回
        """

        self._components.remove(component)


    def isComposite(self):
        """
        方法功能：

            定义一个判断是否是组合配件的函数
        """

        return True 


    def feature(self,run_mode,**kwargs):
        """
        方法功能：

            定义一个组件功能实现的抽象函数接口，依次执行单个组件的功能
        
        参数：
           run_mode (str)：运行模式
           kwargs (str)：可变参数收集（selected_component为选择的组件名称）

        返回：
           返回：无返回，将结果存入类属性_result中
        """
        if run_mode == 'serial_execution':
            print(run_mode)
            for component in self._components:
                component.feature(component,**kwargs) ### 类方法调用必须指明对象类self
        elif run_mode == 'select_execution':
            print(run_mode)
            selected_component_str = str(kwargs['selected_component'])
            for component in self._components:
                component_name = component.getInstanceName(component) ### 为了避免全局变量的复写，实现类的信息由函数直接返回引入
                if component_name == selected_component_str:
                    component_result = component.feature(component,**kwargs)
                    self._result['data'] = component_result
                    return component_result
                else:
                    continue 



#####################################################################################################################################
#####################################################################################################################################


