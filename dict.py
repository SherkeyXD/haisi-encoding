import random
import itertools


plaindict=[
    '（尖叫）', 
    '（扭曲）', 
    '（阴暗的爬行）', 
    '（爬行）', 
    '（扭动）', 
    '（阴暗地蠕动）', 
    '（翻滚）', 
    '（激烈地爬动）', 
    '（痉挛）', 
    '（嘶吼）', 
    '（蠕动）', 
    '（阴森的低吼）', 
    '（分裂）', 
    '（走上岸）', 
    '（扭曲的行走）', 
    '（不分对象攻击）'
]


def getdict(seed : int) -> dict :
    tmp=[]
    dic={}
    a = itertools.product(plaindict, repeat=4)
    for i in a:
        tmp.append(i[0]+i[1]+i[2]+i[3])
    random.seed(seed)
    random.shuffle(tmp)
    for i in range(0, len(tmp)):
        dic[chr(i)]=tmp[i]
    return dic