#encoding:gbk

import os,sys
import jieba,codecs,math
import jieba.posseg as pseg

names={}#定义一个空的表示姓名的字典
relationships={}#定义一个公的表示关系的字典
lineNames=[]#定义一个空的用来表示每段人物关系的列表
jieba.load_userdict('dict.txt')#将收集的人物以字典的形式打开
with codecs.open("黎明破晓的街道.txt",'r','utf-8') as f:#打开小说文件
    for line in f.readlines():
        cixing=pseg.cut(line)
        lineNames.append([])
        for w in cixing: 
            if  w.flag!="nr" or len(w.word) <2:#遍历寻找米“nr”人名词性的词语
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word]=0
                relationships[w.word]={}
            names[w.word]+=1
for line in lineNames:  #对于每一段循环
   for name1 in line:
      for name2 in line: #每一段中任意两个人
          if name1==name2:
              continue
          if relationships[name1].get(name2) is None:
            relationships[name1][name2]=1
          else:
            relationships[name1][name2]+=1
with codecs.open('busan_node.txt','w','gbk') as f:#将节点集合产生到文本内
    f.write("id lable weight\r\n")
    for name,times in names.items():
        f.write(name+" "+name+" "+str(times)+"\r\n")
with codecs.open('busan_edge.txt','w','gbk') as f:#将边产生到文本内
    f.write("source target weight\r\n")
    for name,edges in relationships.items():
        for v, w in edges.items():
            if w>3:
                f.write(name+ " "+v+" "+str(w)+"\r\n")

