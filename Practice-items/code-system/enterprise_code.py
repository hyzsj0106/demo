# www.cxywy.com
# 程序员未雨
import time, random
import os
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from pystrich.ean13 import EAN13Encoder
import qrcode

root = tk.Tk()

randlist = [] # 用于存储防伪码的变量
rangstr = '' # 用于保存单个防伪码
number = "1234567890"
letter = "ABCDEFGHIJKLMNPQRSTUVWXYZ1234567890"

def menu():
    print('''
    ****************************************************************
                            企业编码生成系统
    ****************************************************************
        1.生成6位数字防伪编码 （213563型）
        2.生成9位系列产品数字防伪编码(879-335439型)
        3.生成25位混合产品序列号(B2R12-N7TE8-9IET2-FE35O-DW2K4型)
        4.生成含数据分析功能的防伪编码(5A61M0583D2)
        5.智能批量生成带数据分析功能的防伪码
        6.后续补加生成防伪码(5A61M0583D2)
        7.EAN-13条形码批量生成
        8.二维码批量输出
        9.企业粉丝防伪码抽奖
        0.退出系统
    ================================================================
    说明：通过数字键选择菜单
    ================================================================
    ''')
    user_option()


def user_option():
    while True:
        user_option = input('请输入您要操作的菜单选项:').strip()
        if not user_option.isdigit() or len(user_option) > 1:
            print("您的输入有误,请重新输入")
            continue
        if user_option == '1':
            code1_func()
        elif user_option == '2':
            code2_func()
        elif user_option == '3':
            code3_func()
        elif user_option == '4':
            code4_func(user_option)
        elif user_option == '5':
            code5_func(user_option)
        elif user_option == '6':
            code6_func()
        elif user_option == '7':
            code7_func()
        elif user_option == '8':
            code8_func()
        elif user_option == '9':
            code9_func()
        elif user_option == '0':
            print("正在退出系统!!")
            time.sleep(2)
            quit()

# 检测本地对应文件夹是否存在
def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

# 读取之前生成的防伪码
def openfile(filename):
    f = open(filename)
    fstr = f.read()
    f.close()
    return fstr

# input判断函数
def inputbox(showstr,mode,length):
    if showstr != '' and mode != '':
        # 如果为0 此条限制仅数字
        if mode == '0':
            num1 = input(showstr).strip()
            if num1.isdigit():
                if length == 0 and int(num1) > 0:
                    return int(num1)
                elif len(num1) == length:
                    return int(num1)
                else:
                    print('您的输入有误,请重新输入!90')
                    return '0'
            else:
                print('您的输入有误,请重新输入!93')
                return '0'
        # 此条限制为字母
        elif mode == '1':
            abc = input(showstr).strip().upper()
            if abc.encode('utf-8').isalpha():
                if length == 0 and len(abc) > 0:
                    return abc
                elif len(abc) == length:
                    return abc
                else:
                    print('您的输入有误,请重新输入!104')
                    return '0'
            else:
                print('您的输入有误,请重新输入!107')
                return '0'
        else:
            print('您的输入有误,请重新输入!110')
            return '0'
    else:
        print('您的输入有误,请重新输入!113')
        return '0'


def show_save_file(lis, path, file_name, msg, typies):
    mkdir(path) # 确保路径文件夹存在
    datafile = path + '\\' + file_name  # 拼接文件路径
    f = open(datafile, 'w')
    pingmu_data = ''    # 清空变量,防止上次残留
    for i in range(len(lis)):
        write_data = lis[i]
        f.write(str(write_data))
        pingmu_data = pingmu_data + write_data
    f.close()
    print(pingmu_data)
    # 根据传进来的参数判断是否弹窗显示
    if typies != 'no':
        tk.messagebox.showinfo('提示:', msg + str(len(randlist)) + '\n防伪码文件存放位置:'+datafile)
        root.withdraw()

# 生成6位数字防伪编码
def code1_func():
    str1 = '请输入要生成防伪码的数量:'
    code_num = inputbox(str1, '0', 0)
    while code_num == '0':
        code_num = inputbox(str1, '0', 0)
    randlist.clear()    # 清空保存防伪码的变量
    for i in range(int(code_num)):
        randstr = ''
        for j in range(6):  # 循环生成单条注册码
            randstr = randstr + random.choice(number)
        randstr = randstr + '\n'
        randlist.append(randstr)    # 保存到列表里
    msg = '已生成6位防伪码共计:'
    # 调用函数show_save_file
    show_save_file(randlist, 'codepath', 'code1'+'.txt', msg, '')

