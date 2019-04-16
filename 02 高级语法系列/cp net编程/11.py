from email.mime.text import MIMEText
import smtplib
from email.header import Header
mail_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>陈鹏的个人主页</title>
                <style>
                    *{margin: 0;padding: 0}
                    div{
                        border: 1px solid #ffffff;
                        margin: auto;
                        font-family: '隶书';
                        box-sizing: border-box;
                    }
                    a{
                        text-decoration: none;
                        /*color: #000000;*/
                    }
                    .header{
                        height: 768px;
                        background: url("./images/1552967579194.jpg");
                    }
                    .head-box1{
                        border-radius: 50%;
                        font-size: 40px;
                        text-align: center;

                        color: white;
                        font-weight: bold;
                        line-height: 120px;
                    }
                    .head-box2{
                        width: 100px;
                        height: 100px;
                        border: 2px solid white;
                        background: url("./images/af0657db2af61de1d2a1c1da0108282.jpg");
                        background-size: 100%;
                    }
                    .label{
                        width: 704px;
                        height: 52px;
                        background: aquamarine;
                        margin-top: 20px;
                        line-height: 50px;
                        text-align: center;
                        font-size: 20px;
                        cursor: pointer;

                    }
                    .label1{
                        float: left;
                        width: 140px;
                        position: relative;
                        display: inline-block;
                    }
                    .label2{
                        float: left;
                        width: 140px;
                        position: relative;
                        display: inline-block;
                    }
                    .label3{
                        float: left;
                        width: 140px;
                        position: relative;
                        display: inline-block;
                    }
                    .label4{
                        float: left;
                        width: 140px;
                        position: relative;
                        display: inline-block;
                    }
                    .label5{
                        float: left;
                        width: 140px;
                        position: relative;
                        display: inline-block;
                    }
                    .box-left{
                        height: 350px;
                        /*background: black;*/
                    }
                    .box-left1{
                        width: 302px;
                        height: 350px;
                        float: left;
                    }
                    .box-left2{
                        width: 700px;
                        height: 350px;
                        float: left;
                        /*text-align: center;*/
                        text-indent: 48px;
                    }
                    p{
                        font-size: 30px;
                    }
                    .box-left2 p{
                        display: none;
                    }
                    .box-left2 h1  {
                        display: none;
                    }
                    .box-left2 h2{
                        display: none;
                    }
                    .box-left2:hover p {
                        display: block;

                    }
                    .box-left2:hover h1{
                        display: block;
                        text-align: center;
                        color: red;
                    }
                    .box-left2:hover h2{
                        display: block;
                        text-align: right;
                        padding-right: 20px;
                    }
                    .box-left3{
                        width: 302px;
                        height: 350px;
                        float: left;
                    }
                    .footer{
                        height: 120px;
                        background: #ffffff;
                        color: #000000;
                        font-size: 30px;
                        font-weight: bold ;

                    }
                    .footer a{
                        box-shadow: 10px 10px 20px 10px #cccccc;
                    }
                    .footer span{
                        box-shadow: 10px 10px 20px 10px #cccccc;
                    }
                </style>
            </head>
            <body>
                <div class="header">
                    <div class="head-box1">
                        <h1>陈鹏的个人主页</h1>
                        <div class="head-box2"></div>
                    </div>
                    <div class="label">
                        <a href="#" class="label1">个人信息</a>
                        <a href="#" class="label2">成长经历</a>
                        <a href="#" class="label3">兴趣爱好</a>
                        <a href="#" class="label4">专业特长</a>
                        <a href="#" class="label5">其他</a>
                    </div>
                    <div class="box-left">
                        <div class="box-left1"></div>
                        <div class="box-left2">
                            <h1>定风波·三月七日</h1>
                            <h2>--苏轼</h2>
                            <p>莫听穿林打叶声，何妨吟啸且徐行。竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。</p>
                            <br>
                            <p> 料峭春风吹酒醒，微冷，山头斜照却相迎。回首向来萧瑟处，归去，也无风雨也无晴。</p>
                        </div>
                        <div class="box-left3"></div>
                    </div>
                    <div class="footer">
                        <span>QQ:113487698 微信:13834319675 联系方式:13834319675</span> <br>
                        <a href="https://github.com/" target="_blank">我的github地址</a>
                        <a href="https://www.csdn.net/" target="_blank">我的csdn地址</a>
                        <a href="https://www.cnblogs.com/" target="_blank">我的博客</a>

                    </div>
                </div>

            </body>
            </html>
                """
msg = MIMEText(mail_content,"html","utf-8")
from_addr = "chenpeng9750@foxmail.com"
from_pwd = "umndufctjbnkjfcg"
to_addr = input("TO:")
smtp_srv = "smtp.qq.com"

header_from = Header("从陈鹏邮箱用代码发出去的邮件<chenpeng9750@foxmail.com>","utf-8")
msg["From"] = header_from
header_to = Header(to_addr,"utf-8")
msg["To"] = header_to
header_sub = Header(input("邮件的主题:"))
msg["Subject"] = header_sub

try:
    srv = smtplib.SMTP(smtp_srv.encode(),25)
    srv.starttls()# 创建安全链接
    srv.set_debuglevel(1)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)





