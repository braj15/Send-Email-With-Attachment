# Sending email


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


email_user = 'braj1902@gmail.com'
email_password = 'thed@mnmailer123'
email_rcver = 'braj95644@gmail.com'

subject = 'Python is cool!'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_rcver
msg['Subject'] = subject

body = "Hi there, I'm sending this email using python! Pretty coool, huh!!!"
msg.attach(MIMEText(body, 'plain'))

filename = 'YAY.gif'
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