# 生成9位系列产品数字防伪编码
def code2_func():
    str1 = '请输入系列产品的数字起始号(3位):'
    str2 = '请输入产品系列的数量:'
    str3 = '请输入要生成的每个系列产品的防伪码数量:'
    qishi_id = inputbox(str1, '0', 3)
    while qishi_id == '0':
        qishi_id = inputbox(str1, '0', 3)
    xilie_num = inputbox(str2, '0', 0)
    while xilie_num == '0':
        xilie_num = inputbox(str2, '0', 0)
    code_num = inputbox(str3, '0', 0)
    while code_num == '0':
        code_num = inputbox(str3, '0', 0)
    randlist.clear()    # 清空保存防伪码的变量
    for k in range(int(xilie_num)):
        now_id = int(qishi_id) + k
        for i in range(int(code_num)): # 防伪码总数量
            randstr = ''    
            for j in range(6):  # 循环生成单条注册码
                randstr = randstr + random.choice(number)
            randstr = str(now_id) + randstr + '\n'
            randlist.append(randstr)    # 保存到列表里
    msg = '已生成9位防伪码共计:'
    # 调用函数show_save_file
    show_save_file(randlist, 'codepath', 'code2'+'.txt', msg, '')
    
# 生成25位混合产品序列号
def code3_func():
    str1 = '请输入要生成的25位混合产品序列号数量:'
    serial_num = inputbox(str1, '0', 0)
    while serial_num == '0':
        serial_num = inputbox(str1, '0', 0)
    randlist.clear()    # 清空保存防伪码的变量
    for i in range(int(serial_num)):  # 防伪码总数量
        randstr = ''
        for j in range(1, 30):  # 循环生成单条注册码
            if j % 6 == 0:
                randstr = randstr + '-'
            randstr = randstr + random.choice(letter)
        randstr = randstr + '\n'
        randlist.append(randstr)    # 保存到列表里
    msg = '已生成25位混合产品序列号共计:'
    # 调用函数show_save_file
    show_save_file(randlist, 'codepath', 'code3' + '.txt', msg, '')

# 生成含数据分析功能的防伪编码
def code4_func(user_option):
    str1 = '请输入要生成的带数据分析功能的验证码数量:'
    str2 = '请输入数据分析编号(3位字母)'
    shuliang_num = inputbox(str1, '0', 0)
    while shuliang_num == '0':
        shuliang_num = inputbox(str1, '0', 0)
    abc_num = inputbox(str2, '1', 3)
    while abc_num == '0':
        abc_num = inputbox(str2, '1', 3)
    code_func(shuliang_num, abc_num, user_option)

# 生成数据分析防伪编码
def code_func(shuliang_num, abc_num, user_option):
    randlist.clear()    # 清空保存防伪码的变量
    abc_list = list(abc_num)
    # 生成防伪码
    for i in range(int(shuliang_num)): # 防伪码总数量
        randstr = ''
        for j in range(9):  # 循环生成单条注册码
            randstr = randstr + random.choice(number)
        # 为了取出3个随机位置
        index_lis = random.sample(number, 3)
        index_lis.sort()
        for k in range(3):
            index = int(index_lis[k])
            randstr = randstr[0:index] + abc_list[k] + randstr[index:]
        randstr = randstr + '\n'
        randlist.append(randstr)    # 保存到列表里
    msg = '已生成含数据分析功能的防伪编码:'
    typies = ''
    if user_option == '5':
        typies = 'no'
    # 调用函数show_save_file
    show_save_file(randlist, 'codepath', abc_num + 'code'+ user_option + '.txt', msg, typies)


# 智能批量生成带数据分析功能的防伪码
def code5_func(user_option):
    default_dir = r"wysoft.wy"  # 设置默认打开的文件名称
    # 打开文件选择对话框，指定打开的文件名称为"wysoft.wy" ，扩展名为“wy”，可以使用记事本打开和编辑
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text file", "*.wy")],
                                                   title=u"请选择自动防伪码智能批处理文件：",
                                                   initialdir=(os.path.expanduser(default_dir)))
    if os.path.exists(file_path):
        read_file = openfile(file_path)     # 返回str
        file_list = read_file.split('\n')
        for s_str in file_list:
            abc_num = s_str.split(',')[0].upper()
            shuliang_num = s_str.split(',')[1]
            code_func(shuliang_num, abc_num , user_option)
    else:
        print('打开失败,请查证是否存在文件')
        time.sleep(2)

