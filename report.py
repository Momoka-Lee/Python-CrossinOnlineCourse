import sys
import os

ff=open('Report Analysis.txt','w',encoding='utf-8')

with open('report.txt', encoding='utf-8') as f:
    data = [l.strip() for l in f.readlines() if l]

ss = []
for i in data:
    p = data.index(i)
    if p==0:
       print(i,file=ff)
    if p > 0:
        student = i.split()
        student[1:] = list(map(int, student[1:]))
        total = sum(student[1:])
        student.append(total)
        gpa = round(sum(student[1:-1]) / 9, 2)
        student.append(gpa)
        ss.append(student)

new=[]
for i in range(1,12):
        for x in ss:
            new.append(x[i])
ssa=[]
l=[i for i in new]
n=30
sal=([l[i:i+n]for i in range(0,len(l),n)])
for y in sal:
    average=int(round(sum(y)/30))
    ssa.append(average)
ssa_new=[str(x) for x in ssa]
ssa_new_str=','.join(ssa_new)
print(0,ssa_new_str,file=ff)

for student in ss:
    student[1:-3] = ['不及格' if x < 60 else x for x in student[1:-3]]
ssn=sorted(ss, key=lambda s:s[-1],reverse=True)

index=0
for i in ssn:
    index+=1
    i_new=[str(x)for x in i]
    i_new_str=' '.join(i_new)
    print(index,i_new_str,file=ff)

ff.close()








































