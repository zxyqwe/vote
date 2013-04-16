#!/usr/bin/env python
#coding=utf-8
#Thanks for DingYuntong

import sys,re,os
import gevent
import gevent.monkey
import requests
from pyquery import PyQuery

PORT = ['8080','80','43','3128','43']
urls=[]
gevent.monkey.patch_all()

def get_proxy(url):
	try:
		r = requests.get(url)#plz set timeout
		r.encoding='gb2312'
		d = PyQuery(r.text)
		for item in d("#proxylisttb table tr td"):
			ip = item.text
			if ip and re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ip):
				print ip
	except gevent.queue.Empty:
		print 'get_proxy quit!'

def vote():
	pass #do as your wish

if __name__ == '__main__':
	get_proxy("http://www.cnproxy.com/proxy1.html")
