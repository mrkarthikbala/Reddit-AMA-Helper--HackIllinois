#!/usr/local/bin/python3

import cgi

def getData():
	formData = cgi.FieldStorage()
	number = formData.getvalue(number)
	return number