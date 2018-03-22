# Sending email


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


email_user = 'sender@gmail.com'
email_password = 'put your password here'
email_rcver = 'receiver@gmail.com'

subject = 'put your sub here'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_rcver
msg['Subject'] = subject

body = "write down body of the email here"
msg.attach(MIMEText(body, 'plain'))

filename = 'filepath'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('content-disposition', "attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email_rcver, text)
server.quit()
