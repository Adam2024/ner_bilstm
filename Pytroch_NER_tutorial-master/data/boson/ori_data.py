import codecs
import pandas as pd
import numpy as np
import re
import json
import os

output_data = codecs.open("F:\\work\\履约事件抽取\\事件抽取方式\\_CSDN_Pytroch_NER_tutorial-master\\Pytroch_NER_tutorial-master\\data\\boson\\origindata.txt",'w','utf-8')
path="F:\\work\\履约事件抽取\\事件抽取方式\\标注数据\\5.处理后的数据\\data_pro"
path_list=os.listdir(path)
text_all=[]
for pt in path_list: 
    with open(f'{path}\\{pt}','r',encoding='utf-8') as load_f:
        event_list=json.load(load_f)
        
    for event in event_list:
        text=event["text"]
        arguments=event["event_list"]
        for arg in arguments["arguments"]:
            role=arg["role"]
            argument=arg["argument"]
            str="{{"+role+":"+argument+"}}"
            text=text.replace(argument,str,1)
        text_all+=text
        output_data.write(text)
        output_data.write('\n')
        
output_data.close()
