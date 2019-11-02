import requests
import re
import shutil
import threading

first = int(input('请输入初始页码'))
last = int(input('请输入终止页码'))
print('开始下载')

for i in range(first, last + 1):
    if i == 1:
        url = 'http://www.cxdq.com/'
    else:
        url = 'http://www.cxdq.com/index_%d.htm' % i


        req=requests.get(url)
        data=req.text
        img=re.findall(r'http.*?jpg',data)
        lst=[]
        for j in img:
            lst.append(j)

        def download(x):
            resp=requests.get(x,headers={'referer':'http://m.cxdq.com'},stream=True)
            file_name=x.split('/')[-1]+'.jpg'
            file=open(file_name,'wb')
            resp.raw.decode_content=True
            shutil.copyfileobj(resp.raw,file)
            print(file_name,'下载完成')
            del resp

        thread=[]
        files=range(len(lst))
        for i in files:
            t=threading.Thread(target=download,args=(lst[i],))
            thread.append(t)
        for i in files:
            thread[i].start()
        for i in files:
            thread[i].join()

print('全部页面下载完成')




