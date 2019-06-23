file = open('b_lovely_landscapes.txt','r')
v_h = []
tags = []
img_tags = []
temp_tag = []
max_len = 0
img_dict = {}
for i,f in enumerate(file):
    if i == 0:
        total_num = int(f)
    else:
        l = f.split(' ')
        v_h.append(l[0])
        for t in l[2:]:
            tags.append(t.strip())
            temp_tag.append(t.strip())
        leng = len(temp_tag)
        img_dict[i-1] = leng
        if leng > max_len:
            max_len = leng
            max_len_img = i - 1
        #tags.extend(l[2:])
        img_tags.append(temp_tag)
        temp_tag = []

x = img_dict
from operator import itemgetter
s = sorted(x.items(), key=itemgetter(1),reverse = True)

r = open('sub.txt','w')
r.write(str(len(s)))
r.write('\n')
for i in s:
    r.write(str(i[0]))
    r.write('\n')
r.close()