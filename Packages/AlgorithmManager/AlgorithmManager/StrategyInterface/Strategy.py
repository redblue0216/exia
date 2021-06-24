# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个利用策略模式技术和回调技术实现的接口类，主要用于实现算法平台的各种功能接口
"""
模块介绍
-------

这是一个利用策略模式技术和回调技术实现的接口类，主要用于实现算法平台的各种功能接口

    功能：                  

        （1）算法组件套餐生成         

        （2）算法组件对象添加      

        （3）算法组件对象管理                                                                                                                                                                                                              

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################


from abc import ABCMeta,abstractmethod
from AlgorithmManager.ObjectManager.ObjectPool import *
from AlgorithmManager.ObjectManager.ObjectInstance import *



####### 算法接口 #############################################################
### 功能：                                                                 ###
### （1）算法组件套餐生成                                                   ###
### （2）算法组件对象添加                                                   ###
### （3）算法组件对象管理                                                   ###
#############################################################################



####### 策略模式基类 ##################################################################################
######################################################################################################



class Strategy(metaclass = ABCMeta):
    """
    类介绍：

        这是一个策略模式的基类，主要用于实现回调机制，此处的回调机制是为了实现算法接口
    """


    @abstractmethod
    def algorithm(self,*args,**kwargs):

        pass



####### 策略模式上下文管理类 ############################################################################
#######################################################################################################



class StrategyContext:
    """
    类介绍：

        这是一个上下文环境类，用来管理算法平台的各种套餐
    """


    def interface(self,strategy,*args,**kwargs):
        """
        方法功能：

            定义一个接口方法，主要用来实现依赖倒置原则，使得实现与算法平台框架解耦。
        """

        result = strategy.algorithm(*args,**kwargs)
        return result



####### 策略模式具体实现类 ############################################################################
#####################################################################################################



class StrategyObjectPoolEmpty(Strategy):
    """
    类介绍：

        这是一个可以返回空的对象池类
    """


    def __init__(self,ObjectPool,ParameterDict = None):
        """
        属性方法功能：

            定义一个传参用的初始化方法

        参数：
            ObjectPool (object): 对象池
            ParameterDict (Dict): 参数字典
        """

        self.ParameterDict = ParameterDict
        self.ObjectPool = ObjectPool
    

    def algorithm(self,*args,**kwargs):
        """
        方法功能：

            定义一个返回对象池的方法
        """

        return self.ObjectPool



class StrategyShowInfo(object):
    """
    类介绍：

        这是一个显示模块使用功能的类
    """

    def __init__(self,name):
        """
        属性方法功能：

            定义一个设置名称的初始化方法

        参数：
            name (str): 名称
        """

        self.name = name


    def ShowInfo(self,object_pool,cls_instance_name):
        """
        方法功能：

            定义一个获取具体功能模块的方法

        参数：
            object_pool (object): 对象池
            cls_instance_name (object): 实例名称
        """

        result = object_pool.function[cls_instance_name]
        return result


class StrategyObjectPoolBase(Strategy):
    """
    类介绍：

        这是一个基础套餐类，主要功能有：（1）数据库接口（2）服务管理（3）模型管理（4）模型监控（5）算法记录
    """


    def __init__(self,ObjectPool,ParameterDict = None):
        """
        属性方法功能：

            定义一个接受参数的方法

        参数：
            ObjectPool (object): 对象池
            ParameterDict (Dict): 参数字典
        """

        self.ParameterDict = ParameterDict
        self.ObjectPool = ObjectPool


    def algorithm(self,*args,**kwargs):
        """
        方法功能：

            定义一个生成基础套餐的具体实现方法。该套餐初始参数需要数据库连接参数。
        """

        DataAPI_user = kwargs['DataAPI_user']
        DataAPI_passwd = kwargs['DataAPI_passwd']
        DataAPI_host = kwargs['DataAPI_host']
        DataAPI_port = kwargs['DataAPI_port']
        DataAPI_db = kwargs['DataAPI_db']
        DataAPI_charset	= kwargs['DataAPI_charset']
        ###################################
        ### ShowInfo ######################
        ###################################
        ShowInfo = StrategyShowInfo('ShowInfo')
        ##################################
        ### ModelMonitoring ##############
        ##################################
        ModelMonitoring_eval_dict = {
            'import':{
                'eval_type':'import',
                'eval_sentence':'from ModelMonitoring.observer_realization import ModelMonitoring,UpdateMode'
            },
            'model_monitor':{
                'eval_type':'obj',
                'eval_sentence':'ModelMonitoring()'
            },
            'update_mode':{
                'eval_type':'obj',
                'eval_sentence':'UpdateMode()'
            },
            'init':{
            'eval_type':'exec',
            'eval_sentence':"object_model_dict['model_monitor'].addObserver(object_model_dict['update_mode'])"
            }
        }
        ModelMonitoring_tmp_rep = 'import->model_monitor,model_monitor->update_mode,update_mode->init'
        ModelMonitoring_startLabel = 'import'
        ModelMonitoring_outputLabel = 'model_monitor'
        ModelMonitoring_name = 'ModelMonitoring'
        ModelMonitoring_input_parameter = {'a':'123','b':'456'}
        ModelMonitoring_output_parameter = {'setindex':'setIndex()',
                                            'stop':'stop()',
                                            'restart':'restart()',
                                            'state':'state'}
        ModelMonitoring_input_output = {'input':ModelMonitoring_input_parameter,
                                        'output':ModelMonitoring_output_parameter}
        ModelMonitoring_ObjectDag = BuilderManager().buildObjectDag(ModelMonitoring_eval_dict,
                                                    ModelMonitoring_tmp_rep,
                                                    ModelMonitoring_startLabel,
                                                    ModelMonitoring_outputLabel)
        ModelMonitoring_obj_instance = ObjectInstance(name = ModelMonitoring_name,
                                                      input_parameter = ModelMonitoring_input_parameter,
                                                      output_parameter = ModelMonitoring_output_parameter,
                                                      handler = ModelMonitoring_ObjectDag)
        #####################################
        ### DataAPI #########################
        #####################################
        DataAPI_eval_dict = {
            'import':{
                'eval_type':'import',
                'eval_sentence':'from DataAPI.database_interface_realization import *'
            },
            'DB':{
                'eval_type':'obj',
                'eval_sentence':"DataBaseAPI(user = '{}',passwd = '{}',host = '{}',port = {},db = '{}',charset = '{}')"\
                .format(DataAPI_user,DataAPI_passwd,DataAPI_host,DataAPI_port,DataAPI_db,DataAPI_charset)
            }
        }
        DataAPI_tmp_rep = 'import->DB'
        DataAPI_startLabel = 'import'
        DataAPI_outputLabel = 'DB'
        DataAPI_name = 'DataAPI'
        DataAPI_input_parameter = {'a':'123','b':'456'}
        DataAPI_output_parameter = {'exec_stored_procedure':'exec_stored_procedure(InputParameters_dict)',
                                            'exit':'exit()'}
        DataAPI_input_output = {'input':DataAPI_input_parameter,
                                'output':DataAPI_output_parameter}
        DataAPI_ObjectDag = BuilderManager().buildObjectDag(DataAPI_eval_dict,
                                                             DataAPI_tmp_rep,
                                                             DataAPI_startLabel,
                                                             DataAPI_outputLabel)
        DataAPI_obj_instance = ObjectInstance(name = DataAPI_name,
                                            input_parameter = DataAPI_input_parameter,
                                            output_parameter = DataAPI_output_parameter,
                                            handler = DataAPI_ObjectDag)
        #####################################
        ### LogDecoratorEK ##################
        #####################################
        LogDecoratorEK_eval_dict = {
            'import':{
                'eval_type':'import',
                'eval_sentence':'from LogDecoratorEK.log_decorator_base import *'
            },
            'AlgorithmLog_Decorator':{
                'eval_type':'obj',
                'eval_sentence':"AlgorithmLog_Decorator()"
            }
        }
        LogDecoratorEK_tmp_rep = 'import->AlgorithmLog_Decorator'
        LogDecoratorEK_startLabel = 'import'
        LogDecoratorEK_outputLabel = 'AlgorithmLog_Decorator'
        LogDecoratorEK_name = 'LogDecoratorEK'
        LogDecoratorEK_input_parameter = {'a':'123','b':'456'}
        LogDecoratorEK_output_parameter = {'log':'run_model.log(name,logtext,host,port)'}
        LogDecoratorEK_input_output = {'input':LogDecoratorEK_input_parameter,
                                'output':LogDecoratorEK_output_parameter}
        LogDecoratorEK_ObjectDag = BuilderManager().buildObjectDag(LogDecoratorEK_eval_dict,
                                                             LogDecoratorEK_tmp_rep,
                                                             LogDecoratorEK_startLabel,
                                                             LogDecoratorEK_outputLabel)
        LogDecoratorEK_obj_instance = ObjectInstance(name = LogDecoratorEK_name,
                                            input_parameter = LogDecoratorEK_input_parameter,
                                            output_parameter = LogDecoratorEK_output_parameter,
                                            handler = LogDecoratorEK_ObjectDag)
        #####################################
        ### ModelLibrary ####################
        #####################################
        ModelLibrary_eval_dict = {
            'import':{
                'eval_type':'import',
                'eval_sentence':'from ModelLibrary.model_library_interface import *'
            },
            'ModelLibraryInterface':{
                'eval_type':'obj',
                'eval_sentence':"ModelLibraryInterface()"
            }
        }
        ModelLibrary_tmp_rep = 'import->ModelLibraryInterface'
        ModelLibrary_startLabel = 'import'
        ModelLibrary_outputLabel = 'ModelLibraryInterface'
        ModelLibrary_name = 'ModelLibrary'
        ModelLibrary_input_parameter = {'a':'123','b':'456'}
        ModelLibrary_output_parameter = {'WriteModel':'ModelLibrary.WriteModel()',
                                         'ReadModel':'ModelLibrary.ReadModel()'}
        ModelLibrary_input_output = {'input':ModelLibrary_input_parameter,
                                'output':ModelLibrary_output_parameter}
        ModelLibrary_ObjectDag = BuilderManager().buildObjectDag(ModelLibrary_eval_dict,
                                                             ModelLibrary_tmp_rep,
                                                             ModelLibrary_startLabel,
                                                             ModelLibrary_outputLabel)
        ModelLibrary_obj_instance = ObjectInstance(name = ModelLibrary_name,
                                            input_parameter = ModelLibrary_input_parameter,
                                            output_parameter = ModelLibrary_output_parameter,
                                            handler = ModelLibrary_ObjectDag)		
        #####################################
        ### ServerManager ###################
        #####################################
        ServerManager_eval_dict = {
            'import':{
                'eval_type':'import',
                'eval_sentence':'from ServerManager.ServerCommandInterface import *'
            },
            'ServerManagerInterface':{
                'eval_type':'obj',
                'eval_sentence':"ServerManagerCommandInterface()"
            }
        }
        ServerManager_tmp_rep = 'import->ServerManagerInterface'
        ServerManager_startLabel = 'import'
        ServerManager_outputLabel = 'ServerManagerInterface'
        ServerManager_name = 'ServerManager'
        ServerManager_input_parameter = {'a':'123','b':'456'}
        ServerManager_output_parameter = {'log':'run_model.log(name,logtext,host,port)'}
        ServerManager_input_output = {'input':ServerManager_input_parameter,
                                'output':ServerManager_output_parameter}
        ServerManager_ObjectDag = BuilderManager().buildObjectDag(ServerManager_eval_dict,
                                                             ServerManager_tmp_rep,
                                                             ServerManager_startLabel,
                                                             ServerManager_outputLabel)
        ServerManager_obj_instance = ObjectInstance(name = ServerManager_name,
                                            input_parameter = ServerManager_input_parameter,
                                            output_parameter = ServerManager_output_parameter,
                                            handler = ServerManager_ObjectDag)													
        #####################################
        ### 对象实例化，方便调用功能 ##########
        #####################################
        ModelMonitoring = ModelMonitoring_obj_instance.gen(ModelMonitoring_ObjectDag)
        DataAPI = DataAPI_obj_instance.gen(DataAPI_ObjectDag)
        LogDecoratorEK = LogDecoratorEK_obj_instance.gen(LogDecoratorEK_ObjectDag)
        ModelLibrary = ModelLibrary_obj_instance.gen(ModelLibrary_ObjectDag)
        ServerManager = ServerManager_obj_instance.gen(ServerManager_ObjectDag)
        #####################################
        ### 创建对象池 ######################
        ####################################
        ObjectPool = self.ObjectPool
        ObjectPool.function = dict()
        ###################################
        ### 向对象池添加对象 ###############
        ##################################
        ObjectPool.addObject(ShowInfo,'ShowInfo')
        ObjectPool.addObject(ModelMonitoring,'ModelMonitoring')
        ObjectPool.addObject(DataAPI,'DataAPI')
        ObjectPool.addObject(LogDecoratorEK,'LogDecoratorEK')
        ObjectPool.addObject(ModelLibrary,'ModelLibrary')
        ObjectPool.addObject(ServerManager,'ServerManager')
        ##################################
        ### 向对象池写入功能说明 ###########
        ##################################
        ObjectPool.function['ModelMonitoring'] = ModelMonitoring_input_output
        ObjectPool.function['DataAPI'] = DataAPI_input_output
        ObjectPool.function['LogDecoratorEK'] = LogDecoratorEK_input_output
        ObjectPool.function['ModelLibrary'] = ModelMonitoring_input_output
        ObjectPool.function['ServerManager'] = ServerManager_input_output
        #################################
        #################################
        #################################
        return ObjectPool



#########################################################################################################################
#########################################################################################################################


