from send_mail import Mail
from 生成验证码 import Random
import _thread
if __name__ == '__main__':

    mail = Mail('985897924@qq.com')
    ans = Random().Random(10)
    try:
        _thread.start_new_thread(mail.send_text, (ans,1))
        _thread.start_new_thread(mail.send_text, (ans,2))
        # mail.send_text(ans)
    except:
        print("false")
    while 1:
        pass