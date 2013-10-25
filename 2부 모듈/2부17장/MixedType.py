# -*- coding: cp949 -*-
import smtplib
import mimetypes

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#global value
host = "smtp.test.com" #your smtp address
htmlFileName = "logo.html"
imageFileName = "logo.gif"

senderAddr = "test@send.com"     #보내는 사람 email 주소.
recipientAddr = "test@rec.com"   #받는 사람 email 주소.

#create MMIMEBase 
msg = MIMEBase("multipart", "mixed")

msg['Subject'] = "Test email in Python 3.0"
msg['From'] = senderAddr
msg['To'] = recipientAddr

#Make MIMEType
htmlFD = open(htmlFileName, 'rb')
HtmlPart = MIMEText(htmlFD.read(), _charset = 'UTF-8' )
htmlFD.close()

imageFD = open(imageFileName, 'rb')
ImagePart = MIMEImage(imageFD.read())
imageFD.close()

# 만들었던 mime을 MIMEBase에 첨부 시킨다.
msg.attach(ImagePart)
msg.attach(HtmlPart)

#헤더에 첨부 파일에 대한 정보를 추가 시킨다.
msg.add_header('Content-Disposition','attachment',filename=imageFileName)

msg['Subject'] = "test python email"
msg['From'] = senderAddr
msg['To'] = recipientAddr


#메일을 발송한다.
s = smtplib.SMTP(host)
s.connect()
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()
