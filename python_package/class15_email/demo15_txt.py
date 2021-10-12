# 邮件
'''
1.用python代码发送文本邮件
2.用python代码发送html邮件
3.发送附件和图片
'''
# smtplib库：对smtp进行封装，可以用来发送电子邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 1.创建邮箱服务器，类似邮局，需要用到smtplib库，引入语法：import smtplib
# SMTP_SSL比SMTP更安全
# 语法：smtplib.SMTP_SSL(邮箱链接地址,端口号) 其中：邮箱链接地址 smtp.xx.com  端口号：自己查 QQ邮箱是465或587
con = smtplib.SMTP_SSL("smtp.qq.com", "465")
# 2.登录邮箱  用户名+密码
# 163邮箱可以直接填用户名和密码进行登录，QQ邮箱需要设置一下（登录qq邮箱--设置--账户--POP3/SMTP服务看开启--获得授权码），用户名是邮箱名，密码是授权密码（iajmhnstgkezbbji）
con.login('605284854@qq.com', 'iajmhnstgkezbbji')
print(con)  # <smtplib.SMTP_SSL object at 0x000002293A1EE0A0> 表示连接成功
# 3.设置发件人账号
sender = '605284854@qq.com'
# 4.设置接收人账号列表
recevier = ['605284854@qq.com', '823036978@qq.com']
# 设置抄送人列表
Cc = ['605284854@qq.com', '605284854@qq.com']

# 5.设置邮件内容（包括头部信息和正文内容）
# 5.1 发送邮件正文：需要用到MIMEText库，引入语法：from email.mime.text import MIMEText
# _text：邮件内容;   _subtype：文本内容，默认是plain;
message = MIMEText(_text='老公我爱你呀~么么哒~早点回家~宝宝想你~！', _subtype='plain', _charset='utf-8')

# 5.2 设置头部信息（邮件标题、发件人和收件人）：需要用到Header库， 引入语法：from email.header import Header
# 设置标题:message['Subject']  固定写法
message['Subject'] = Header('你的小可爱粗线啦~~')
# 设置发件人
message['From'] = Header('小可爱')
# 设置收件人
message['To'] = Header('大可爱')
# 设置抄送人
message['Cc'] = ','.join(Cc)  # 分号也行
# 分号也行: message['Cc'] = ';'.join(Cc)  

# 6.发送邮件：邮局con发送
try:
    con.sendmail(sender, recevier + Cc, message.as_string())
    print('邮件发送成功')
except Exception:
    print('邮件发送失败')
