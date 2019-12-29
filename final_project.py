#encoding:gbk

import os,sys
import jieba,codecs,math
import jieba.posseg as pseg

names={}#����һ���յı�ʾ�������ֵ�
relationships={}#����һ�����ı�ʾ��ϵ���ֵ�
lineNames=[]#����һ���յ�������ʾÿ�������ϵ���б�
jieba.load_userdict('dict.txt')#���ռ����������ֵ����ʽ��
with codecs.open("���������Ľֵ�.txt",'r','utf-8') as f:#��С˵�ļ�
    for line in f.readlines():
        cixing=pseg.cut(line)
        lineNames.append([])
        for w in cixing: 
            if  w.flag!="nr" or len(w.word) <2:#����Ѱ���ס�nr���������ԵĴ���
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word]=0
                relationships[w.word]={}
            names[w.word]+=1
for line in lineNames:  #����ÿһ��ѭ��
   for name1 in line:
      for name2 in line: #ÿһ��������������
          if name1==name2:
              continue
          if relationships[name1].get(name2) is None:
            relationships[name1][name2]=1
          else:
            relationships[name1][name2]+=1
with codecs.open('busan_node.txt','w','gbk') as f:#���ڵ㼯�ϲ������ı���
    f.write("id lable weight\r\n")
    for name,times in names.items():
        f.write(name+" "+name+" "+str(times)+"\r\n")
with codecs.open('busan_edge.txt','w','gbk') as f:#���߲������ı���
    f.write("source target weight\r\n")
    for name,edges in relationships.items():
        for v, w in edges.items():
            if w>3:
                f.write(name+ " "+v+" "+str(w)+"\r\n")

