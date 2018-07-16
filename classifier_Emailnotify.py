import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
fromaddr = "collinsbunde@gmail.com"
toaddr = "collinsbunde@yahoo.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ATTACHMENT"
 
body = "YOH MAN GET THIS FILE"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "biomeetris.PNG"
attachment = open("C:/Users/BUNDEX-PC/Desktop/twitter sentiment analysis", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "MULEcob1494")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
