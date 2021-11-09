# 发送附件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def send_report():
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
    content = open('../report/report.html', 'rb').read()
    # 写信
    file1 = MIMEText(content, 'base64', 'utf-8')
    # 信封取个名字 附件名  有个html文件发送
    file1['Content-Disposition'] = 'attachment;filename="report.html"'
    # 把信放在信封中
    message.attach(file1)

    # 设置标题:
    message['Subject'] = Header('XX系统冒烟测试结果')
    # 设置发件人
    message['From'] = Header('发件人')
    # 设置收件人
    message['To'] = Header('收件人')
    # 设置抄送人
    message['Cc'] = ','.join(Cc)  # 分号也行

    # 发送邮件
    con.sendmail(sender, recevier, message.as_string())