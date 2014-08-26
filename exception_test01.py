try:
	f=open('file.txt','r')
except IOError,e:
	print e
