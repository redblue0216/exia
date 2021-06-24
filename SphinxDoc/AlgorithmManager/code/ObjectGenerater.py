# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个对象生成器，主要用于对象实例中功能对象的具体生成过程。使用的技术有类方法实现的抽象工厂、eval、exec和描述符技术。
"""
模块介绍
-------

这是一个对象生成器，主要用于对象实例中功能对象的具体生成过程。使用的技术有类方法实现的抽象工厂、eval、exec和描述符技术。

    功能：             

        （1）属性托管           

        （2）方法绑定       

        （3）预先检查                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from model import GraphDemoModel
from algorithms import *
from transform import *
from descriptor import *
from transform import *



####### 对象生成器 ###########################################################
### 功能：                                                                 ###
### （1）属性托管                                                          ###
### （2）方法绑定                                                          ###
### （3）预先检查                                                          ###
#############################################################################



####### 对象生成类 ####################################################################################
######################################################################################################



class ObjectGenerater(object):
    """
    类介绍：

        这是一个对象生成器，用来生成使用到的实例对象。
    """


    @classmethod
    def gen(cls,eval_dict,tmp_rep,startLabel,outputLabel):
        """
        方法功能：

            定义一个根据具体DAG生成功能对象的类方法。

        参数：
            cls (object)：抽象类
            eval_dict (Dict)：执行语句字典
            tmp_rep (str)：DAG描述
            startLabel (str)：DAG开始节点
            outputLabel (str)：DAG输出节点
        """

        GraphDemoModel = eval('GraphDemoModel({})'.format(eval_dict))
        trans_rep_list = trans_rep(tmp_rep)
        GraphDemoModel.createGraph(rep=trans_rep_list,startLabel=startLabel)
        graph = GraphDemoModel.getGraph()
        stack = GraphDemoModel.run(topoSort)
        topoSort_deque = trans_stack(stack)
        object_model_dict = dict()
        for tmp_item in topoSort_deque:
            if eval_dict[tmp_item]['eval_type'] == 'import':
                str_sentence = eval_dict[tmp_item]['eval_sentence']
                exec(str_sentence)
            elif eval_dict[tmp_item]['eval_type'] == 'obj':
                str_sentence = eval_dict[tmp_item]['eval_sentence']
                object_model_dict[tmp_item] = eval(str_sentence)
            elif eval_dict[tmp_item]['eval_type'] == 'exec':
                str_sentence = eval_dict[tmp_item]['eval_sentence']
                eval(str_sentence)
            else:
                raise KeyError('key does not exist!')
        return object_model_dict[outputLabel]



##########################################################################################################
##########################################################################################################


