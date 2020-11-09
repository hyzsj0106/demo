# view 视图界面
# 登陆（管理员账号登陆）,欢迎界面，操作界面
import time
class View():

    def login():
        while True:
            admin_name = input('请输入管理员账号:').strip()
            if ' ' in admin_name:
                print('用户名非法!')
                continue
            else:
                admin_pwd = input('请输入管理员密码:').strip()
                if admin_name== 'admin' and admin_pwd == '123':
                    print('**************************************************')
                    print('*                                                *')
                    print('*              Welcome To WY Bank                *')
                    print('*                                                *')
                    print('**************************************************')
                    time.sleep(1)
                    View.menu()
                    return
                else:
                    print('输入的账号或密码错误!')

    def menu():
        print('**************************************************')
        print('*       (1)注册                    (2)查询        *')
        print('*       (3)存钱                    (4)取钱        *')
        print('*       (5)转账                    (6)改密        *')
        print('*       (7)锁卡                    (8)解卡        *')
        print('*       (9)补卡                    (0)退出        *')
        print('*                 其他返回主菜单                   *')
        print('**************************************************')


