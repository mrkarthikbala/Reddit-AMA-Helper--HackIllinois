import smtplib, time
from amahelp import *
from users import *
from emailChecker import *
from datetime import datetime

def setup():
        server = smtplib.SMTP()
	server.connect("smtp.gmail.com", "587")
	server.ehlo()
        server.starttls()
        server.login('amahelper@gmail.com', 'hackIllinois')
	return server
def init_users():
	theEmails = getEmailData()

	theusers = Users()

	for i in theEmails:
		userinfo = parseEmailData(theEmails[i])
		theusers.buildUser(userinfo[0] + "|" + userinfo[1] + "~" + "300")
		
	
	return theusers

def clear_file():
	f = open("user_info.txt","w").close()
def send_top_ama():
	server = setup()
	theusers = init_users()
	submissions = login()
	#	theusers.refresh()
	for user in theusers.myusers:
		recipient = str(user.number) + str(user.provider)
		
		for x in submissions:	
			thattime = x.created
			now = time.time() #11-13
			t1 = str(thattime)
			t2 = str(now)
			if x.ups >= int(user.quality) and x.ups < 1000 and float(t2)-float(t1)< 10000	:
				server.sendmail("amahelper@gmail.com", 					recipient, str(x)) #AND LINK
	server.quit()

def main():
	clear_file()
	while(True):
		a = int(time.strftime("%M"))
		if a < 60: #change for demo

			send_top_ama()	
		
			time.sleep(600)

main()
