#encoding=utf-8
import random
import re
print("begin lottery!")
list=[]#创建一个空列表放抽奖名单
#str=input("please input name:")#输入列表的第一个值
#list.append(str)#将输入值插入列表
i=0
#判断输入值是否为空，输入值不为空，继续输入；输入值为空，跳出循环，进行抽奖
'''
def SpecCheck():#特殊字符提示错误
    specstr = "~!@#$%^&*()_+-*/<>.[]\/"
    for n in specstr:
        if n in str:
            print("Invalid input!Contain special characters!")
        else:
            list = str.split(',')
    return(list)   


def main():
    while list[len(list)-1] != '':  # 输入值不为空时，继续输入值
        str = input("please input name:").split(',')#将输入值以’,‘为切割符，将输入值放入str列表
        for name in str:#遍历str列表，将里面的值放入list列表
            list.append(name)
        #print(list)
        i=len(list)+1
        if list[len(list)-1]== '':  # 输入值为空，跳出循环
            list.remove('')
            break
            
'''

while i==0:#当i=0时，将输入值插入list列表
    str = input("please input name:")
    #SpecCheck(str)
    list=str.split(',')
   #print('lottery list:',list.remove(''))
    if list[len(list) - 1] == '':  # 输入值为空，跳出循环
        list.remove('')
        break
    else:
        while list[len(list) - 1] != '':  # 输入值不为空时，继续输入值
            str = input("please input name:").split(',')  # 将输入值以’,‘为切割符，将输入值放入str列表
            for name in str:  # 遍历str列表，将里面的值放入list列表
                list.append(name)
            #print('lottery list:', list.remove(''))
            i = len(list) + 1
            if list[len(list) - 1] == '':  # 输入值为空，跳出循环
                list.remove('')
                break

print("the last lottert list:",list)
print("begin lottery！")
j=int(random.randint(0,len(list)-1))#产生一个随机的整数
print("the lottery result is:",list[j])


