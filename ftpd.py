#coding:utf-8

import os
import filecmp

from ftplib import FTP

src_dir = "E:\\xxx\\src"
dst_dir = "E:\\xxx\\dst"

def ftp_down_files():
    try:
        ftp = FTP()
        ftp.set_debuglevel(2)
        timeout = 30
        port = 21
        ftp.connect('0.0.0.0',port,timeout)
        ftp.login('root','root')
        print ftp.getwelcome()

        remotepath = "/xxx/web.tar"
        localpath = "D:/xxx/web.tar"

        bufsize = 1024
        fp = open(localpath, 'wb')
        ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
        ftp.set_debuglevel(0)
        fp.close()
        ftp.quit()
        print "Download fiel success"
    except Exception, e:
        print "连接或登录失败"
        print e

def cmp_files(src_dir, dst_dir):
    dc = filecmp.dircmp(src_dir, dst_dir)
    #print "common files : ", dc.common_files
    #print "Left : ", dc.left_list
    #print "Right : ", dc.right_list
    #print "Left Only : ", dc.left_only
    print "Right Only : ", dc.right_only


ftp_down_files()
