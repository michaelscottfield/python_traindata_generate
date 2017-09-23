# -*- coding: UTF-8 -*-

# 打开一个文件

fr = open("../work/work919/词性标注4.txt", "r")
fw = open("../work/work919/dict.txt", "w")

for line in fr.readlines():
    item = line.split(' ')[0]
    str = line.split(' ')[1].strip('\n')
    if str == '症状词':
        fw.write(item + ' sym\n')
    if str == '疾病词':
        fw.write(item + ' dis\n')
    if str == '查体词':
        fw.write(item + ' cty\n')
    if str == '表现词':
        fw.write(item + ' des\n')
    if str == '时间词':
        fw.write(item + ' tm\n')
    if str == '性状词':
        fw.write(item + ' cha\n')
    if str == '方位词':
        fw.write(item + ' din\n')

