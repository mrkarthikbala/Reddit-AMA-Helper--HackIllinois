import smtplib, time
import test
def setup():
        server = smtplib.SMTP("smtp.gmail.com","587")
        server.starttls()
        server.login('amahelper@gmail.com', 'hackIllinois')
	return server
def send_top_ama():
	server = setup()
	submissions = test.login()
	for x in submissions:
		print str(x)
		#server.sendmail('amahelper@gmail.com', '6308158668@txt.att.net', str(x))
		server.sendmail('amahelper@gmail.com', '6306188778@tmomail.net', "Now on Reddit IAMA" + str(x))
	





while(True):
	if int(time.strftime("%M")) % 10 == 0:

	send_top_ama()	
	
	time.sleep(60)
