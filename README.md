# 中文分词与词性标注



## 1. 项目介绍

基于隐马尔科夫模型的中文分词与词性标注



## 2. 代码

### 2.1 语料

/data

- train_seg_corpus.txt_utf8: 中文分词语料
- 199801.txt: 词性标注语料

### 2.2 Main Function

/tagger

- extra.py: 停用词
- hmm.py: 隐马尔科夫模型
- seg.py: 分词
- tagging.py: 词性标注
- utils.py: 

### 2.3 Demo

/demo

- seg_test.py: Segging demo
- tag_test.py: Tagging demo
- seg_tag_test.py: Segging + Tagging demo

## 3. Result

Original string =  我很喜欢自然语言处理
Seg =  ['我', '很', '喜欢', '自然', '语言', '处理']
Tagging =  ['我/r', '很/d', '喜欢/v', '自然/a', '语言/n', '处理/v']

