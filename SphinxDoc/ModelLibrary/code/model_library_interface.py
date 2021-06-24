# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个模型库操作命令的接口类，主要实现采用静态方法
"""
模块介绍
-------

这是一个模型库操作命令的具体实现类，主要实现模型库的一系列操作

功能
----

    主要技术：               

        （1）静态方法

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from command_mode_realization import *
from command_mode_base import *
from assist_base import *
import pymongo
import dill
import pandas as pd 
import numpy as np
from bson.binary import Binary
import paramiko



####### 模型库操作命令实现类 ######################################################
### 设计模式：                                                                 ###
### （1）命令模式                                                              ###
#################################################################################



###### 模型库操作命令基础类 ############################################################
######################################################################################



class ModelLibraryInterface(object):
    """
    类介绍：

        这是一个模型库管理接口类，主要采用静态方法实现
    """

    @staticmethod
    def WriteModel(**kwargs):
        """
        方法功能：

            定义一个写模型的方法

        参数：
            user (str): 用户名
            passwd (str): 密码
            db (str): 数据库名称
            collection_name (str): 数据集名称
            mongodb_config_dict (str): mongodb连接配置参数

                mode (str)：

                （1）direct_operation----可直接运行模式

                model_instance (str): 模型实例
                model_name (str): 模型名称

                （2）trained_model----需要训练模型的模式

                mode_name (str): 模型名称
                mode_type (str): 模型类型
                local_path (str): 本地路径，主要指训练机器路径
                target_path (str): 模型库路径，主要指模型库存储地址，通过assist_base配置

        返回：
            writre_result (str): 执行写模型动作后的结果
        """
        user = kwargs['user']
        passwd = kwargs['passwd']
        db = kwargs['db']
        collection_name = kwargs['collection_name']
        mongodb_config_dict = kwargs['mongodb_config_dict']
        manager = ModelManager(user,passwd,db,collection_name,mongodb_config_dict)
        invoker = ModelInvoker()
        mode = kwargs['mode']
        if mode == 'direct_operation':
            model_instance = kwargs['model_instance']
            model_name = kwargs['model_name']
            write_result = invoker.setCommand(ModelCommand_instance_write_model(manager)).action(mode = mode,
                                                                                        model_instance = model_instance,
                                                                                        model_name = model_name)
            return write_result
        elif mode == 'trained_model_object_store':
            model_name = kwargs['model_name']
            model_type = kwargs['model_type']
            connect_info = kwargs['connect_info']
            access_key = kwargs['access_key']
            secret_key = kwargs['secret_key']
            secure = kwargs['secure']
            object_file = kwargs['object_file']
            bucket = kwargs['bucket']
            write_result = invoker.setCommand(ModelCommand_instance_write_model(manager)).action(mode = mode,
                                                                                        model_name = model_name,
                                                                                        model_type = model_type,
                                                                                        connect_info = connect_info,
                                                                                        access_key = access_key,
                                                                                        secret_key = secret_key,
                                                                                        secure = secure,
                                                                                        object_file = object_file,
                                                                                        bucket = bucket)
            return write_result


    @staticmethod
    def ReadModel(**kwargs):
        """
        方法功能：

            定义一个读模型的方法

        参数：
            user (str): 用户名
            passwd (str): 密码
            db (str): 数据库名称
            collection_name (str): 数据集名称
            mongodb_config_dict (str): mongodb连接配置参数

            mode (str)：

            （1）direct_operation----可直接运行模式

                model_name （str): 模型名称

            （2）trained_model_remote----需要训练模型的模式(远端模型库)

                mode_name (str): 模型名称
                mode_type (str): 模型类型
                local_path (str): 本地路径，主要指训练机器路径
                target_path (str): 模型库路径，主要指模型库存储地址，通过assist_base配置

            （3）trained_model_target----需要训练模型的模式(目标模型库，适用于主程与模型库同在一台机器上的情况)
            
                mode_name (str): 模型名称
                mode_type (str): 模型类型
                local_path (str): 本地路径，主要指训练机器路径
                target_path (str): 模型库路径，主要指模型库存储地址，通过assist_base配置

        返回：
            writre_result (object): 执行写模型动作后的结果
        """
        
        user = kwargs['user']
        passwd = kwargs['passwd']
        db = kwargs['db']
        collection_name = kwargs['collection_name']
        mongodb_config_dict = kwargs['mongodb_config_dict']
        manager = ModelManager(user,passwd,db,collection_name,mongodb_config_dict)
        invoker = ModelInvoker()
        mode = kwargs['mode']
        if mode == 'direct_operation':
            model_name = kwargs['model_name']
            model = invoker.setCommand(ModelCommand_instance_read_model(manager)).action(mode = mode,
                                                                                         model_name = model_name)
            return model
        elif mode == 'trained_model_object_store':
            model_name = kwargs['model_name']
            model_type = kwargs['model_type']
            connect_info = kwargs['connect_info']
            access_key = kwargs['access_key']
            secret_key = kwargs['secret_key']
            secure = kwargs['secure']
            object_file = kwargs['object_file']
            bucket = kwargs['bucket']
            model = invoker.setCommand(ModelCommand_instance_read_model(manager)).action(mode = mode,
                                                                                        model_name = model_name,
                                                                                        model_type = model_type,
                                                                                        connect_info = connect_info,
                                                                                        access_key = access_key,
                                                                                        secret_key = secret_key,
                                                                                        secure = secure,
                                                                                        object_file = object_file,
                                                                                        bucket = bucket)
            return model



    @staticmethod
    def QueryModel(**kwargs):
        """
        方法功能：

            定义一个查询模型的函数

        参数：
            无

        返回：
            model_name (str)：最新版本的模型名字
        """
        
        user = kwargs['user']
        passwd = kwargs['passwd']
        db = kwargs['db']
        collection_name = kwargs['collection_name']
        mongodb_config_dict = kwargs['mongodb_config_dict']
        manager = ModelManager(user,passwd,db,collection_name,mongodb_config_dict)
        invoker = ModelInvoker()
        mode = kwargs['mode']
        print("====================================query_model")
        model = invoker.setCommand(ModelCommand_instance_query_model(manager)).action()
        return model



###################################################################################################################################
###################################################################################################################################


