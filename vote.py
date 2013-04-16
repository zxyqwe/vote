#!/usr/bin/env python
#coding=utf-8
#Thanks for DingYuntong

import sys,re,os
import gevent
import gevent.monkey
import urllib2
from pyquery import PyQuery

PORT = ['8080','80','43','3128','43']
urls=[]
gevent.monkey.patch_all()

def get_proxy(url):
	try:
		r = urllib2.urlopen(url)
		d = PyQuery(r.read())
		for item in d("#proxylisttb table tr td"):
			ip = item.text
			if ip and re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ip):
				print ip
	except Exception as e:
		print e
		print 'get_proxy quit!'

def vote():
	pass #do as your wish

if __name__ == '__main__':
	get_proxy("http://www.cnproxy.com/proxy1.html")
