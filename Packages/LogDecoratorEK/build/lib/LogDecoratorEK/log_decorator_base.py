# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法运行日志记录的辅助包，主要采用装饰器模式为算法运行函数添加日志记录功能
"""
模块介绍
-------

这是一个算法运行日志记录的辅助包，主要采用装饰器模式为算法运行函数添加日志记录功能

设计模式：

    （1）装饰器模式   

关键点：    

    （1）不侵入代码，算法运行需要整合成一个函数  

主要功能：            

    （1）日志记录功能                                                     

使用示例
-------

>>>from LogDecorator.log_decorator_base import *

>>>AlgorithmLog_Decorator = AlgorithmLog_Decorator()

>>>@AlgorithmLog_Decorator.extend

>>>def run_model(a,b):

---    c = a + b

---    print(">>>>>>",c)

---    return c

>>>if __name__ == '__main__':

---    c = run_model(1,2)

>>>run_model.log(name='log_level_Test',logtext='Add log with consul!',host = '10.2.12.248',port = 8500)

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import logging
import sys
from os import makedirs
from os.path import dirname, exists
from cmreslogging.handlers import CMRESHandler
from LogDecoratorEK.assist_base import *



####### 算法日志基础类 ######################################################
### 设计模式：                                                           ###
### （1）装饰器模式                                                      ###
### 关键点：                                                             ###
### （1）不侵入代码，算法运行需要整合成一个函数                             ###
### 主要功能：                                                           ###
### （1）日志记录功能                                                     ###
############################################################################



###### 算法日志基础类 #################################################################
######################################################################################



class AlgorithmLog_Base(object):
    """
    类介绍：

        这是一个算法日志基础类

        1.日志记录等级包括：

            (1)DEBUG

            (2)INFO

            (3)WARNING

            (4)ERROR

            (5)CRITICAL

    属性方法:
        __call__: 定义一个直接运行函数的魔法方法
    """


    def __call__(self,*args,**kwargs):
        """
        方法功能：

            定义一个直接运行函数的魔法方法

        参数:
            输入参数 (any)：根据具体函数的输入参数而定
        
        返回:
            返回 (object)：返回一个直接运行的函数类对象
        """

        return self.run(*args,**kwargs)


    def log(self,name,logtext,**kwargs):
        """
        方法功能：

            定义一个算法记录的附件功能函数

        参数:
            name (str): 算法记录名称
            logtext (str)：算法记录内容
            host (str)：参数管理服务器的host
            port (int)：参数管理服务器的端口
            log_config_dict (str)：参数管理服务器Elasticsearch配置参数

        返回:
            返回 (object)：无返回，直接形成日志文件和提交日志信息到Elasticsearch
        """

        global loggers
        loggers = {}
        host = kwargs['host']
        port = kwargs['port']
        log_config_dict = kwargs['log_config_dict']
        log_config_dict = get_log_config_dict(host = host,port = port,log_config_dict = log_config_dict)
        LOG_ENABLED = log_config_dict['LOG_ENABLED']  ### 是否开启日志
        LOG_TO_CONSOLE = log_config_dict['LOG_TO_CONSOLE']  ### 是否输出到控制台
        LOG_TO_FILE = log_config_dict['LOG_TO_FILE']  ### 是否输出到文件
        LOG_TO_ES = log_config_dict['LOG_TO_ES']  ### 是否输出到 Elasticsearch
        LOG_PATH = log_config_dict['LOG_PATH']  ### 日志文件路径
        LOG_LEVEL = log_config_dict['LOG_LEVEL']  ### 日志级别
        LOG_FORMAT = log_config_dict['LOG_FORMAT']  ### 每条日志输出格式
        ELASTIC_SEARCH_HOST = log_config_dict['ELASTIC_SEARCH_HOST']  ### Elasticsearch Host
        ELASTIC_SEARCH_PORT = log_config_dict['ELASTIC_SEARCH_PORT']  ### Elasticsearch Port
        ELASTIC_SEARCH_INDEX = log_config_dict['ELASTIC_SEARCH_INDEX']  ### Elasticsearch Index Name
        APP_ENVIRONMENT = log_config_dict['APP_ENVIRONMENT']  ### 运行环境，如测试环境还是生产环境

        def get_logger(name=name):
            """
            方法功能：

            在log函数内部定义一个提交日志记录的具体实现函数

            参数:
               name (str)：算法记录名称

            返回:
               返回 (object)：无返回
            """

            # global loggers
            ### 初始化配置
            if not name: name = __name__
            if loggers.get(name):
                return loggers.get(name)
            logger = logging.getLogger(name)
            logger.setLevel(LOG_LEVEL)
            ### 输出到控制台
            if LOG_ENABLED and LOG_TO_CONSOLE:
                stream_handler = logging.StreamHandler(sys.stdout)
                stream_handler.setLevel(level=LOG_LEVEL)
                formatter = logging.Formatter(LOG_FORMAT)
                stream_handler.setFormatter(formatter)
                logger.addHandler(stream_handler)
            ### 输出到文件
            if LOG_ENABLED and LOG_TO_FILE:
                ### 如果路径不存在，创建日志文件文件夹
                log_dir = dirname(LOG_PATH)
                if not exists(log_dir): makedirs(log_dir)
                ### 添加 FileHandler
                file_handler = logging.FileHandler(LOG_PATH, encoding='utf-8')
                file_handler.setLevel(level=LOG_LEVEL)
                formatter = logging.Formatter(LOG_FORMAT)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
            ### 输出到 Elasticsearch
            if LOG_ENABLED and LOG_TO_ES:
                ### 添加 CMRESHandler
                es_handler = CMRESHandler(hosts=[{'host': ELASTIC_SEARCH_HOST, 'port': ELASTIC_SEARCH_PORT}],
                                        ### 可以配置对应的认证权限
                                        auth_type=CMRESHandler.AuthType.NO_AUTH,  
                                        es_index_name=ELASTIC_SEARCH_INDEX,
                                        ### 一个月分一个 Index
                                        index_name_frequency=CMRESHandler.IndexNameFrequency.MONTHLY,
                                        ### 额外增加环境标识
                                        es_additional_fields={'environment': APP_ENVIRONMENT}  
                                        )
                es_handler.setLevel(level=LOG_LEVEL)
                formatter = logging.Formatter(LOG_FORMAT)
                es_handler.setFormatter(formatter)
                logger.addHandler(es_handler)
            ### 保存到全局 loggers
            loggers[name] = logger
            return logger
        ### 记录具体的算法流程
        logger = get_logger()
        if LOG_LEVEL == 'DEBUG':
            logger.debug(str(logtext))
        elif LOG_LEVEL == 'INFO':
            logger.info(str(logtext))
        elif LOG_LEVEL == 'WARNING':
            logger.warning(str(logtext))
        elif LOG_LEVEL == 'ERROR':
            logger.error(str(logtext))
        elif LOG_LEVEL == 'CRITICAL':
            logger.critical(str(logtext))
        print("log done!",ELASTIC_SEARCH_INDEX)



###### 算法记录装饰器类 ########################################################################################
##############################################################################################################



class AlgorithmLog_Decorator(object):
    """
    类介绍：

        这是一个算法记录装饰器类
        
        主要功能：
        
        1.记录算法的运行流程，并将运行状态等信息形成日志，输出到Elasticsearch
    """


    def __init__(self):
        pass


    def extend(self,decorated):
        """
        方法功能：

            定义一个提交装饰器函数

        参数:
            decorated (object)：作用参数，目标函数

        返回:
           返回 (object)：返回一个具有扩展功能的函数类对象
        """


        class extendsubclass(AlgorithmLog_Base):
            """
            类介绍：
            
                这是一个继承于算法记录基础类的提交子类，目的是为了给目标函数提供扩展功能
            """


            def run(self,*args,**kwargs):
                """
                方法功能：

                定义一个装饰器函数，用于返回添加了扩展功能的目标函数
                
                """

                return decorated(*args,**kwargs)

        return extendsubclass()



####################################################################################################################
####################################################################################################################


