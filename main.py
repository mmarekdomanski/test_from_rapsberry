import os
import datetime

dir0 = '/'
dir1 = 'home'
dir2 = 'pi'
dir3= 'PycharmProjects'
dir4 = 'testy'
dir5 = 'working'
file_name = 'text_2.txt'

dir = os.path.join(dir0, dir1, dir2, dir3, dir4, dir5)
path = os.path.join(dir, file_name)
#path = dir + file_name
file = open(path, 'a')
file.write('linika\n')
file.close()

with open(path, 'a') as f:
    f.write('line\n')

if os.path.exists(path):
    print('ok exists {}'.format(file_name))

print(os.listdir(dir))


(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(path)

a = datetime.datetime.fromtimestamp(mode)
b = datetime.datetime.fromtimestamp(ino)
c = datetime.datetime.fromtimestamp(dev)
d = datetime.datetime.fromtimestamp(nlink)
e = datetime.datetime.fromtimestamp(uid)
f = datetime.datetime.fromtimestamp(gid)
g = datetime.datetime.fromtimestamp(size)
h = datetime.datetime.fromtimestamp(atime)
data_modyfikacji = datetime.datetime.fromtimestamp(mtime)
i = datetime.datetime.fromtimestamp(ctime)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(data_modyfikacji)
print(i)

