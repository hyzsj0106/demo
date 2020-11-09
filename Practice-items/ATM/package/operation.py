#operation类（具体的操作功能实现）
# 把我们需要的十个功能都放在这个类里
from .card import Card
from .person import Person
from .view import View
import os,pickle,random,time
class Operation():
    #初始化加载用户信息
    def __init__(self):
        self.load_user()
        self.load_user_id()
    #读取用户信息     卡号：用户
    def load_user(self):
        if os.path.exists('user.txt'):
            with open('user.txt','rb') as f:
                self.user_dict=pickle.load(f)
        else:
            self.user_dict={}

    #读身份id卡信息   身份证：卡号
    def load_user_id(self):
        if os.path.exists('userid.txt'):
            with open('userid.txt','rb') as f:
                self.user_id_dict=pickle.load(f)
        else:
            self.user_id_dict={}

    # 获取银行卡号
    def get_card_id(self):
        while True:
            id_card = str(random.randint(100000, 999999))
            if id_card not in self.user_dict:
                return id_card
    # 获取密码
    def get_pwd(self):
        while True:
            pwd1 = input('请输入密码:').strip()
            pwd2 = input('请确认密码:').strip()
            if pwd1 == pwd2 and pwd2!='':
                return pwd2
            else:
                print('您的输入不合法!,请查证!')
    # 获取身份证id
    def userid(self):
        while True:
            print('尊敬的用户:')
            time.sleep(1)
            print('\t您好,为了提升服务效率,ATM机仅支持一人一卡! 感谢您的理解!')
            print('如需办理多卡,请咨询银行前台,谢谢您的支持!😙')

            userid = input('请输入您的身份证号(6位):').strip()
            if len(userid) < 6 or len(userid) > 6:
                print('输入位数不对哟!温馨提示:需要6位哟~')
                continue
            elif userid[-1] == 'X' and userid.count('X')==1:
                return userid
            elif len(userid) == 6 and userid.isdigit() == True:
                return userid
            else:
                print('您输入的有误,请查证后再次输入!')
                print('温馨提醒:如末位是X,请大写X!')
                continue

    # 获取手机号
    def phone(self):
        print('********温馨提示:输入界面按1回车返回主目录********')
        while True:
            phone = input('输入您的手机号(5位纯数字):').strip()
            if len(phone) < 5 or len(phone) > 5:
                print('位数不对!需要5位')
                continue
            elif phone.isdigit() == False:
                print('必须为5位纯数字')
                continue
            else:
                return phone
    # 注册
    def register(self):
        while True:
            print('*********************注册账号*********************')
            time.sleep(0.2)
            print('**************支持中/英文,不支持空格**************')
            name=input('请输入注册用户名:').strip()
            if ' 'in name or name.isspace():
                print('温馨提示:用户名不合法!请查证后再次输入!')
                continue
            else:
                user_id=self.userid()
                phone=self.phone()
                pwd=self.get_pwd()
                money=10
                card_id=self.get_card_id()
                card = Card(card_id,pwd,money)
                person = Person(name,user_id,phone,card)
                self.user_dict[card_id]=person
                self.user_id_dict[user_id] = card_id
                print('尊敬的:{},您已开户成功,卡号为:{},余额为{:,}元'.format(name,card_id,money))
                return
    # 查询
    def query(self):
        print('*********************开始查询*********************')
        time.sleep(0.2)
        #返回卡对象
        ex_card = self.get_card_info()
        if ex_card:
            if ex_card.islock:
                print('您的卡状态: 冻结!')
            else:
                if self.check_pwd(ex_card):
                    print('余额为:{:,}'.format(ex_card.money))

    #检测密码
    def check_pwd(self,card):
        count = 3
        while count>0:
            pwd = input('请输入您的密码:').strip()
            if pwd == card.password:
                return True
            else:
                count -= 1
                print('密码错误,你还有{}次机会'.format(count))
        print('您的卡状态调整为: 冻结!')
        card.islock=True

    #卡是否存在
    def get_card_info(self):
        count = 2
        while True:
            input1 = input('请输入卡号: ')
            if input1 in self.user_dict:
                user = self.user_dict[input1]
                card = user.card
                return card
            else:
                count -= 1
                print('您输入的卡号不存在! 还有{}次机会'.format(count))
                if count==0:
                    break

    def save_money(self):   #存钱
        print('*********************存钱操作*********************')
        time.sleep(0.2)
        card=self.get_card_info()
        if card:
            if card.islock:
                print('您的卡状态: 冻结!')
            elif card.islock==False:
                print('用户名为:',self.user_dict[card.cardid].name)
                caozuo=input('按1存款,其他返回上一层:')
                if caozuo=='1':
                    cun_cash=input('输入要存款的金额:').strip()
                    if cun_cash.isdigit():
                        card.money += int(cun_cash)
                        print('存入成功,您的账户余额为:{:,}元'.format(card.money))
                    else:
                        print('输入不合法!')

    # 取钱
    def get_money(self):
        print('*********************取出现金*********************')
        time.sleep(0.2)
        card = self.get_card_info()
        if card:
            if card.islock==True:
                print('您的卡状态: 冻结! 请解锁后使用!')
            else:
                if self.check_pwd(card):
                    print('用户名为:', self.user_dict[card.cardid].name)
                    qu_cash = input('输入要取款的金额:').strip()
                    if qu_cash.isdigit()==True and card.money - int(qu_cash)>=0 :
                        card.money -= int(qu_cash)
                        print('取出{}成功,您的账户余额为:{:,}元'.format(qu_cash,card.money))
                    else:
                        print('输入不合法!或可取余额不足!')
                else:
                    return

    # 转账
    def trans_money(self):
        print('*********************进行转账*********************')
        time.sleep(0.2)
        print('**************确认对方身份,谨防上当受骗*************')
        card = self.get_card_info()
        if card:
            if card.islock:
                print('您的卡状态: 冻结! 请解锁后使用!')
            else:
                if self.check_pwd(card):
                    print('当前转出账户为:', self.user_dict[card.cardid].name, '请在下方输入收账卡号(☄⊙ω⊙)☄')
                    # 验证对方账号
                    card1 = self.get_card_info()
                    if card1.islock:
                        print('对方的卡状态: 冻结!')
                    elif card == card1:
                        print('喜提彩蛋,非法操作!')
                    elif card1.islock==False:
                        print('请核验:对方卡号为 {},注册名 *{}'.format(card1.cardid,self.user_dict[card1.cardid].name[-2:]))
                        trans_cash = input('请输入要转账的金额:').strip()
                        if trans_cash.isdigit() == True and card.money - int(trans_cash) >= 0:
                            #自己钱减少
                            card.money -= int(trans_cash)
                            #对方钱增加
                            card1.money += int(trans_cash)
                            print('转出{:,}元成功,您的账户余额为:{:,}元'.format(int(trans_cash), card.money))
                        else:
                            print('输入不合法!或可取余额不足!')

    #判断新密码是否相等合法
    def check_change_pwd(self,card):
        while True:
            pwd1 = input('请输入修改密码:').strip()
            pwd2 = input('请确认修改密码:').strip()
            if pwd1 == pwd2 and pwd1 != '':
                card.password = pwd2
                print('修改成功,牢记您的密码,请勿交给他人!')
                return pwd2
            else:
                print('您的输入不合法!请查证后再次输入!')

    # 改密
    def change_pwd(self):
        print('*********************改密操作*********************')
        time.sleep(0.2)
            #卡存在
        card = self.get_card_info()
        if card:
            choice = input('1.原密码改密  2.身份证改密')
            if choice=='1':
                if self.check_pwd(card):
                    self.check_change_pwd(card)
            elif choice=='2':
                res = self.userid()
                #根据卡号找身份证号
                if res == self.user_dict[card.cardid].userid:
                    self.check_change_pwd(card)
                else:
                    print('你是假的吧!')
            else:
                print('输入不合法!')

    def lock(self):     #锁卡
        print('*********************紧急锁卡*********************')
        time.sleep(0.1)
        card1 = self.get_card_info()
        if card1:
            if card1.islock==False:
                print('您的卡状态: 未冻结')
                choice=input('1) 使用密码冻结 2) 使用身份证冻结')
                if choice == '1':
                    if self.check_pwd(card1):
                        card1.islock=True
                        print('您的卡冻结成功!')
                        return
                elif choice == '2':
                    res = self.userid()
                    # 根据卡号找身份证号
                    if res == self.user_dict[card1.cardid].userid:
                        card1.islock = True
                        print('您的卡冻结成功!')
                        return
                    else:
                        print('你是假的吧!')
            elif card1.islock==True:
                print('您的卡状态: 冻结')
                return

    def ublock(self):   #解卡
        print('*********************解卡操作*********************')
        time.sleep(0.2)
        card2 = self.get_card_info()
        if card2:
            if card2.islock==False:
                print('您的卡状态: 未冻结')
            elif card2.islock==True:
                print('您的卡状态: 冻结')
                choice = input('1) 使用密码解冻 2) 使用身份证解冻')
                if choice == '1':
                    if self.check_pwd(card2):
                        card2.islock = False
                        print('您的卡解冻成功!')
                        return
                elif choice == '2':
                    res = self.userid()
                    # 根据卡号找身份证号
                    if res == self.user_dict[card2.cardid].userid:
                        card2.islock = False
                        print('您的卡解冻成功!')
                        return
                    else:
                        print('你是假的吧!')

    def new_card(self):     #补卡
        print('*********************操作补卡*********************')
        time.sleep(0.2)
        user_id = self.userid()                     #调用userid检查输入身份证号是否合法
        if user_id in self.user_id_dict:            #根据输入的身份证号去user_id_dict字典里找:
            old_card = self.user_id_dict[user_id]   #根据id键,获取卡号值.
            person1 = self.user_dict[old_card]      #通过银行卡行获取用户对象
            self.user_id_dict.pop(user_id)          # 使用pop函数删除字典中的身份证号键及对应卡号值
            self.user_dict.pop(old_card)
            new_idcard = self.get_card_id()           # 使用get_card_id获取新卡号
            self.user_id_dict[user_id] = new_idcard   # 并把新卡号和原用户对象赋给字典更新：
            self.user_dict[new_idcard]=person1
            print('您的新卡号为:{}'.format(new_idcard))
        else:
            print('没有找到,是不是来错银行了~')

    def save(self):     #保存
        print('*********************保存退出*********************')
        time.sleep(0.2)
        with open('user.txt','wb')as f:
            pickle.dump(self.user_dict,f)
        with open('userid.txt','wb')as f:
            pickle.dump(self.user_id_dict,f)
        print('*************感谢您的使用,请收好您的卡片************')