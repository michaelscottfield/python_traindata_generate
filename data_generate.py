# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
fr = open('../work/work919/heartdisease.txt', 'r')
frr = open('../work/work919/dict.txt', 'r')
fw = open('../work/work919/train.data', 'w')
sym = []
dis = []
cty = []
des = []
tm = []
cha = []
din = []
for line in frr.readlines():
    line = line.decode("utf-8")
    x = line.strip('\n').strip(' ')
    x1 = x.split(' ')[0]
    x2 = x.split(' ')[1]
    if x2 == 'sym':
        sym.append(x1)
    if x2 == 'dis':
        dis.append(x1)
    if x2 == 'cty':
        cty.append(x1)
    if x2 == 'des':
        des.append(x1)
    if x2 == 'tm':
        tm.append(x1)
    if x2 == 'cha':
        cha.append(x1)
    if x2 == 'din':
        din.append(x1)

for line in fr.readlines():
    line = line.decode("utf-8")
    x = line.strip('\n')
    
    for xchar in x:
        flag = 0
        for term in sym:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + ' sym-S\n')
                    flag = 1
                    break
                if xchar == term[0]:
                    fw.write(xchar + ' sym-B\n')
                    flag = 1
                    break
                if xchar == term[-1]:
                    fw.write(xchar + ' sym-E\n')
                    flag = 1
                    break
                else:
                    fw.write(xchar + ' sym-M\n')
                    flag = 1
                    break
        if flag == 1:
            break
        for term in dis:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + ' dis-S\n')
                    flag = 1
                    break
                if xchar == term[0]:
                    fw.write(xchar + ' dis-B\n')
                    flag = 1
                    break
                if xchar == term[-1]:
                    fw.write(xchar + ' dis-E\n')
                    flag = 1
                    break
                else:
                    fw.write(xchar + ' dis-M\n')
                    flag = 1
                    break
        if flag == 1:
            break
        for term in cty:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + ' cty-S\n')
                    flag = 1
                    break
                if xchar == term[0]:
                    fw.write(xchar + ' cty-B\n')
                    flag = 1
                    break
                if xchar == term[-1]:
                    fw.write(xchar + ' cty-E\n')
                    flag = 1
                    break
                else:
                    fw.write(xchar + ' cty-M\n')
                    flag = 1
                    break
        if flag == 1:
            break
        for term in des:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + ' des-S\n')
                    flag = 1
                    break
                if xchar == term[0]:
                    fw.write(xchar + ' des-B\n')
                    flag = 1
                    break
                if xchar == term[-1]:
                    fw.write(xchar + ' des-E\n')
                    flag = 1
                    break
                else:
                    fw.write(xchar + ' des-M\n')
                    flag = 1
                    break
        if flag == 1:
            break
        for term in tm:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + ' tm-S\n')
                    flag = 1
                    break
                if xchar == term[0]:
                    fw.write(xchar + ' tm-B\n')
                    flag = 1
                    break
                if xchar == term[-1]:
                    fw.write(xchar + ' tm-E\n')
                    flag = 1
                    break
                else:
                    fw.write(xchar + ' tm-M\n')
                    flag = 1
                    break
        if flag == 1:
            break
        for term in cha:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + ' cha-S\n')
                    flag == 1
                    break
                if xchar == term[0]:
                    fw.write(xchar + ' cha-B\n')
                    flag == 1
                    break
                if xchar == term[-1]:
                    fw.write(xchar + ' cha-E\n')
                    flag == 1
                    break
                else:
                    fw.write(xchar + ' cha-M\n')
                    flag == 1
                    break
        if flag == 1:
            break
        for term in din:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + ' din-S\n')
                    flag = 1
                    break
                if xchar == term[0]:
                    fw.write(xchar + ' din-B\n')
                    flag = 1
                    break
                if xchar == term[-1]:
                    fw.write(xchar + ' din-E\n')
                    flag = 1
                    break
                else:
                    fw.write(xchar + ' din-M\n')
                    flag = 1
                    break
        if flag == 1:
            break
        fw.write(xchar + ' O\n')
