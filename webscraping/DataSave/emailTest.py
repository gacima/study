# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The test e-mail.')

msg['Subject'] = "Testing"
msg['From'] = 'yalongl@ncsi.com.cn'
msg['To'] = 'yalongl@ncsi.com.cn'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()