# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个服务管理的接口类，主要用于生成服务、参数管理、服务注册、服务启停和服务运行环境管理。
"""
模块介绍
-------

    这是一个服务管理类，主要用于生成服务、参数管理、服务注册、服务启停和服务运行环境管理。使用了静态方法。

        接口：      

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



from ServerManagerCommand import *



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



class ServerManagerCommandInterface(object):
    """
    类介绍：

        这是一个服务管理接口类
    """


    @staticmethod
    def InputParameter(**kwargs):
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

        result = None
        host = kwargs['host']
        port = kwargs['port']
        key = kwargs['key']
        value = kwargs['value']
        invoker = ServerManagerCommandInvoker()
        cmd = MacroCommand()
        cmd.addCommand(CommandConsulInputParameter(CommandRole,'CommandConsulInputParameter'))
        result = invoker.setCommand(cmd).action(host = host,port = port,key = key,value = value)
        return result


    @staticmethod
    def GetParameter(**kwargs):
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
        invoker = ServerManagerCommandInvoker()
        cmd = MacroCommand()
        cmd.addCommand(CommandConsulGetParameter(CommandRole,'CommandConsulGetParameter'))
        result = invoker.setCommand(cmd).action(host = host,port = port,key = key)
        return result


    @staticmethod
    def GenerateJinjia2(**kwargs):
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
        invoker = ServerManagerCommandInvoker()
        cmd = MacroCommand()
        cmd.addCommand(CommandJinja2Generater(CommandRole,'Jinja2Generater'))
        result = invoker.setCommand(cmd).action(searchpath = searchpath,template_name = template_name,
                                                parameter_dict = parameter_dict,
                                                output_filepath = output_filepath)
        return result 


    @staticmethod
    def OSRemove(**kwargs):
        """
        方法功能：

            删除文件

        参数：
            filepath (str): 文件路径

        返回：
            返回 (str): 删除成功
        """

        filepath = kwargs['filepath']
        invoker = ServerManagerCommandInvoker()
        cmd = MacroCommand()
        cmd.addCommand(CommandOSRemove(CommandRole,'OSRemove'))
        result = invoker.setCommand(cmd).action(filepath = filepath)
        return result


    @staticmethod
    def PutObject(**kwargs):
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
        invoker = ServerManagerCommandInvoker()
        cmd = MacroCommand()
        cmd.addCommand(CommandMinioPutObject(CommandRole,'PutObject'))
        result = invoker.setCommand(cmd).action(connect_info = connect_info,
                                                access_key = access_key,
                                                secret_key = secret_key,
                                                secure = secure,
                                                object_file = object_file,
                                                bucket = bucket)
        return result


    @staticmethod
    def GetObject(**kwargs):
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
        invoker = ServerManagerCommandInvoker()
        cmd = MacroCommand()
        cmd.addCommand(CommandMinioGetObject(CommandRole,'GetObject'))
        result = invoker.setCommand(cmd).action(connect_info = connect_info,
                                                access_key = access_key,
                                                secret_key = secret_key,
                                                secure = secure,
                                                object_file = object_file,
                                                bucket = bucket)
        return result


    @staticmethod
    def SSHRunCMD(**kwargs):
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
        invoker = ServerManagerCommandInvoker()
        cmd = MacroCommand()
        cmd.addCommand(CommandSSHRunCMD(CommandRole,'SSHRunCMD'))
        result = invoker.setCommand(cmd).action(SSH_host_dict = SSH_host_dict,
                                                command = command)
        return result



###################################################################################################################################
###################################################################################################################################


