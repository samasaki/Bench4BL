#-*- coding: utf-8 -*-

import time


###############################################################################################################
class DiffTimer(object):
	last = None
	
	def __init__(self):
		self.set()
		pass
	
	def set(self):
		self.last = time.time()
		pass
	
	def diff(self):
		diff = time.time() - self.last
		self.set()
		return diff
	
	def diff_millisecond(self):
		diff = int(self.diff()*1000)
		return '%dms' % diff
	
	def diff_seconds(self):
		diff = int(self.diff()*1000)
		return '%ds %dms' % (diff/1000, diff%1000)
		
	def diff_minute(self):
		diff = int(self.diff())
		return '%dm %ds' % (diff/60, diff%60)
	
	def diff_hour(self):
		diff = int(self.diff())
		m = diff/60
		return '%dh %dm %ds' % (m/60, m%60, diff%60)
	
	def diff_day(self):
		diff = int(self.diff())
		m = diff/60
		h = m/60
		return '%dd %dh %dm' % (h/24, h%24, m)

	def diff_auto(self):
		diff = int(self.diff()*1000)
		ms = diff%1000  #get millisecond
		s = diff/1000
		m = s/60		#get minute
		s = s%60
		h = m/60
		m = m%60
		d = h/24
		h = h%24

		text = ''
		if d!=0:
			text += '%dd '%d
		if h!=0 or text!='':
			text += '%02d:'%h
		if m!=0 or text!='':
			text += '%02d:'%m
		if s!=0 or text!='':
			text += '%02d.'%s
		if ms!=0 or text!='':
			text += '%03d.'%ms
		text = text[:-1]

		if len(text)==0:
			text ='0ms'
		elif len(text)<2:
			text += 'ms'
		return text
