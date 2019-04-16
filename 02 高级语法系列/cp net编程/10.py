from email.mime.text import MIMEText
from email.header import Header
text = input("请输入邮件内容:")
msg = MIMEText(text,"plain","utf-8")

header_from = Header("从陈鹏邮箱用代码发出去的邮件<chenpeng9750@foxmail.com>","utf-8")
msg["From"] = header_from
# 填写接受者信息
header_sub = Header(input("邮件的主题为:"))
msg["Subject"] = header_sub
# 输入Email地址和口令:
from_addr = "chenpeng9750@foxmail.com"
print(from_addr)
password = "umndufctjbnkjfcg"
# 输入SMTP服务器地址:
smtp_server = "smtp.qq.com"
# 输入收件人地址:
to_addr = input('To: ')
print(to_addr)
header_to = Header("接收者:{0}".format(to_addr),"utf-8")
msg["TO"] = header_to

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

