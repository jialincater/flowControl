import urllib2
import urllib
import re
import time
Limit=10485760
cnt=0
def login(ID,passWord):
	#print "login with "+ID+"\n"
	info = {'DDDDD':ID,
	'upass':passWord,
	'0MKKey':'123456'}
	key = urllib.urlencode(info)
	url = "http://gw.bupt.edu.cn"
	door = urllib2.Request(url,key)
	#print door
	res = urllib2.urlopen(door).read()
	#print res

def logout():
	url = "http://gw.bupt.edu.cn/F.htm"
	door = urllib2.Request(url)
	res = urllib2.urlopen(door).read()
	#print res

def getFlow():
	url = "http://gw.bupt.edu.cn/"
	door = urllib2.Request(url)
	res = urllib2.urlopen(door).read()
	#print res
	l = re.search(r'flow=\'(\d+)',res)
	if l:
		n = l.group(0)
	else:
		#print "login unsuccess, next ID\n"
		return -1
	m = re.search(r'\d+',n)
	if m:
		r=m.group(0)
		return int(r)
	else:
		#print "login unsuccess, next ID\n"
		return -1

def readIDList(cnt):
	file_object = open('s.log')
	all_the_text = file_object.read()
	file_object.close()
	line=all_the_text.split('\n')[cnt]
	info=line.split(' ')
	ID=info[0]
	passWord=info[1]
	print "now login with ID "+ID
	login(ID,passWord)

def test():
	flow=getFlow()
	#print flow
	if flow<0 or flow>=Limit:
		global cnt
		cnt+=1
        #logout()
		print "login unsuccess or flow execced\n"
		return False
	else:
		print "check success with flow stage: "+str(flow/(Limit/10))
		return True

def fuckYourSelf():
	# read ID list
	logout()
	while True:
		global cnt
		readIDList(cnt)
		while test():
			time.sleep(30)

fuckYourSelf()
