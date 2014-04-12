import time

print type(time.strftime("%M"))
if int(time.strftime("%M")) % 16 == 0:
	print "hello"
