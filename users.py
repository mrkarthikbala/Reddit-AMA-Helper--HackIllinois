
#our users!

#users set up in file as
#phonenumber|provider~quality 

class Users:
	myusers = []
	def __init__(self):
		pass
	def refresh(self):
		f = open("user_info.txt","r")
		lines = f.readlines()
		for line in lines:
			self.myusers.append(self.buildUser(line))
		f.close()
	def buildUser(self, info_string):
		number = info_string[:info_string.find("|")]
		provider = info_string[info_string.find("|"):info_string.find("~")]
		quality = info_string[info_string.find("~") :]

		auser = User(number, provider, quality[1:])
		self.myusers.append(auser)
		return auser
		
	def remove(self, auser):
		f = open("user_info.txt","r")
		lines = f.read_lines
		outlines = []
		for i in users:
			if i.number == auser.number:
				users.remove(i)
		for i in lines:
			number = i[:i.find("|")]
			if not number == auser.number:
				outlines.append(i)
		f.close()
		f = open("user_info.txt", "w")
		for i in outlines:
			f.write(i)
		f.close()

			
	
	
		

		
class User:
	def __init__(self, anumber, aprovider, qualityPreference ):
		self.number = anumber
		self.provider = self.chooseprovider(aprovider)
		self.quality = qualityPreference #not doing anything with this yet
		##write to file
		f = open("user_info.txt", "r")
		lines = f.readlines()
		f.close()
		lines.append(str(self.number) + "|" + str(self.provider) + "~" + str(self.quality))
		f = open("user_info.txt", "w")
		f.writelines(lines)
		f.close()

		
	def chooseprovider(self, aprovider): #LOOK INTO THIS
		aprovider = aprovider[1:]
		if  "T Mob" in aprovider:
			return "@tmomail.net"
		elif "AT" in aprovider:
			return "@txt.att.net"
		elif "zon" in aprovider:
			return "@vtext.com"
		else:
			return ""
