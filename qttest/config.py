import pymysql

class config:
    def __init__(self, Widget):
        self.Widget = Widget

    def hideWindows(self, power, name):
        print(name + ' 登陆成功')
        self.Widget.name = name
        self.Widget.power = power
        if power == 1:
            self.Widget.page.hide()
            self.Widget.toolBox.removeItem(0)
            print('中介')
            name += ' 中介'
        elif power == 0:
            self.Widget.page_3.hide()
            self.Widget.toolBox.removeItem(2)
            print('顾客')
            name += ' 顾客'
        else:
            print('管理员')
            name += ' 管理员'
        self.Widget.label_6.setText(name)

