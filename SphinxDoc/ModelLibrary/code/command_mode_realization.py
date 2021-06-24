# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个模型库操作命令的具体实现类，主要实现模型库的一系列操作
"""
模块介绍
-------

这是一个模型库操作命令的具体实现类，主要实现模型库的一系列操作

功能
----

    设计模式：               

        （1）命令模式

    关键点：

        （1）命令对象化，便于扩展

    主要功能：

        （1）连接模型库

        （2）读取模型

        （3）写入模型

        （4）模型目录（开发中）

        （5）模型查询（开发中）                                                                                                             

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from command_mode_base import *
from assist_base import *
import pymongo
from bson.binary import Binary
import dill
from assist_base import *
import os
from minio import Minio
from minio.error import ResponseError



####### 模型库操作命令实现类 ######################################################
### 设计模式：                                                                 ###
### （1）命令模式                                                              ###
### 关键点：                                                                   ###
### （1）命令对象化，便于扩展                                                   ###
### 主要功能：                                                                 ###
### （1）连接模型库                                                            ###
### （2）读取模型                                                              ###
### （3）写入模型                                                              ###
### （4）模型目录（开发中）                                                     ###
### （5）模型查询（开发中）                                                     ###
#################################################################################



###### 模型库操作命令基础类 ############################################################
######################################################################################



class ModelManager(object):
    """
    类介绍：

        这是一个模型管理者类，主要实现了模型库一系列基础操作，模型库分类：（1）可直接运行的算法函数，测试用collection:pickle（2）需要训练的算法模型，测试用collection:capped
       
        主要操作：（1）连接模型库（2）写入模型（3）读取模型
    """


    def __init__(self,user,passwd,db,collection_name,mongodb_config_dict):
        """
        属性方法功能：

            定义一个初始化函数，主要用于创建模型库连接
           
        参数：   
            user (str)：用户名
            passwd (int)：密码
            collection_name (str)：指定模型库，直接运行的算法和需要训练的算法
            ModelLibrary_Collection (object)：模型库连接对象
        """

        self.user = user
        self.passwd = passwd
        self.db = db
        self.collection_name = collection_name
        self.mongodb_config_dict = mongodb_config_dict
        self.ModelLibrary_Collection = self.create_ModelLibraryConnect()


    def create_ModelLibraryConnect(self):
        """
        方法功能：

            定义一个连接模型库的函数，从assist_base模块中读取配置信息
        """

        mongodb_config_dict = self.mongodb_config_dict
        host = mongodb_config_dict['host']
        port = mongodb_config_dict['port']
        ModelLibrary_Client = pymongo.MongoClient(host = host,port = port,username = self.user,password = self.passwd)
        ModelLibrary_Dadabase = ModelLibrary_Client[self.db]
        dblist = ModelLibrary_Client.list_database_names()
        if self.db not in dblist:
            ModelLibrary_Dadabase.create_collection(self.collection_name, capped=True, size=1024 * 1024 * 10, max=10)
        ModelLibrary_Collection = ModelLibrary_Dadabase[self.collection_name]
        return ModelLibrary_Collection


    def write_model(self,**kwargs):
        """
        方法功能：

            定义一个写入模型的函数
           
        参数：   
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
            返回 (str)：写入成功/失败
        """

        mode = kwargs['mode']
        if mode == 'direct_operation':
            model = kwargs['model_instance']
            model_name = kwargs['model_name']
            dill_model = dill.dumps(model)
            print(dill_model)
            self.ModelLibrary_Collection.insert({'{}'.format(model_name):Binary(dill_model)})
            return 'Write success!'
        elif mode == 'trained_model_object_store':
            model_name = kwargs['model_name']
            model_type = kwargs['model_type']
            model_info_dict = {'model_name':model_name,'model_type':model_type}
            self.ModelLibrary_Collection.insert_one(model_info_dict)
            connect_info = kwargs['connect_info']
            access_key = kwargs['access_key']
            secret_key = kwargs['secret_key']
            secure = kwargs['secure']
            object_file = kwargs['object_file']
            bucket = kwargs['bucket']
            minioClient = Minio(connect_info,
                                access_key = access_key,
                                secret_key = secret_key,
                                secure = secure)
            try:
                file_stat = os.stat(object_file)
                file_data = open(object_file,'rb')
                print(minioClient.put_object(bucket,object_file,file_data,file_stat.st_size))
            except ResponseError as err:
                print(err)
            return 'Put Object successful!'
        elif mode == 'trained_model':
            model_name = kwargs['model_name']
            model_type = kwargs['model_type']
            target_path = path_dict['target_path']
            local_path = kwargs['local_path']
            model_info_dict = {'model_name':model_name,'model_type':model_type}
            self.ModelLibrary_Collection.insert_one(model_info_dict)
            host_dict = SSH_host_dict
            ssh = SSHConnection(host_dict = host_dict)
            ssh.connect()
            ssh.upload(local_path = '{}{}.{}'.format(local_path,model_name,model_type),
                        target_path = '{}{}.{}'.format(target_path,model_name,model_type))
            return 'Write success!'
        else:
            return 'Write failed!'


    def read_model(self,**kwargs):
        """
        方法功能：

            定义一个读取模型的函数
           
        参数：   
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
            返回 (str)：写入成功/失败
        """

        mode = kwargs['mode']
        if mode == 'direct_operation':
            model_name = kwargs['model_name']
            models = self.ModelLibrary_Collection.find({},{'{}'.format(model_name):1,'_id':0})
            for item in models:
                model = item
                if model:
                    break
            dill_model = model['{}'.format(model_name)]
            normal_model = dill.loads(dill_model)
            return normal_model

        elif mode == 'trained_model_remote':
            model_name = kwargs['model_name']
            model_type = kwargs['model_type']
            target_path = path_dict['target_path']
            local_path = kwargs['local_path']
            if not os.path.exists('{}{}.{}'.format(local_path,model_name,model_type)):
                print("Download model!")
                host_dict = SSH_host_dict
                ssh = SSHConnection(host_dict = host_dict)
                ssh.connect()
                ssh.download(target_path = '{}{}.{}'.format(target_path,model_name,model_type),
                            local_path = '{}{}.{}'.format(local_path,model_name,model_type))
                with open('{}{}.{}'.format(local_path,model_name,model_type),'rb') as f:
                    s = f.read()
                dill_model = dill.loads(s)
            else:
                print('Already exists!')
                with open('{}{}.{}'.format(local_path,model_name,model_type),'rb') as f:
                    s = f.read()
                dill_model = dill.loads(s)
            return dill_model

        elif mode == 'trained_model_target':
            model_name = kwargs['model_name']
            model_type = kwargs['model_type']
            target_path = path_dict['target_path']
            local_path = path_dict['local_path']
            with open('{}{}.{}'.format(local_path,model_name,model_type),'rb') as f: ### 此处暂时使用local_path,正常应该使用target_path
                s = f.read()
            dill_model = dill.loads(s)
            return dill_model

        elif mode == 'trained_model_object_store':
            model_name = kwargs['model_name']
            model_type = kwargs['model_type']
            connect_info = kwargs['connect_info']
            access_key = kwargs['access_key']
            secret_key = kwargs['secret_key']
            secure = kwargs['secure']
            object_file = kwargs['object_file']
            bucket = kwargs['bucket']
            minioClient = Minio(connect_info,
                                access_key = access_key,
                                secret_key = secret_key,
                                secure = secure)
            try:
                data = minioClient.get_object(bucket,object_file)
                with open(object_file,'wb') as file_data:
                    for d in data.stream(32*1024):
                        file_data.write(d)
            except ResponseError as err:
                print(err)
            print('Get Object successful!')
            with open('{}'.format(object_file),'rb') as f: ### 此处暂时使用local_path,正常应该使用target_path
                s = f.read()
            dill_model = dill.loads(s)
            return dill_model

        else:
            return 'Read failed!'


    def list_model(self):
        """
        方法功能：

            定义一个列举出所有模型的函数（后续开发）
        """

        print("list_model")


    def query_model(self):
        """
        方法功能：

            定义一个查询模型的函数

        参数：
            无

        返回：
            model_name (str)：最新版本的模型名字
        """

        for item in self.ModelLibrary_Collection.find():
            try:
                model_name = item['model_name']
            except:
                model_name = None
        return model_name



####### 模型库操作命令对象化类 #########################################################################
######################################################################################################



class ModelCommand_instance_read_model(ModelCommand_base):
    """
    类介绍：

        这是一个读取模型操作命令对象化类
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个执行具体操作命令的函数
        """

        command_result = self._manager.read_model(**kwargs)

        return command_result



class ModelCommand_instance_write_model(ModelCommand_base):
    """
    类介绍：

        这是一个写入模型操作命令对象化类
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个执行具体操作命令的函数
        """

        command_result = self._manager.write_model(**kwargs)

        return command_result



class ModelCommand_instance_query_model(ModelCommand_base):
    """
    类介绍：

        这是一个查询模型操作命令对象化类
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个执行具体操作命令的函数
        """

        command_result = self._manager.query_model(**kwargs)

        return command_result



##################################################################################################################
##################################################################################################################


