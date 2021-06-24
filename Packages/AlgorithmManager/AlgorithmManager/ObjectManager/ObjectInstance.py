# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个功能对象实例类，主要用于生成向对象池存储的对象实例，使用的技术有描述符技术，回调技术，eval,exec和单例模式
"""
模块介绍
-------

这是一个功能对象实例类，主要用于生成向对象池存储的对象实例，使用的技术有描述符技术，回调技术，eval,exec和单例模式

    功能：            

        （1）生成对象实例        

        （2）对象存储     

        （3）对象方法运行                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from AlgorithmManager.utils.descriptor import *
from AlgorithmManager.ObjectManager.ObjectGenerater import *
from AlgorithmManager.utils.transform import *
from AlgorithmManager.utils.builder import *



####### 对象实例类 ###########################################################
### 功能：                                                                 ###
### （1）生成对象实例                                                       ###
### （2）对象存储                                                          ###
### （3）对象方法运行                                                      ###
#############################################################################



####### 对象实例类 ####################################################################################
######################################################################################################



@entity
class ObjectInstance(object):
    """
    类介绍：

        这是一个对象实例类，主要用于生成向对象池存储的对象实例。使用的技术有描述符技术，回调技术，eval,exec和单例模式
    """


    __instance = None
    __isFirstInit = False
    input_parameter = Descriptor()
    handler = DescriptorClass()
    output_parameter = Descriptor()
    

    def __new__(cls,name,input_parameter,output_parameter,handler):
        """
        属性方法功能：

            复写一个类构造的魔法方法，实现单例构造
        
        参数：
            cls (object)：对象
            name (object)：实例名称
            input_parameter (objcet)：输入参数，数据类型Dict
            output_parameter (object)：输出参数，数据类型Dict
            handler (object)：对象DAG，数据类型自定义类
        """

        if not cls.__instance:
            ObjectInstance.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self,name,input_parameter,output_parameter,handler):
        """
        属性方法功能：

            定义一个初始化方法，在属性构造魔法方法中加入单例控制的逻辑
        
        参数：
            name (str)：实例名称
            input_parameter (str)：输入参数，数据类型Dict
            output_parameter (str)：输出参数，数据类型Dict
            handler (object)：对象DAG，数据类型自定义类
        """

        if not self.__isFirstInit:
            self.__name = name
            ObjectInstance.__isFirstInit = True
        self.input_parameter = input_parameter
        self.output_parameter = output_parameter
        self.handler = handler
        self.object_model = None


    def getName(self):
        """
        方法功能：

            定义个获取类名字的方法
        """

        return self.__name


    def gen(self,ObjectDag):
        """
        方法功能：

            定义一个在生成对象后调用对象方法的方法

        参数：
            ObjectDag (object)：对象DAG，数据类型自定义类
        """

        ObjectDagParameters = ObjectDag.feature()
        eval_dict = ObjectDagParameters['eval_dict']
        tmp_rep = ObjectDagParameters['tmp_rep']
        startLabel = ObjectDagParameters['startLabel']
        outputLabel = ObjectDagParameters['outputLabel']
        object_model = ObjectGenerater.gen(eval_dict,tmp_rep,startLabel,outputLabel)
        self.object_model = object_model
        return self.object_model


    def run(self,run_sentence,run_type):
        """
        方法功能：

            定义一个在生成对象后运行各种方法的接口方法

        参数：
            run_sentence (str)：运行语句
            run_type (str)：运行类型
        """

        if run_type == 'NoReturn':
            exec(str('self.object_model.{}'.format(run_sentence)))
            return 'Run Susseceful!'
        elif run_type == 'Return':
            result = eval(str('self.object_model.{}'.format(run_sentence)))
            return result



##############################################################################################
##############################################################################################


