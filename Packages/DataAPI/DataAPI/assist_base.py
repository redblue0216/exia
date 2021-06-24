# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个辅助类，主要为DataAPI提供一些辅助功能
"""
模块介绍
-------

这是一个辅助类，主要为DataAPI提供一些辅助功能

功能
----

    （1）输入参数辅助                                    

    （2）Fixed_DataBaseConnect_config_dict                             

类说明
-----

"""



####### 载入程序包 ##########################################################
############################################################################



import pymysql



####### 辅助类 #############################################################
### 功能：                                                               ###
### （1）输入参数辅助                                                     ###
### （2）Fixed_DataBaseConnect_config_dict                               ###
############################################################################



####### 输入参数辅助类 ##########################################################################
################################################################################################



class InputParameters(object):
    """
    类介绍：

        这是一个输入参数辅助类

        使用技术：
        @property，支持类属性自由读写
    """


    @property
    def paramters_dict(self):
        """
        方法功能：

            参数存储，采用@property技术。
            注意：这里的下划线不能少，因为方法名和属性名一致，需要区分，否则会频繁调用getter出现死循环！
        """

        return self._parameters_dict


    @paramters_dict.setter
    def paramters_dict(self,value):
        """
        方法功能：

            参数输入接口函数，采用@property技术，
            注意，这里的下划线也不能少，因为方法名和属性名一致，需要区分，否则会频繁调用setter出现死循环！
        """

        self._parameters_dict = value



#####################################################################################################
#####################################################################################################


