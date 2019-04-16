# 导入相应的包
import smtplib
from email.mime.text import MIMEText

# MIMEText三个主要的参数
# 1, 邮件内容
# 2, MIME子类型 在此案例我们用plain表示text类型
# 3, 邮件编码格式

msg = MIMEText("HEllo, This is email,I sent you with a software program"
               ,"plain","utf-8")
# 发送email地址 ,此地址用我的email邮箱
from_addr = "chenpeng9750@foxmail.com"
# 此吃密码是申请授权后的授权码,不是邮箱密码
from_pwd = "umndufctjbnkjfcg"
# 收件人信息
# 此吃使用qq邮箱
to_addr = "245141214@qq.com","1216250635@qq.com","chenpeng9750@163.com"

# 输入SMTP服务器地址
# 此处根据不同服务器写不同的地址
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
# 腾讯qq邮箱所的smtp地址是 smtp.qq.com
smtp_srv = "smtp.qq.com"

try:
    # 两个参数
    # 第一个是服务器地址,但一定是bytes格式,需要编码
    # 第二个参数是服务器接受访问的端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465) # SMtp协议默认端口是25
    srv.debuglevel(1)
    # 登录邮箱发送
    srv.login(from_addr,from_pwd)
    # 发送邮件
    # 三个参数
    # 1, 发送地址
    # 2, 接受地址,必须是list形式
    # 3, 发送内容,作为字符串发送
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)