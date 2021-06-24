# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个数据服务API封装的具体实现，主要根据业务逻辑将存储过程和PythonAPI对应上
"""
模块介绍
-------

    这是一个数据服务API封装的具体实现，主要根据业务逻辑将存储过程和PythonAPI对应上

功能
----                                                                                                                                                                                                                                                          

类说明
-----

"""



####### 载入程序包 ##########################################################
############################################################################



from database_interface_base import *



####### 数据服务API #############################################################
################################################################################



class DataBaseAPI(DataBaseAPI_base):
    """
    类介绍：

        这是一个数据服务API的具体封装类
    """


    def __init__(self,user,passwd,host,port,db,charset):
        """
        属性方法功能：

            定义一个初始化函数，主要功能都继承自数据库操作基础类
        """

        super().__init__(user,passwd,host,port,db,charset)


    def exec_stored_procedure(self,**kwargs):
        """
        方法功能：
            定义一个实际执行存储过程的函数函数
        
        参数：
               InputParameters_dict (Dict)：场站名称

        返回：
            data (DataFrame)：获取的数据集合
        """

        InputParameters_dict = kwargs['InputParameters_dict']
        data = self.query(InputParameters_dict = InputParameters_dict)
        return data



########################################################################################
########################################################################################


