import glob, os, shutil
import win32api

os.chdir('C:/Users/'+os.getlogin()+'/Desktop')
a = ['INI', 'LNK']
for file in glob.glob("*.*"):
    i = len(file)-1
    s = ''
    k = 0
    while(file[i] != '.'):
        s = s + file[i]
        k+=1
        i-=1
    s = s[::-1]
    s = s.upper()
    if(s not in a):
        newpath = 'C:/Users/'+os.getlogin()+'/Documents/'+s
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        if not os.path.exists(newpath+'/'+file):
            shutil.move('C:/Users/'+os.getlogin()+'/Desktop/'+file, newpath)
        else:
            os.remove('C:/Users/'+os.getlogin()+'/Desktop/'+file)

#print("Enter the directory : ")
#dir = input()


for dir in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
    print(dir)
    dict = {}
    b = []
    for root, dirs, files in os.walk(dir):
        for f in files:
            a = []
            filename = os.path.join(root, f)
            try:
                filesize = os.path.getsize(filename) >> 20
            except IOError:
                print('',end='')
                continue
            a.append(filesize)
            a.append(filename)
            b.append(a)
    b = sorted(b, reverse = True)
    for i in range (0,10):
        if(i < len(b)):
            print(b[i][0], end = ' MB\t\t')
            print(b[i][1])