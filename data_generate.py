# coding=utf-8

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

for linee in fr.readlines():
    x = linee.strip('\n')
    #y = unicode(x, "gb2312")

    #print linee.decode("gb2312")
    for i in range(0, len(x)):
        fw.write(x[i])
    ''' for term in sym:
            if xchar in term:
                if xchar == term:
                    #fw.write(xchar + 'sym-S')
                    break
                if xchar == term[0]:
                    fw.write(xchar)
                    #fw.write(term[0] + 'ok')
                    break
                if xchar == term[-1]:
                    #fw.write(xchar + 'sym-E')
                    break
                else:
                    #fw.write(xchar + 'sym-M')
                    break'''
    '''for term in dis:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + 'dis-S')
                    break
                if xchar == term[0]:
                    fw.write(xchar + 'dis-B')
                    break
                if xchar == term[-1]:
                    fw.write(xchar + 'dis-E')
                    break
                else:
                    fw.write(xchar + 'dis-M')
                    break
            else:
                fw.write(xchar + 'O')
                break
        for term in cty:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + 'cty-S')
                    break
                if xchar == term[0]:
                    fw.write(xchar + 'cty-B')
                    break
                if xchar == term[-1]:
                    fw.write(xchar + 'cty-E')
                    break
                else:
                    fw.write(xchar + 'cty-M')
                    break
            else:
                fw.write(xchar + 'O')
                break
        for term in des:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + 'des-S')
                    break
                if xchar == term[0]:
                    fw.write(xchar + 'des-B')
                    break
                if xchar == term[-1]:
                    fw.write(xchar + 'des-E')
                    break
                else:
                    fw.write(xchar + 'des-M')
                    break
            else:
                fw.write(xchar + 'O')
                break    
        for term in tm:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + 'tm-S')
                    break
                if xchar == term[0]:
                    fw.write(xchar + 'tm-B')
                    break
                if xchar == term[-1]:
                    fw.write(xchar + 'tm-E')
                    break
                else:
                    fw.write(xchar + 'tm-M')
                    break
            else:
                fw.write(xchar + 'O')
                break 
        for term in cha:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + 'cha-S')
                    break
                if xchar == term[0]:
                    fw.write(xchar + 'cha-B')
                    break
                if xchar == term[-1]:
                    fw.write(xchar + 'cha-E')
                    break
                else:
                    fw.write(xchar + 'cha-M')
                    break
            else:
                fw.write(xchar + 'O')
                break 
        for term in din:
            if xchar in term:
                if xchar == term:
                    fw.write(xchar + 'din-S')
                    break
                if xchar == term[0]:
                    fw.write(xchar + 'din-B')
                    break
                if xchar == term[-1]:
                    fw.write(xchar + 'din-E')
                    break
                else:
                    fw.write(xchar + 'din-M')
                    break
            else:
                fw.write(xchar + 'O')
                break '''
