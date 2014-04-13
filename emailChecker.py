import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('amahelper@gmail.com', 'hackIllinois')
mail.list()
print mail.select('inbox')
result, data = mail.search(None, 'ALL')

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]
message = email.message_from_string(raw_email)
print message['From']
for part in message.walk():
	if part.get_content_type() == 'text/plain':
		print part.get_payload()