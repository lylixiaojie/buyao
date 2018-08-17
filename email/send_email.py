#!bin/python
# -*- coding: utf-8 -*-

#author:lixj
#date:18.8.17
#this is test send email

import smtplib
from email.mime.text import MIMEText

#信的文本
email_text = MIMEText('nihao,woshi lixiaojie ,send by lixj..','plain','utf-8')

user = '1397500399@qq.com'
passwd = 'ffaukqfltuebgheb'

#收件箱
email_to = 'lylixiaojie@163.com'

#收件邮箱地址
smtp_server = 'smtp.qq.com'

#连接服务器
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
#登录
server.login(user,passwd)


#发送邮件（发件人邮箱，收件人邮箱，内容）
server.sendmail(user,[email_to],email_text.as_string())
print(email_text)
print(email_text.as_string())
#关闭连接
server.quit()