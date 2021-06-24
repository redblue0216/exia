# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个数据库API基础操作类，利用构建者模式和组合模式创造的几个功能组件实现一系列的数据库的操作
"""
模块介绍
-------

    这是一个数据库API基础操作类，利用构建者模式和组合模式创造的几个功能组件实现一系列的数据库的操作

功能
----

    主要技术：                               

        （1）初始化中执行部分构建操作，如authority        

    主要功能：                        

        （1）初始化即登录数据库    

        （2）退出               

        （3）调用存储过程查询                                                                                                                                                                                                                                                            

类说明
-----

"""



####### 载入程序包 #########################################################
############################################################################



from builder_mode_base import *
from builder_mode_realization import *
from composite_mode_base import *
from composite_mode_realization import *
from assist_base import *
import pymysql



###### 数据库API基础操作类 ##########################################################
### 主要技术：                                                                   ###
### （1）初始化中执行部分构建操作，如authority                                     ###
### 主要功能：                                                                   ###
### （1）初始化即登录数据库                                                       ###
### （2）退出                                                                    ###
### （3）调用存储过程查询                                                         ###
####################################################################################



class DataBaseAPI_base(object):
    """
    类介绍：

        这是一个数据库API基础操作类，利用构建者模式和组合模式创造的几个功能组件实现一系列的数据库的操作，目的是为了灵活配置各种操作

           主要功能：（1）初始化即登录数据库（2）退出（3）调用存储过程查询
    """


    def __init__(self,user,passwd,host,port,db,charset):
        """
        属性方法功能：

            定义一个初始化登录数据库的函数，一些操作在初始化中进行。

        参数：
               user (str)：用户ID
               passwd (str)：用户密码
            host (str)：host
            port {int}: port
            db (str): 数据库
            charset (str): 编码类型
        
        返回：
           返回：无返回
        """

        self.user = user 
        self.passwd = passwd
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset
        Input_config_dict = {
            'user' : self.user,
            'passwd' : self.passwd
        }
        Fixed_DataBaseConnect_config_dict = {
            'host' : self.host,
            'port' : self.port,
            'db' : self.db,
            'charset' : self.charset,
            'cursorclass' : pymysql.cursors.DictCursor ###  指定类型
        }
        self.Fixed_DataBaseConnect_config_dict = Fixed_DataBaseConnect_config_dict
        self.DataBaseConnect_config_dict = {**Input_config_dict,**Fixed_DataBaseConnect_config_dict} ### 利用**合并两个字典
        self.BuildManger = BuildManger()
        self.DBAPI = self.authority() ### self属性调用方法时有顺序的
        

    def authority(self):
        """
        方法功能：

            定义一个创建数据连接和游标的函数
        
        参数：
            无参数

        返回：
           authority (Dict): 数据库连接connect,游标cursor
        """

        DataBaseConnect_config_dict = self.DataBaseConnect_config_dict
        DataBaseConnect_object = self.BuildManger.buildDataBaseConnect()
        DataBaseConnect_object.feature(run_mode = 'select_execution',
                                    selected_component = 'DataBaseConnect',
                                    DataBaseConnect_config_dict = DataBaseConnect_config_dict)
        ### 获取连接
        connect = DataBaseConnect_object._result['connect']
        ### 获取游标
        cursor = DataBaseConnect_object._result['cursor']
        authority_dict = {
            'connect' : connect,
            'cursor' : cursor
        }

        return authority_dict


    def exit(self):
        """
        方法功能：

            定义一个退出的函数
        
        参数：
            无参数
           
        返回：
            无返回
        """

        self.DBAPI['cursor'].close()
        self.DBAPI['connect'].close()
        

    def query(self,InputParameters_dict):
        """
        方法功能：

            定义一个查询的函数，主要通过调用存储过程实现数据的查询
        
        参数：
               InputParameters_dict (Dict)：输入参(args：存储过程的参数，procname：存储过程名字)
        
        返回：
           data (DataFrame)：data查询的数据
        """

        StoreProcedureCall_object = self.BuildManger.buildStoreProcedureCall()
        StoreProcedureCall_object.feature(run_mode = 'select_execution',
                                        selected_component = 'StoreProcedureCall',
                                        cursor = self.DBAPI['cursor'],
                                        InputParameters_dict = InputParameters_dict)
        data = StoreProcedureCall_object._result['data']

        return data



##############################################################################################################
##############################################################################################################


