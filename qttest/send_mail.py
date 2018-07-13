import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
class Mail:
    def __init__(self, receiver):
        self.my_sender = '985897924@qq.com'  # 发件人邮箱账号
        self.my_passwd = 'hslwszxtkhmybaif'  # 发件人邮箱密码
        self.my_receiver = receiver  # 收件人邮箱账号

    def send_text(self, text):
        try:
            msg = MIMEText(text, 'plain', 'utf-8')
            msg['From'] = formataddr(["andy", self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["myself", self.my_receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "验证信息"  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [self.my_receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            print('发送成功 ')
            self.flag = 1
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print('发送失败')
            self.flag = 0

    def get_ok(self):
        return self.flag


