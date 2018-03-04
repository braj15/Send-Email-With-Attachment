# Sending email


import smtplib

email_user = 'braj1902@gmail.com'
email_rcver = 'braj95644@gmail.com'

message = "Hi there, I'm sending this email using python! Pretty coool, huh!!!"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, 'thed@mnmailer123')

server.sendmail(email_user, email_rcver, message)
server.quit()
