# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个服务管理类，主要用于生成服务、参数管理、服务注册、服务启停和服务运行环境管理。
"""
模块介绍
-------

    这是一个服务管理类，主要用于生成服务、参数管理、服务注册、服务启停和服务运行环境管理。

        功能：      

            （1）生成服务    
                                                        
            （2）参数管理   

            （3）服务注册                                                          

            （4）服务启停                                                          

            （5）服务运行环境管理                                                                                                     

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractmethod
from collections import OrderedDict
import consul
from jinja2 import Environment, FileSystemLoader
from minio import Minio
from minio.error import ResponseError
import os
from ServerManager.utils import *



####### 服务管理 #############################################################
### 功能：                                                                 ###
### （1）生成服务                                                          ###
### （2）参数管理                                                          ###
### （3）服务注册                                                          ###
### （4）服务启停                                                          ###
### （5）服务运行环境管理                                                   ###
#############################################################################



####### 命令模式基类 ##################################################################################
######################################################################################################



class ServerManagerCommand(metaclass = ABCMeta):
    """
    类介绍：

        这是一个服务甘丽命令基础类，主要用于抽象命令基类
    """


    def __init__(self,role,role_name):
        """
        属性方法功能：
            定义一个初始化方法

        参数：
            role (object)：命令角色实体
            role_name (object)：命令角色实体名称
        """

        self._role = role
        self.role_name = role_name


    def setRole(self,role):
        """
        方法功能：

            定义一个设置命令角色实体的方法

        参数：   
            role (object)：命令角色实体
        """

        self._role = role


    @abstractmethod
    def execute(self):
        """
        方法功能：

            定义一个执行命令的抽象方法
        """

        pass



####### 命令调度类 ############################################################################################
##############################################################################################################



class ServerManagerCommandInvoker(object):
    """
    类介绍：

        这是一个命令调度者类，主要用于调度各种命令，组合各种逻辑命令实现一项具体功能。
    """

    def __init__(self):
        """
        属性方法功能：

            定义一个初始化方法

        参数：
            __command (object)：命令实体
        """

        self.__command = None


    def setCommand(self,command):
        """
        方法功能：

            定义一个设置命令实体的方法

        参数：
            command (object)：命令实体
        """

        self.__command = command
        return self


    def action(self,**kwargs):
        """
        方法功能：

            定义一个执行具体命令对象的方法
        """

        result = None
        if self.__command is not None:
            result = self.__command.execute(**kwargs)
        return result



####### 宏命令类 ##############################################################################################
##############################################################################################################



class MacroCommand(ServerManagerCommand):
    """
    类介绍：

        这是一个宏命令类，用来组合各种具体命令
    """


    def __init__(self,role = None,role_name = None):
        """
        属性方法功能：

            定义一个初始化方法

        参数：
            role (object)：命令角色实体
        """

        super().__init__(role,role_name)
        self.__commands = OrderedDict()


    def addCommand(self,command):
        """
        方法功能：

            定义一个添加命令的方法
        
        参数：
            command (object)：命令实体
        """

        command_name = command.role_name
        self.__commands[command_name] = command


    def removeCommand(self,command):
        """
        方法功能：

            定义一个删除命令对象的方法

        参数：
            command (object)：命令实体
        """

        command_name = command.role_name
        self.__commands.pop(str(command_name))


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个按照具体逻辑执行各个子命令的方法，这里是依次循环执行。后续需要调度运行，可以通过改变有序字典顺序，依次执行。
        """

        result = None
        for command in self.__commands.values():
            result = command.execute(**kwargs)
        return result



####### 对象化的命令类 #########################################################################################
###############################################################################################################



class CommandConsulInputParameter(ServerManagerCommand):
    """
    类介绍：

        向Consul输入参数
    """


    def __init__(self,role,role_name):
        """
        属性方法功能：

            继承自服务管理命令类

        参数：
            role (object): 命令实例
            role_name (str): 命令名称
        """

        super().__init__(role,role_name)


    def execute(self,**kwargs):
        """
        方法功能：

            执行具体的命令动作
        """

        result = None
        result = self._role.ConsulInputParameter(self,**kwargs)
        return result



class CommandConsulGetParameter(ServerManagerCommand):
    """
    类介绍：

        从Consul获取参数
    """


    def __init__(self,role,role_name):
        """
        属性方法功能：

            继承自服务管理命令类

        参数：
            role (object): 命令实例
            role_name (str): 命令名称
        """

        super().__init__(role,role_name)


    def execute(self,**kwargs):
        """
        方法功能：

            执行具体的命令动作
        """

        result = None
        result = self._role.ConsulGetParameter(self,**kwargs)
        return result



class CommandJinja2Generater(ServerManagerCommand):
    """
    类介绍：

        用Jinja2生成对应文件
    """

    def __init__(self,role,role_name):
        """
        属性方法功能：

            继承自服务管理命令类

        参数：
            role (object): 命令实例
            role_name (str): 命令名称
        """

        super().__init__(role,role_name)


    def execute(self,**kwargs):
        """
        方法功能：

            执行具体的命令动作
        """

        result = None
        result = self._role.Jinja2Generater(self,**kwargs)
        return result



