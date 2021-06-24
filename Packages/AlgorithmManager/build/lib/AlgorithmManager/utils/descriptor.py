# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个描述符工具类，主要用于构建描述符机制。
"""
模块介绍
-------

这是一个描述符工具类，主要用于构建描述符机制。

    功能：       

        （1）属性托管                                                          

        （2）方法绑定                                                          

        （3）预先检查                                                                                                         

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import abc 



####### 描述符类 #############################################################
### 功能：                                                                 ###
### （1）属性托管                                                          ###
### （2）方法绑定                                                          ###
### （3）预先检查                                                          ###
#############################################################################



####### 描述符基础类 ##################################################################################
######################################################################################################



class AutoStorage(object):
    """
    类介绍：

        这是一个描述符基础类，是一个覆盖型描述符。
    """


    __counter = 0


    def __init__(self):
        """
        属性方法功能：

            定义一个初始化方法
        
        参数：
            storage_name (str)：具体的行为操作
        """

        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix,index)
        cls.__counter += 1


    def __get__(self,instance,owner):
        """
        属性方法功能：

            定义一个获取的协议，用来执行具体的行为操作

        参数：
            self (object)：描述符实例本身
            instance (object)：调用描述符的具体实例即访问属性所属的实例
            owner (object)：描述符附加到的类
        """

        if instance is None:
            return self
        else:
            return getattr(instance,self.storage_name)


    def __set__(self,instance,value):
        """
        属性方法功能：

            定义一个设置的协议，用来动态设置实例属性
        
        参数：
            self (object)：描述符实例本身
            instance (object)：调用描述符的具体实例即访问属性所属的实例
            owner (object)：描述符附加到的类
        """

        setattr(instance,self.storage_name,value)



####### 带审查功能的描述符类 ##################################################################################
#############################################################################################################



class Validated(abc.ABC,AutoStorage):
    """
    类介绍：

        这是一个带有审查功能的描述符抽象基类
    """


    def __set__(self,instance,value):
        """
        属性方法功能：

            定义一个设置的协议，用来动态设置实例属性
        
        参数：
            self (object)：描述符实例本身
            instance (object)：调用描述符的具体实例即访问属性所属的实例
            owner (object)：描述符附加到的类
        """

        value = self.validate(instance,value)
        super().__set__(instance,value)


    @abc.abstractmethod
    def validate(self,instance,value):
        """
        方法功能：

            定义一个具体的审查函数，此处为抽象方法
        """

        pass



####### 自动检索类属性名的装饰器 ##################################################################################
#################################################################################################################



def entity(cls):
    """
    函数功能：

        定义一个动态索引实例名称和属性的装饰器
    参数：
        cls (object)：目标对象类
    """

    for key,attr in cls.__dict__.items():
        if isinstance(attr,Validated):
            type_name = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name,key)
    return cls



####### 带审查功能的描述符具体实现类 ##################################################################################
#####################################################################################################################



class Descriptor(Validated):
    """
    类介绍：

        这是一个具有检查类型功能的描述符类
    """


    def validate(self,instance,value):
        """
        方法功能：

            定义一个具体的检查函数
        
        参数：
            instance (object)：具体实例对象
            value (object)：具体的属性值
        
        返回：
            返回 (object)：具体的属性值/报错
        """

        if not type(value) == dict:
            raise TypeError('value must be dict!')
        return value



class DescriptorClass(Validated):
    """
    类介绍：

        这是一个具有检查类的类型功能的描述符类
    """


    def validate(self,instance,value):
        """
        方法功能：

            定义一个具体的检查函数
        
        参数：
            instance (object)：具体实例对象
            value (object)：具体的属性值

        返回：
            返回 (object)：具体的属性值/报错
        """

        if not str(type(value)) == "<class 'AlgorithmManager.utils.builder.ObjectDagParameterStorage'>":
            raise TypeError('value must be dict!')
        return value



class Quantity(Validated):
    """'
    类介绍：

        这是一个具有检查属性值范围功能的描述符类
    """
     

    def validate(self,instance,value):
        """
        方法功能：

            定义一个具体的检查函数
        
        参数：
            instance (object)：具体实例对象
            value (object)：具体的属性值

        返回：
            返回 (object)：具体的属性值/报错
        """

        if value <= 0:
            raise ValueError('value must be > 0')
        return value



class NonBlank(Validated):
    """
    类介绍：

        这是一个具有检查数据是否为空功能的描述符类
    """

    def validate(self,instance,value):
        """
        方法功能：

            定义一个具体的检查函数

        参数：
            instance (object)：具体实例对象
            value (object)：具体的属性值

        返回：
            返回 (object)：具体的属性值/报错
        """

        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value



#######################################################################################################################
#######################################################################################################################


