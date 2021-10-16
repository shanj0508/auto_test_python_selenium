# 发送html文件

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 1.创建邮箱服务器
# 语法：smtplib.SMTP_SSL(邮箱链接地址,端口号) 其中：邮箱链接地址 smtp.xx.com  端口号：自己查 QQ邮箱是465或587
con = smtplib.SMTP_SSL("smtp.qq.com", "465")
# 2.登录邮箱  用户名+密码
con.login('605284854@qq.com', 'iajmhnstgkezbbji')
print(con)  # <smtplib.SMTP_SSL object at 0x000002293A1EE0A0> 表示连接成功
# 3.设置发件人账号
sender = '605284854@qq.com'
# 4.设置接收人账号列表
recevier = ['605284854@qq.com']
# 5.设置抄送人列表
Cc = ['605284854@qq.com']
# html的文件内容
htmlconnext = '''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Unit Test Report</title>
    <meta name="generator" content="HTMLTestRunner 0.8.2"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>

<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         { }

/* -- heading ---------------------------------------------------------------------- */
h1 {
	font-size: 16pt;
	color: gray;
}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}

/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}

a.popup_link:hover {
    color: red;
}

.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 500px;
}

}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
}
#result_table {
    width: 80%;
    border-collapse: collapse;
    border: 1px solid #777;
}
#header_row {
    font-weight: bold;
    color: white;
    background-color: #777;
}
#result_table td {
    border: 1px solid #777;
    padding: 2px;
}
#total_row  { font-weight: bold; }
.passClass  { background-color: #6c6; }
.failClass  { background-color: #c60; }
.errorClass { background-color: #c00; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }


/* -- ending ---------------------------------------------------------------------- */
#ending {
}

</style>

</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

<div class='heading'>
<h1>Unit Test Report</h1>
<p class='attribute'><strong>Start Time:</strong> 2020-11-16 21:15:18</p>
<p class='attribute'><strong>Duration:</strong> 0:00:36.322919</p>
<p class='attribute'><strong>Status:</strong> Pass 2</p>

<p class='description'></p>
</div>



<p id='show_detail_line'>Show
<a href='javascript:showCase(0)'>Summary</a>
<a href='javascript:showCase(1)'>Failed</a>
<a href='javascript:showCase(2)'>All</a>
</p>
<table id='result_table'>
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row'>
    <td>Test Group/Test case</td>
    <td>Count</td>
    <td>Pass</td>
    <td>Fail</td>
    <td>Error</td>
    <td>View</td>
</tr>

<tr class='passClass'>
    <td>loginTest.TestCases</td>
    <td>2</td>
    <td>2</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c1',2)">Detail</a></td>
</tr>

<tr id='pt1.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_01</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_02</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='total_row'>
    <td>Total</td>
    <td>2</td>
    <td>2</td>
    <td>0</td>
    <td>0</td>
    <td>&nbsp;</td>
</tr>
</table>

<div id='ending'>&nbsp;</div>

</body>
</html>
'''

# 6.设置邮件内容（包括头部信息和正文内容）
# 6.1 发送邮件正文：text和html类型邮件都需要用到MIMEText库，引入语法：from email.mime.text import MIMEText
# _text：邮件内容(text或html);   _subtype：文本内容，默认是plain;
message = MIMEText(_text=htmlconnext, _subtype='html', _charset='utf-8')
# 6.2 设置头部信息（邮件标题、发件人和收件人）：需要用到Header库， 引入语法：from email.header import Header
# 设置标题:message['Subject']  固定写法
message['Subject'] = Header('邮件标题')
# 设置发件人
message['From'] = Header('发件人')
# 设置收件人
message['To'] = Header('收件人')
# 设置抄送人
message['Cc'] = ','.join(Cc)  # 分号也行
# 分号也行: message['Cc'] = ';'.join(Cc)

# 7.发送邮件：邮局con发送
try:
    con.sendmail(sender, recevier + Cc, message.as_string())
    print('邮件发送成功')
except Exception:
    print('邮件发送失败')
