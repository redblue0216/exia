# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个辅助类，主要为log_decorator_base提供一些辅助功能
"""
模块介绍
-------

这是一个辅助类，主要为log_decorator_base提供一些辅助功能

功能
----

(1) 配置参数辅助

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import consul



####### 辅助类 #############################################################
### 功能：                                                               ###
### （1）配置参数辅助                                                     ###
############################################################################



####### 配置参数辅助类 ##########################################################################
################################################################################################


def get_log_config_dict(**kwargs):
        """
        函数功能：
        
        定义一个从Consul获取记录字典的函数

        参数:
            host (str)：参数管理服务器的host
            port (int)：参数管理服务器的端口
            log_config_dict (str)：参数管理服务器Elasticsearch配置参数

        返回:
            log_config_dict (dict)：记录配置字典
        """
        
        host = kwargs['host']
        port = kwargs['port']
        key = kwargs['log_config_dict']
        consul_connect = consul.Consul(host,port)
        kv_value = consul_connect.kv.get(key = key)
        value = str(kv_value[1]['Value'])[2:-1]
        tmp_value = value
        tmp_value = tmp_value.replace("'",'"').lstrip('{').rstrip('}').split(',')
        tmp_dict = dict()
        for tmp in tmp_value:
            tmp = tmp.replace(' ','')
            tmp = tmp.replace('"','')
            tmp = tmp.split(':')
            tmp_dict[tmp[0]] = tmp[1]
        log_config_dict = tmp_dict
        return log_config_dict
        
        

#########################################################################################################
#########################################################################################################


