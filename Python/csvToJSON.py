# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 17:07:25 2015

@author: Laura Pang
"""

import csv
import json
import collections

with open('../OD/andorra0902_0.csv', 'rb') as f:
    reader = csv.reader(f)
    arr = list(reader)
dic_fixed = []
dic = {}
for r in range(1,len(arr)):
    for c in range(1,len(arr[0])):
        nodea = min(arr[0][c],arr[r][0])
        nodeb = max(arr[r][0],arr[0][c])
        val = int(arr[r][c])
        if val==0:
            continue
        if (nodea not in dic_fixed):
            dic_fixed.append(nodea)
        if (nodeb not in dic_fixed):
            dic_fixed.append(nodeb)
        if nodea in dic:
            if nodeb in dic[nodea]:
                dic[nodea][nodeb]=dic[nodea][nodeb]+val
            else:
                dic[nodea][nodeb]=val
        else:
            dic[nodea]={nodeb: val}
        #print arr[r][c]
#print dic_fixed
print len(dic_fixed)
nodeList = []
linkList = []
x =0
y=500
for el in dic_fixed:
    nodeList.append({"name":el,"group":1,"x":x, "y": y})
    x+=1
    y+=1
for ob in dic:
    for ob2 in dic[ob]:
        ind1 = dic_fixed.index(ob)
        ind2 = dic_fixed.index(ob2)
        linkList.append({"source":ind1,"target":ind2,"value": dic[ob][ob2]})
#print linkList        
print len(nodeList)
finalList = {"nodes":nodeList,"links":linkList}
with open("../Web/JSON/cdrAndorra.json", 'w') as json_file:
        json_file.write(json.dumps(finalList))
