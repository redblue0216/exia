# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个对象池类，主要用于存储算法平台的各个算法组件。使用的技术有：对象池技术和上下文管理器技术
"""
模块介绍
-------

这是一个对象池类，主要用于存储算法平台的各个算法组件。使用的技术有：对象池技术和上下文管理器技术

    功能：        

        （1）算法组件对象存储     

        （2）算法组件对象使用    

        （3）算法组件对象管理                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



####### 对象池 ###############################################################
### 功能：                                                                 ###
### （1）算法组件对象存储                                                   ###
### （2）算法组件对象使用                                                   ###
### （3）算法组件对象管理                                                   ###
##############################################################################



####### 池化对象基础类 ################################################################################
######################################################################################################



class PooledObject(object):
    """
    类介绍：

        这是一个池化对象类，主要用于将一个类对象池化，以放入对象池存储调用。
    """
    

    def __init__(self,obj):
        """
        属性方法功能：

            定义一个初始化方法

        参数：
            obj (object)：具体的类对象
            __busy (bool)：是否被占用
        """

        self.__obj = obj
        self.__busy = False


    def getObject(self):
        """
        方法功能：

            定义一个获取对象的方法
        """

        return self.__obj


    def setObject(self,obj):
        """
        方法功能：
            定义一个设置对象的方法

        参数：
            obj (object)：组件对象
        """

        self.__obj = obj


    def isBusy(self):
        """
        方法功能：

            定义一个获取对象是否调用状态的方法
        """

        return self.__busy


    def setBusy(self,busy):
        """
        方法功能：

            定义一个设置对象调用状态的方法
        """

        self.__busy = busy 


####### 对象池类 ######################################################################################
######################################################################################################



class ObjectPool(object):
    """
    类介绍：

        这是一个对象池类，主要用于存储算法平台各个功能组件。使用的技术有：（1）对象池技术（2）上下文管理器技术
    """


    def __init__(self,name):
        """
        属性方法功能：

            定义一个对象池字典和管理对象池进入退出的方法

        参数：
            name (str)：对象池名称
        """

        self.__pools = dict()
        self.entered = False
        self.name = name
        self.function = None


    def createPooledObject(self,obj):
        """
        方法功能：

            定义一个创建池化对象的方法

        参数：
            obj (class)：目标池化对象

        返回：
            返回 (class)：池化后的对象
        """

        PooledObj = PooledObject(obj)
        return PooledObj


    def borrowObject(self,obj_name):
        """
        方法功能：

            定义一个借用对象的方法
        
        参数：
            obj_name (str)：被借用的对象名称

        返回：
            返回 (class)：返回要借用的对象
        """

        obj = self._findFreeObject(obj_name)
        return obj


    def returnObject(self,obj_name):
        """
        方法功能：

            定义一个归还对象的方法

        参数：
           obj_name (str)：要归还对象的名称
        """

        self.__pools[obj_name].setBusy(True)


    def addObject(self,obj,obj_name):
        """
        方法功能：

            定义一个添加新对象的方法

        参数：
            obj (class)：添加的对象实例
            obj_name (str)：添加的对象名称
        
        返回：
            返回 (str)：添加成功的字符串文本
        """

        PooledObj = self.createPooledObject(obj)
        self.__pools[obj_name] = PooledObj
        return 'AddObject successful!'


    def clear(self):
        """
        方法功能：

            定义一个清空对象池的方法
        """

        self.__pools.clear()


    def getObjectPool(self):
        """
        方法功能：

            定义一个获取对象池的方法
        
        返回：
               返回 (object)：返回对象池
        """

        return self.__pools


    def _findFreeObject(self,obj_name):
        """
        方法功能：

            定义一个查找空闲对象的方法
        
        参数：
            obj_name (str)：要查找的空闲对象名称
        
        返回：
            返回 (class)：空闲的目标对象
        """
        
        obj = None
        if not self.__pools[obj_name].isBusy():
            obj = self.__pools[obj_name].getObject()
            self.__pools[obj_name].setBusy(True)
        return obj


    def __enter__(self):
        """
        属性方法功能：

            复写一个进入操作的魔法方法,用来控制对象池启停状态和初始行为（该协议方法只能包含self对象自身）

        返回：
            返回：self对象自身，若要使用with...as...必需返回self
        """

        self.entered = True
        return self


    def __exit__(self,exc_type,exc_instance,traceback):
        """
        属性方法功能：

            复写一个退出操作的魔法方法，用来控制对象池的退出行为

        参数：
            self (object)：对象自身
            exc_type (str)：执行类型
            exc_instance (object)：执行实例
            traceback (object)：循迹
            （四个参数必须）
        """

        self.clear()
        self.entered = False



###############################################################################################
###############################################################################################


