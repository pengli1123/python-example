from socket import *
import urllib
import threading
import time
import urllib2
import random
import cookielib

setdefaulttimeout(10)

class BasicClass:
    def __init__(self):
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')]

    def postData(self, data):
        leet = 1337
        while leet == 1337:
            try:
                url = self.opener.open(data)
                url = url.read()
                leet = 0
            except:
                print '     lag'

        return url

    def postData2(self, data, data2):
        leet = 1337
        while leet == 1337:
            try:
                url = self.opener.open(data, data2)
                url = url.read()
                leet = 0
            except:
                print '     lag'
        return url
def grabNames(source):
    leet = 1337
    totalAccts = 0
    names = []
    IDS = []
    sour = source.split('Trustee Access')[1]
    acctReader = sour.split('\n')
    
    c = 0
    while leet == 1337:
        acctCode = acctReader[c].strip()

        if acctCode.find('world.php?suid=') != -1:
            temp = acctReader[c].split('world.php?suid=')[1].split('&serverid')[0]
            IDS.append(temp)
            totalAccts = totalAccts + 1
        elif acctCode.find('star.jpg') != -1:
            if acctReader[c+3].find('</b>') != -1:
                temp = acctReader[c+3].split('</b>')[0].split('<b>')[1]
                names.append(temp)
        elif acctCode.find('</html>') != -1:
            leet = 0
        c = c + 1

    return names, IDS, totalAccts

x = BasicClass()
interval = raw_input('Interval in seconds: ')

while True:
    for i in range(1,8):
        print 'On sss' + str(i)
        login = x.postData2('http://zimbob.outwar.com/accounts.php?ac_serverid=4', 'login_username=sss' + str(i) + '&login_password=yomomma123')
        login = x.postData('http://zimbob.outwar.com/accounts.php?ac_serverid=4')
        temp = grabNames(login)

        names = temp[0]
        ids = temp[1]

        c = 0
        while c < len(names):
            rem = x.postData('http://zimbob.outwar.com/myaccount_trust_remove.php?trustee=' + ids[c] + '&ac_serverid=4')
            print '\t' + names[c] + ' removed'
            c += 1
    print 'DONE'
    print 'Waiting ' + interval + ' to restart\n'
    time.sleep(int(interval))

