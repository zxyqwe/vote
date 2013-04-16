#!/usr/bin/env python
#coding=utf-8
#Thanks for DingYuntong

import sys,re,os
import gevent
import gevent.monkey
import urllib2
import urllib
import socket
from pyquery import PyQuery

ports = ['8080','80','43','3128']
urls=[]
gevent.monkey.patch_all()

def get_proxy(url):
	try:
		r = urllib2.urlopen(url)
		d = PyQuery(r.read())
		for item in d("#proxylisttb table tr td"):
			ip = item.text
			if ip and re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ip):
				urls.append(ip)
		for port in ports:
			jobs = [gevent.spawn(vote,ip,port) for ip in urls]
		gevent.joinall(jobs)
		r.close()
	except Exception as e:
		print e
		print 'get_proxy quit!'

def vote(ip,port):
	try:
		r = urllib.urlopen(r'http://hi.baidu.com/zxyqwe',proxies = {'http':('http://'+ip+':'+port)}) 
		print ip,port	
		r.close()
	except Exception as e:
		print e	
		pass	

if __name__ == '__main__':
	socket.setdefaulttimeout(5)
	for i in range(1,3):
		get_proxy("http://www.cnproxy.com/proxyedu"+str(i)+".html")
	for i in range(1,11):
		get_proxy("http://www.cnproxy.com/proxy"+str(i)+".html")