class CommandOSRemove(ServerManagerCommand):
    """
    类介绍：

        用OS删除文件
    """


    def __init__(self,role,role_name):
        """
        属性方法功能：

            继承自服务管理命令类

        参数：
            role (object): 命令实例
            role_name (str): 命令名称
        """

        super().__init__(role,role_name)


    def execute(self,**kwargs):
        """
        方法功能：

            执行具体的命令动作
        """

        result = None
        result = self._role.OSRemove(self,**kwargs)
        return result



class CommandMinioPutObject(ServerManagerCommand):
    """
    类介绍：

        向Minio推送对象
    """


    def __init__(self,role,role_name):
        """
        属性方法功能：

            继承自服务管理命令类

        参数：
            role (object): 命令实例
            role_name (str): 命令名称
        """

        super().__init__(role,role_name)


    def execute(self,**kwargs):
        """
        方法功能：

            执行具体的命令动作
        """

        result = None
        result = self._role.MinioPutObject(self,**kwargs)
        return result



class CommandMinioGetObject(ServerManagerCommand):
    """
    类介绍：

        从Minio获取对象
    """


    def __init__(self,role,role_name):
        """
        属性方法功能：

            继承自服务管理命令类

        参数：
            role (object): 命令实例
            role_name (str): 命令名称
        """

        super().__init__(role,role_name)


    def execute(self,**kwargs):
        """
        方法功能：

            执行具体的命令动作
        """

        result = None
        result = self._role.MinioGetObject(self,**kwargs)
        return result



class CommandSSHRunCMD(ServerManagerCommand):
    """
    类介绍：

        用SSH远程运行命令
    """


    def __init__(self,role,role_name):
        """
        属性方法功能：

            继承自服务管理命令类

        参数：
            role (object): 命令实例
            role_name (str): 命令名称
        """

        super().__init__(role,role_name)


    def execute(self,**kwargs):
        """
        方法功能：

            执行具体的命令动作
        """

        result = None
        result = self._role.SSHRunCMD(self,**kwargs)
        return result



####### 命令角色类（具体实现） ##############################################################################################
###########################################################################################################################
class CommandRole(object):
    """
    类介绍：

        命令的具体实现
    """

    def __init__(self,name):
        """
        属性方法功能：

            命令集合名称

        参数：
            name (str): 命令集合名称
        """

        self.name = name


    def ConsulInputParameter(self,**kwargs):
        """
        方法功能：

            向Consul输入参数

        参数：
            host (str): host
            port (int): port
            key (str): 参数名称
            value (str): 具体的参数值

        返回：
            返回 (str): 输入成功
        """

        host = kwargs['host']
        port = kwargs['port']
        key = kwargs['key']
        value = kwargs['value']
        consul_connect = consul.Consul(host,port)
        consul_connect.kv.put(key = key,value = value)
        return 'Input Parameter Successful!'


    def ConsulGetParameter(self,**kwargs):
        """
        方法功能：

            向Consul输入参数

        参数：
            host (str): host
            port (int): port
            key (str): 参数名称

        返回：
            value (str): 具体参数值
        """

        host = kwargs['host']
        port = kwargs['port']
        key = kwargs['key']
        consul_connect = consul.Consul(host,port)
        kv_value = consul_connect.kv.get(key = key)
        value = str(kv_value[1]['Value'])[2:-1]
        return value


    def Jinja2Generater(self,**kwargs):
        """
        方法功能：

            用Jinja2生成对应文件

        参数：
            search (str): 工作路径
            template_name (str): 模板名称
            parameter_dict (Dict): 输入参数
            output_filepath (str): 输出路径

        返回：
            返回 (str): 生成成功
        """

        searchpath = kwargs['searchpath']
        template_name = kwargs['template_name']
        parameter_dict = kwargs['parameter_dict']
        output_filepath = kwargs['output_filepath']
        env = Environment(loader = FileSystemLoader(searchpath = searchpath))
        template = env.get_template(template_name)
        output = template.render(parameter_dict)
        with open("{}".format(output_filepath),'w',encoding = 'utf8') as out:
            out.write(output)
        return 'Generate Done!'


    def OSRemove(self,**kwargs):
        """
        方法功能：

            删除文件

        参数：
            filepath (str): 文件路径

        返回：
            返回 (str): 删除成功
        """

        filepath = kwargs['filepath']
        os.remove(filepath)
        return 'Remove successful!'



    def MinioPutObject(self,**kwargs):
        """
        方法功能：

            向Minio推送对象

        参数：
            connect_info (str): 连接地址
            access_key (str): 用户名
            secret_key (str): 密码
            object_file (str): 对象名称
            bucket (str): 桶名称

        返回：
            返回 (str): 上传成功
        """

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


    def MinioGetObject(self,**kwargs):
        """
        方法功能：

            向Minio推送对象

        参数：
            connect_info (str): 连接地址
            access_key (str): 用户名
            secret_key (str): 密码
            object_file (str): 对象名称
            bucket (str): 桶名称

        返回：
            返回 (str): 下载成功
        """

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
        return 'Get Object successful!'


    def SSHRunCMD(self,**kwargs):
        """
        方法功能：

            通过SSH远端运行命令

        参数：
            SSH_host_dict (Dict): 连接信息
            command (str): 具体要执行的命令

        返回：
            res (str): 命令执行后远程终端的输出流
        """
        
        SSH_host_dict = kwargs['SSH_host_dict']
        command = kwargs['command']
        ssh = SSHConnection(host_dict = SSH_host_dict)
        ssh.connect()
        res = ssh.run_cmd(command)
        return res



###########################################################################################################################
###########################################################################################################################


