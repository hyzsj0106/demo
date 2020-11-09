from package.view import View
from package.operation import Operation
import time
class Main():
    def run():
        View.login()
        obj=Operation()
        while True:
            choise=input('请输入要选择的选项:').strip()
            if choise == '1':       #注册
                obj.register()
            elif choise == '2':     #查询
                obj.query()
            elif choise == '3':     #存钱
                obj.save_money()
            elif choise == '4':     #取钱
                obj.get_money()
            elif choise == '5':     #转账
                obj.trans_money()
            elif choise == '6':     #改密
                obj.change_pwd()
            elif choise == '7':     #锁卡
                obj.lock()
            elif choise == '8':     #解卡
                obj.ublock()
            elif choise == '9':     #补卡
                obj.new_card()
            elif choise == '0':     #退出
                obj.save()
                exit()
            else:
                View.menu()
Main.run()