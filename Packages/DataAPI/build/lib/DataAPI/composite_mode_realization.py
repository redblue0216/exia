# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个具体的组合模式实现类，主要用于实现各种具体功能。
"""
模块介绍
-------

    这是一个具体的组合模式实现类，主要用于实现各种具体功能。

功能
----

    单个组件具体实现的功能： 

        （1）DataBaseConnect    

        （2）StoreProcedureCall     

    复合组件具体实现的功能：         

        （1）DataBaseConnect      

        （2）StoreProcedureCall                                                                                                                                                                                                        

类说明
-----

"""



####### 载入程序包 #########################################################
############################################################################



from abc import ABCMeta,abstractmethod
from DataAPI.composite_mode_base import *
from DataAPI.assist_base import *
import pandas as pd



####### 组合模式实现类 #####################################################
### 单个组件具体实现的功能：                                              ###
### （1）DataBaseConnect                                                 ###
### （2）StoreProcedureCall                                              ###
### 复合组件具体实现的功能：                                              ###
### （1）DataBaseConnect                                                 ###
### （2）StoreProcedureCall                                              ###
############################################################################



####### 组件实现类 ##########################################################################
############################################################################################



class Component_DataBaseConnect(Component):
    """
    类介绍：

        这是一个用于数据库连接的单功能组件
               支持的数据库：
                   （1）MySQL
    """


    def getInstanceName(self):
        """
        方法功能：

            定义一个获得组件实现类名称的方法
        
        返回：
               返回 (str)：组件实现类的实例名称
        """

        return 'DataBaseConnect'


    def feature(self,**kwargs):
        """
        方法功能：

            定义一个数据库连接具体实现的方法
        
        参数：
               DataBseConnect_config_dict (Dict)：数据库连接配置数据

        返回：
           返回：使用Global放入复合组件的属性中
        """

        print("Component_DataBaseConnect Done!")
        ### 获取连接数据库的配置参数
        DataBaseConnect_config_kwargs = kwargs['DataBaseConnect_config_dict']
        ### 创建mysql连接
        global cursor
        global connect
        connect = pymysql.Connect(**DataBaseConnect_config_kwargs)
        ### 获取游标
        cursor = connect.cursor()



class Component_StoreProcedureCall(Component):
    """
    类介绍：

        这是一个存储过程调用的具体实现类	
    """


    def __init__(self):
        """
        属性方法功能：

            定义一个存储组件的数据属性
        """
        self.data = None


    def getInstanceName(self):
        """
        方法功能：

            定义一个获得组件实现类名称的方法

        返回：
            返回：组件实现类的实例名称，数据类型str
        """

        return 'StoreProcedureCall'


    def feature(self,**kwargs):
        """
        方法功能：

            定义一个存储过程调用具体实现的方法

        参数：
               InputParameters_dict (Dict)：对应存储过程的输入参数args和存储过程名字procname

        返回：
               data (DataFrame)：返回存储过程的结果
        """

        print("Component_StoreProcedureCall Done!")
        ### 获取构建好的游标
        StoreProcedureCall_cursor = kwargs['cursor']
        InputParameters_dict = kwargs['InputParameters_dict']
        args= InputParameters_dict['args']
        procname = InputParameters_dict['procname']
        StoreProcedureCall_cursor.callproc(procname = procname, args= args)
        # 返回获得的集合，即存储函数中的 SELECT * FROM tmp; 结果
        result = cursor.fetchall()
        columnDes = cursor.description #获取连接对象的描述信息
        columnNames = [columnDes[i][0] for i in range(len(columnDes))]
        data = pd.DataFrame.from_records(result,columns = columnNames)
        # print(data)

        return data



####### 复合组件实现类 ######################################################################################
############################################################################################################



class Composite_DataBaseConnect(Composite):
    """
    类介绍：

        这是一个用于数据库连接的复合功能组件
               支持的数据库：
                   （1）MySQL
    """


    def feature(self,run_mode,**kwargs):
        """
        方法功能：

            定义一个数据库连接实现的具体方法
               主要使用属性存储连接对象
        """

        super().feature(run_mode,**kwargs)
        self._result['connect'] = connect
        self._result['cursor'] = cursor  
        print(self._result)
        


class Composite_StoreProcedureCall(Composite):
    """
    类介绍：

        这是一个用于存储过程调用的复合功能组件
    """


    def feature(self,run_mode,**kwargs):
        """
        方法功能：

            定义一个存储过程调用的复合功能组件
               主要用于执行各种存储过程
        """

        super().feature(run_mode,**kwargs)



############################################################################################################
############################################################################################################


