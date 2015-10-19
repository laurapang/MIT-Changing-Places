import csv

with open('../OD/andorra0902_0.csv', 'rU') as f:
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

with open('./links_towers.csv', "a") as csvfile:
    tower_writer = csv.writer(csvfile, delimiter=',')
    header = ['target', 'source', 'flow']
    tower_writer.writerow(header)
    for ob in dic:
        for ob2 in dic[ob]:
            ind1 = dic_fixed.index(ob)
            ind2 = dic_fixed.index(ob2)
            # linkList.append({"source":ind1,"target":ind2,"value": dic[ob][ob2]})
            tower_writer.writerow([ind2,ind1, dic[ob][ob2]*10000])

