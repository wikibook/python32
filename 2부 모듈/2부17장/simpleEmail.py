# -*- coding: cp949 -*-
import smtplib #Import smtplib for the actual sending function

from email.mime.text import MIMEText

smtpHost = "smtp.test.com"   #smtp 서버 주소

text = "hello world"
msg = MIMEText(text)  #텍스트가 기본인 메일을 하나 생성합니다. text는 반듯이 ASCII코드여야만 합니다. 만약 unicode가 들어 있다면 받는 쪽에서 문자가 깨져있는 메일을 받게 될 것 입니다.

senderAddr = "test@send.com"     #보내는 사람 email 주소.
recipientAddr = "test@rec.com"   #받는 사람 email 주소.

msg['Subject'] = "test email"
msg['From'] = senderAddr
msg['To'] = recipientAddr

#SMTP 서버를 이용해 메일 보냅니다.
s = smtplib.SMTP(smtpHost)
s.connect()
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()
