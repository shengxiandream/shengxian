import hashlib
import os

pa='a123'

pas = hashlib.sha3_256(pa.encode('utf-8')).hexdigest()
print(pas)
# a = 'C:/Users/jiang/Desktop/python1904/tian/static/upload/2019/07/09/logo20190709142734462.jpg'
# b = a.split[-3:-1]
# print(b)


path=os.path.abspath(r'C:\Users\jiang\Desktop\python1904\tian\d\2019/07/09\logo201907091438281static/uploa4.jpg')
#
# print(path)
# print(path[39:])
# cd = path[39:]
# ca=os.path.abspath(cd)
# print(ca)
# print(os.path.exists(path))
# bc = 'C:\Users\jiang\Desktop\python1904\tian\static/upload\2019/07/09\logo2019070914382814.jpg'
ab=path.replace('\\','/')
# print(ab)
# dd=ab.lstrip('C')
# dd=os.path.relpath(path)
# dd = os.path.basename(ab)
# dd = ab.split('/')[-6:]
# dc = str(dd)
# aa=dc.replace(',','/')
print(ab,type(ab))

for i in [1,2,3,4]:
    print(i)


