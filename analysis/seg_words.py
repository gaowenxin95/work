#!/usr/bin/env python
# coding: utf-8

# In[1]:



def seg_words(text):
    import jieba
    import re
    #去掉不在(所有中文、大小写字母、数字)中的非法字符
    regex = re.compile(r'[^\u4e00-\u9fa5A-Za-z0-9]')
    text = regex.sub(' ', text) # 将非法字符用‘ ’替代
    text = text.strip() # 去掉前后的空格
    word_list = jieba.cut(text, cut_all= False)
    return word_list


# In[ ]:




