#encoding=utf-8

import jieba
import codecs

Dict = []    #个人词典
lines = ""   #初始化lines

#把提供的词典加入自己的词典中
def match(pathOfTxt):
    with codecs.open(pathOfTxt, 'r', 'utf-8') as DictFile:
        for line in DictFile.readlines():
            line = line.strip('\n')    #去除\n
            Dict.append((line, 0))

#麻烦帅气的师兄/漂亮的师姐自己改下路径啦= =
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/角色/反派.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/角色/角色.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/角色/角色中的其它.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/角色/男主角.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/角色/配角.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/角色/熊顿.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/剧情/剧情.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/剧情/开头.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/剧情/发展.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/剧情/结局.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/剧情/笑点.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/剧情/泪点.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/视听/视听.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/视听/视听效果中的其它.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/视听/画面.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/视听/镜头.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/视听/动作.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/视听/音乐.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/制作/制作.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/制作/导演.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/制作/编剧.txt')
#match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/制作/选景.txt')  为什么选景这个txt无法打开？？？
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/制作/出品公司.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/主题/风格.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/主题/主题.txt')
match('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/词典/主题/题材内容.txt')

with codecs.open('/home/infinite/Downloads/2017数据挖掘作业/week2 Python 作业/作业/太空旅店.txt', 'r', 'utf-8') as filein:
    for line in filein.readlines():
        line.strip('\n')
        lines += line[28:len(line)-1]

ItemsDict = dict(Dict)      #初始化词典
words = jieba.cut(lines)    #对评论分词
OutPutFile = codecs.open('/home/infinite/my_github/PythonStudy/电影评论匹配作业/匹配结果.txt', 'w', 'utf-8')

for word in words:   #进行分词并匹配
    if word in ItemsDict.keys():
        ItemsDict[word] += 1

for k in ItemsDict.keys():
    if k == "" or k == " ":
        continue
    else:
        results = k + ' ' + str(ItemsDict[k]) + '\n'
        OutPutFile.write(results)
