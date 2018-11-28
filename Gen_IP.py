#coding:utf-8

def ip2num(ip):
    ips = [int(x) for x in ip.split('.')]
    return ips[0]<< 24 | ips[1]<< 16 | ips[2] << 8 | ips[3]

def num2ip (num):
    return '%s.%s.%s.%s' % ((num >> 24) & 0xff, (num >> 16) & 0xff, (num >> 8) & 0xff, (num & 0xff))
    #return '%s.%s.%s.%s' % ((num & 0xff000000)>>24,(num & 0x00ff0000)>>16,(num & 0x00000ff00)>>8,num & 0x000000ff)


def gen_ip(ip):
    start ,end = [ip2num(x) for x in ip.split('-')]
    return [num2ip(num) for num in range(start,end+1) if num & 0xff]

#print gen_ip("172.16.5.10-172.16.5.35")