# 6后续补加生成防伪码
def code6_func():
    default_dir = r"ASDcode5.txt"  # 设置默认打开的文件名称
    # 打开文件选择对话框
    file_path = tkinter.filedialog.askopenfilename(title=u"请选择已经生成的防伪码文件:",
                                                   initialdir=(os.path.expanduser(default_dir)))
    if os.path.exists(file_path):
        read_file = openfile(file_path)  # 返回str
        old_code_list = read_file.split('\n')
        old_code_list.remove('')
        old_count = len(old_code_list)
        print(old_count)
        tkinter.messagebox.showinfo('提示:','之前的防伪码' + '\n总计:{}'.format(old_count))
        root.withdraw()
        abc_list = list(old_code_list[0])
        abc_str = ''
        for i in abc_list:
            if not i.isdigit():
                abc_str += i
        str1 = '请输入补充防伪码生成的数量'
        shuliang_num = inputbox(str1, '0', 0)
        while shuliang_num == '0':
            shuliang_num = inputbox(str1, '0', 0)
        randlist.clear()    # 清空保存防伪码的变量
        new_list = []
        randlist.extend(old_code_list)  # 将去掉'\n'的旧列表添加进新列表
        abc_list = list(abc_str)    # 将字母打散成列表
        # 生成防伪码
        set1 = {}
        while len(set1) != old_count + shuliang_num:
            randstr = ''
            for j in range(9):  # 循环生成单条注册码
                randstr = randstr + random.choice(number)
            # 为了取出3个随机位置
            index_lis = random.sample(number, 3)
            index_lis.sort()
            for k in range(3):
                index = int(index_lis[k])
                randstr = randstr[0:index] + abc_list[k] + randstr[index:]
            randlist.append(randstr)    # 保存到列表里
            set1 = set(randlist)    # 集合去重
        for k in range(old_count):
            set1.remove(old_code_list.pop())
        for a in list(set1):
            a = a + '\n'
            new_list.append(a)
        msg = '增加生成含数据分析功能的防伪编码成功,共计:'
        typies = ''
        # 调用函数show_save_file
        show_save_file(new_list, 'addpath', abc_str + 'code6' + '.txt', msg, typies)
    else:
        print('打开失败,请查证是否存在文件')
        time.sleep(2)

# EAN-13条形码批量生成
def code7_func():
    mkdir('barcode')
    str1 = '请输入EAN13的国家代码（3位）'
    country_num = inputbox(str1, '0', 3)
    while country_num == '0':
        country_num = inputbox(str1, '0', 3)
    str2 = '请输入EAN13的企业代码（4位）'
    en_num = inputbox(str2, '0', 4)
    while en_num == '0':
        en_num = inputbox(str2, '0', 4)
    str3 = '请输入要生成的条形码数量'
    shuliang_num = inputbox(str3, '0', 0)
    while shuliang_num == '0':
        shuliang_num = inputbox(str3, '0', 0)
    # 有了7位,还差5位随机码和1位校验码
    for i in range(shuliang_num):
        ran_list = random.choices(list(number), k=5)
        ran_num = str(ran_list[0]) + str(ran_list[1]) + str(ran_list[2]) + str(ran_list[3]) +str(ran_list[4])
        barcode = str(country_num) + str(en_num) + ran_num
        # 计算条形码的校验位
        evensum = int(barcode[1]) + int(barcode[3]) + int(barcode[5]) + int(barcode[7]) + int(barcode[9]) + \
                  int(barcode[11])  # 偶数位
        oddsum = int(barcode[0]) + int(barcode[2]) + int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + \
                 int(barcode[10])
        # checkbit=int(10-(evensum *3 + oddsum)%10)
        checkbit = int((10 - (evensum * 3 + oddsum) % 10) % 10)
        barcode = barcode + str(checkbit)  # 组成完整的EAN13条形码的13位数字
        # 调用打印
        encoder = EAN13Encoder(barcode)  # 调用EAN13Encoder生成条形码
        encoder.save("barcode\\" + barcode + ".png")  # 保存条形码信息图片到文件

# 二维码批量输出,暂无合适的例子
def code8_func():
    mkdir('qrcode')
    str1 = '请输入要生成的条形码数量'
    shuliang_num = inputbox(str1, '0', 0)
    while shuliang_num == '0':
        shuliang_num = inputbox(str1, '0', 0)
    for i in range(shuliang_num):
        qr_list = random.choices(number, k=3)
        qr_str = str(qr_list[0]) + str(qr_list[1]) + str(qr_list[2])
        encoder = qrcode.make(qr_str)
        encoder.save('qrcode\\' + qr_str + '.png')
    print('保存成功...')

# 企业粉丝防伪码抽奖
def code9_func():
    default_dir = r"ASDcode5.txt"  # 设置默认打开的文件名称
    # 打开文件选择对话框
    file_path = tkinter.filedialog.askopenfilename(title=u"请选择包含抽奖号码的抽奖文件：",
                                                   initialdir=(os.path.expanduser(default_dir)))
    if os.path.exists(file_path):
        read_file = openfile(file_path)  # 返回str
        code_list = read_file.split('\n')
        code_list.remove('')
        str1 = '请输入要生成的抽奖数量:'
        shuliang_num = inputbox(str1, '0', 0)
        while shuliang_num == '0':
            shuliang_num = inputbox(str1, '0', 0)
        # 抽取n个
        win_list = random.sample(code_list, shuliang_num)
        print('抽奖信息名单发布：')
        str_all = ''
        for i in win_list:
            str_all += i+'\n'
        print(str_all)
    else:
        print('打开失败,请查证是否存在文件')
        time.sleep(2)

if __name__ == '__main__':
    menu()
