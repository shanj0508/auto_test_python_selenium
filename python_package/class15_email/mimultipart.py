# 发送附件

import smtplib
# 发送附件的包  MIMEMultipart
from email.mime.multipart import MIMEMultipart
# 发送正文
from email.mime.text import MIMEText
# 头部
from email.header import Header

con = smtplib.SMTP_SSL('smtp.qq.com', '465')
con.login('605284854@qq.com', 'iajmhnstgkezbbji')

# 3.设置发件人账号
sender = '605284854@qq.com'
# 4.设置接收人账号列表
recevier = ['605284854@qq.com']
# 5.设置抄送人列表
Cc = ['605284854@qq.com']

# 发送附件
# 创建一个信封
message = MIMEMultipart()
# 先找到这个html文件(测试报告)
content = open('file/1.html', 'rb').read()
# 写信
file1 = MIMEText(content, 'base64', 'utf-8')
# 信封取个名字 附件名  有个html文件发送
file1['Content-Disposition'] = 'attachment;filename="a.html"'
# 把信放在信封中
message.attach(file1)

# 设置标题:
message['Subject'] = Header('邮件标题')
# 设置发件人
message['From'] = Header('发件人')
# 设置收件人
message['To'] = Header('收件人')
# 设置抄送人
message['Cc'] = ','.join(Cc)  # 分号也行

# 发送邮件
con.sendmail(sender, recevier, message.as_string())


# 直接发送html附件后，html中的超链接都无法点击了，原因是QQ邮箱不支持JS
# 解决方法1：
# 先压缩文件，将文件打包成zip包 把zip包以附件的形式发送给负责人  负责人在去下载，解压再看
# 解决方法2：
# 使用pytest+allure测试报告，可以直接通过界面链接，点击链接 在登录就可以看到了
