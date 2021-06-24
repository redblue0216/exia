# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个辅助类，主要为command_mode_realization提供辅助功能
"""
模块介绍
-------

这是一个辅助类，主要为command_mode_realization提供辅助功能

功能
----

(1) 配置参数辅助

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import paramiko



####### 辅助类 #############################################################
### 功能：                                                               ###
### （1）配置参数辅助                                                     ###
############################################################################



####### 配置参数辅助类 ##########################################################################
################################################################################################



# mongodb_config_dict= {
# 	'host' : '192.168.0.103',
# 	'port' : 27017
# }



SSH_host_dict = {
    'host' : '10.2.15.126',
    'port' : 22,
    'username' : 'shihua',
    'pwd' : 'ATTACK7121553rb1'
}



path_dict = {
    'target_path' : '/home/shihua/tulip/test/model_library/',
    'local_path' : 'D:/AEwork/algorithm_platform/'
}



###### openssh远端操作类 ##################################################################################
##########################################################################################################



class SSHConnection(object):
    """
    类介绍：

        这是一个SSHConnection，主要利用openSSH远程连接linux机器，主要功能：（1）远程连接（2）运行Shell命令（3）上传文件（4）下载文件（5）关闭连接
    """

 
    def __init__(self,host_dict):
        """
        属性方法功能：

            定义一个初始化函数，主要用于收集远程连接配置信息
        
        参数：   
            host (str)：IP地址
            port (int): 端口
            username (str)：用户名
            pwd (int)：密码
        """

        self.host = host_dict['host']
        self.port = host_dict['port']
        self.username = host_dict['username']
        self.pwd = host_dict['pwd']
        self.__k = None
 

    def connect(self):
        """
        方法功能：

            定义一个SSH远程连接函数，主要适用openSSH技术
        """

        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport = transport
 

    def close(self):
        """
        方法功能：

            定义一个关闭连接函数
        """

        self.__transport.close()
 
    def run_cmd(self, command):
        """
        方法功能：

            定义一个运行Shell命令的函数，主要返回error和res

        参数：   
            command (str)：Shell命令

        返回：
           返回：无返回，直接输出在控制台
        """


        def to_str(bytes_or_str):
            """
            函数功能：

                定义一个将Byte类型转换为str的函数
               
            参数：   
                bytes_or_str (str)：需要转换的对象

            返回：   
                返回：str类型输出
            """


            if isinstance(bytes_or_str, bytes):
                value = bytes_or_str.decode('utf-8')
            else:
                value = bytes_or_str
            return value

        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        res = to_str(stdout.read())
        # 获取错误信息
        error = to_str(stderr.read())
        # 如果有错误信息，返回error
        # 否则返回res
        if error.strip():
            return {'color':'red','res':error}
        else:
            return {'color': 'green', 'res':res}
        # return res 
 

    def upload(self,local_path, target_path):
        """
        方法功能：

            定义一个上传文件的函数

        参数：
            local_path：本地上传文件的路径
            target_path：目标上传文件的路径

        返回：
            无返回
        """

        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path, confirm=True)
        # print(os.stat(local_path).st_mode)
        # 增加权限
        # sftp.chmod(target_path, os.stat(local_path).st_mode)
        sftp.chmod(target_path, 0o755)  # 注意这里的权限是八进制的，八进制需要使用0o作为前缀
 

    def download(self,target_path, local_path):
        """
        方法功能：

            定义一个下载文件的函数
           
        参数：   
            local_path (str)：本地上传文件的路径
            target_path (str)：目标上传文件的路径

        返回：
            无返回
        """

        # 连接，下载
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 下载至服务器 /tmp/test.py
        sftp.get(target_path, local_path)
 

    # 销毁
    def __del__(self):
        """
        方法功能：
            定义一个销毁函数，关闭整个对象
        """

        self.close()
        
        

#########################################################################################################
#########################################################################################################


