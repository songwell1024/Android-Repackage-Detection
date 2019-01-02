#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: ElementMappedToCharacter.py
@time: 2018/11/12/012 19:41
@desc:  元素映射成为字母
'''


def getElementDictionary(EleTup1, EleTup2):
    ElementArr = mergeTuple(EleTup1, EleTup2)
    ElementDict = {}
    i = 0
    for x in range(ord('a'), ord('z') + 1):
        ElementDict[ElementArr[i]] = chr(x)
        i = i + 1
    return ElementDict

def  mergeTuple(EleTup1, EleTup2):
    ElementArr = []
    i = j = k = 0
    while i < 26:
        if (EleTup1[j] is not None) & (EleTup2[k] is not None):
            if EleTup1[j][1] > EleTup2[k][1]:
                if ElementArr.__contains__(EleTup1[j][0]):
                    j = j + 1
                else:
                    ElementArr.append(EleTup1[j][0])
                    j = j +1
                    i = i + 1
            else:
                if ElementArr.__contains__(EleTup2[k][0]):
                    k = k + 1
                else:
                    ElementArr.append(EleTup2[k][0])
                    k = k + 1
                    i = i + 1
    return ElementArr
