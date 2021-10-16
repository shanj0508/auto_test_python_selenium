# 发送图片

import smtplib
# 附件
from email.mime.multipart import MIMEMultipart
# 图片
from email.mime.image import MIMEImage
# 头部
from email.header import Header
# 正文
from email.mime.text import MIMEText

con = smtplib.SMTP_SSL('smtp.qq.com', '465')
con.login('605284854@qq.com', 'iajmhnstgkezbbji')

sender = '605284854@qq.com'
recevier = ['605284854@qq.com']
Cc = ['605284854@qq.com']

# 创建实例  信封
message = MIMEMultipart()

# 把图片拿出来  路径
image1 = open('file/3.jpeg', 'rb').read()
# 把图片附件中
image_da = MIMEImage(image1)
# 图片设置名字
image_da['Content-Disposition'] = 'attachment;filename="qq.jpeg"'
# 把附件放到邮件对象中去
message.attach(image_da)

content = '''
邮件内容XXXX
'''
cc = MIMEText(content, 'plain', 'utf-8')
message.attach(cc)

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
