import smtplib, time
from amahelp import *
from users import *
def setup():
        server = smtplib.SMTP()
	server.connect("smtp.gmail.com", "587")
	server.ehlo()
        server.starttls()
        server.login('amahelper@gmail.com', 'hackIllinois')
	return server
def init_users():
	##something somehing webform get file make user object out of file
	theusers = Users()
	theusers.buildUser("6306188778|T Mobile~300")
	return theusers

def clear_file():
	f = open("user_info.txt","w").close()
def send_top_ama():
	server = setup()
	theusers = init_users()
	submissions = login()
	for x in submissions:
	#	theusers.refresh()
		for user in theusers.myusers:
			print str(x)
			print x.ups
			if x.ups <= user.quality:
				recipient = str(user.number) + str(user.provider)
				server.sendmail("amahelper@gmail.com", recipient, str(x)) #AND LINK
	server.quit()

def main():
	clear_file()
	while(True):
		a = int(time.strftime("%M"))
		if a < 60:

			send_top_ama()	
		
		time.sleep(600)

main()
