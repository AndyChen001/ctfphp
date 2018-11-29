#coding:utf-8

def readLine():
    file = open("sample.txt")
 
    while 1:
        line = file.readline()
        if not line:
            break
        pass # do something

    file.close()


def readAllLine():
    file = open("sample.txt")

    for line in file.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

    file.close()

    file = open('/Users/michael/test.jpg', 'rb')
    file.read()


def writeFile():
    with open('/Users/ethan/data2.txt', 'a') as f:
    f.write('three\n')
    f.write('four')
