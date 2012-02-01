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
	
        while True:
            try:
                url = self.opener.open(data)
                url = url.read()
                break
            except:
                print '     lag'

        return url
		
x = BasicClass()
interval = raw_input('Interval in seconds: ')

while True:

	login = x.postData('google.com')
	
    print 'DONE'
    print 'Waiting ' + interval + ' to restart\n'
    time.sleep(int(interval))

