import traceback
try:
	1/0
except Exception,e:
	print traceback.format_exc()
#except Exception,e:
#	print "Error:",e
