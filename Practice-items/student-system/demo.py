import re, os
import time
​
file_name = 'students.txt'
​
def menu():
    menu_xunhuan = 1
    while menu_xunhuan:
        print('''
        ************学生信息管理系统*************
​
            ---------   功能菜单   ---------
            1 录入学生信息
            2 查找学生信息
            3 删除学生信息
            4 修改学生信息
            5 排序
            6 统计学生总人数
            7 显示所有学生信息
            0 退出系统
            --------------------------------
            说明：通过数字选择菜单
            
        ****************************************
        ''')
        # 用户指令输入
        user_str = input("请选择:")
        # 抽取用户输入的数字指令
        option = re.sub('\D', "", user_str)
        if option in ['1', '2', '3', '4', '5', '6', '7', '0']:
            option_num = int(option)
            if option_num == 0:
                print("感谢您的使用,再见!")
                time.sleep(1)
                break
            elif option_num == 1:
                # 调用录入函数
                insert_func()
            elif option_num == 2:
                # 调用查找函数
                search_func()
            elif option_num == 3:
                # 调用删除函数
                del_func()
            elif option_num == 4:
                # 调用修改函数
                modify_func()
            elif option_num == 5:
                # 调用排序函数
                sort_func()
            elif option_num == 6:
                # 调用统计函数
                count_func()
            elif option_num == 7:
                # 调用所有显示函数
                show_all_func()
        else:
            print("你的输入有误,按0退出!")
​
​
# 录入函数
def insert_func():
    student_list = []
    mark = True
    while mark:
        id = input('请输入ID(如 1001):')
        if id.isdigit() == False:
            print('输入错误,必须是纯数字,请重新输入!')
            break
        stu_name = input('请输入姓名')
        if stu_name == '':
            print('输入有误,请重新输入!')
            break
        try:
            stu_english = int(input('请输入英语成绩:'))
            stu_python = int(input('请输入Python成绩:'))
            stu_c = int(input('请输入c语言成绩:'))
        except:
            print('输入错误,请重新输入!')
            break
        # 单条学生信息保存字典格式
        stu_dict = {'ID':id,'name':stu_name,'English':stu_english,'Python':stu_python,'C':stu_c}
        student_list.append(stu_dict)
        user_mark = input('是否继续添加信息:y/n:').lower()
        if user_mark == 'y':
            mark = True
        else:
            mark = False
            # 调用保存函数
            save_func(student_list)
            print('保存信息成功!')
​
​
# 存储函数
def save_func(student_list):
    try:
        student_txt = open(file_name, 'a')
    except:
        student_txt = open(file_name, 'w')
    for student in student_list:
        # 换行存储
        student_txt.write(str(student)+'\n')
    # 全部写入之后再关闭
    student_txt.close()
    
​
# 查询函数
def search_func():
    search_list = []
    if os.path.exists(file_name):
        id = ''
        name = ''
        mark = 1
        while mark:
            user_option = input("按ID查询输入1,学生姓名查询输入2:").strip()
            if user_option == '1':
                id = input('请输入你要查询的学生ID:').strip()
                if not id.isdigit():
                    print('输入有误,请重新输入!')
                    break
            elif user_option == '2':
                name = input("请输入你要查询的学习姓名:").strip()
                if name is '':
                    print('输入有误,请重新输入!')
                    break
            else:
                print('您的输入有误,请重新输入!')
                break
            # 打开文件读取所有行到列表里,遍历每行转化为字典.
            with open(file_name, 'r') as f:
                stu_list = f.readlines()
                for stu_info in stu_list:
                    d = dict(eval(stu_info))
                    if id is not '' and d['ID'] == id:
                        search_list.append(d)
                    elif name is not '' and  d['name'] == name:
                        search_list.append(d)
                show_func(search_list)
                search_list.clear()
                mark_state = input('是否继续查询?Y/N:').lower()
                if mark_state != 'y':
                    mark = 0
            
    else:
        print('(o@.@o) 无数据信息 (o@.@o)')
​
​
# 显示查询结果
def show_func(search_list):
    if search_list == False:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    result_title = '{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}'
    print(result_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    result_data = '{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
​
    for info in search_list:
        print(result_data.format(info['ID'],info['name'],info['English'],info['Python'],info['C'],str(info['English']+info['Python']+info['C'])))
​
​
# 删除函数
def del_func():
    # 判断是否有文件存在
    if not os.path.exists(file_name):
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    mark = 1
    while mark:
        new_list = []
        old_list = []
        del_id = input('请输入要删除的学生ID:').strip()
        with open(file_name,'r') as rfile:
            old_list = rfile.readlines()
        # 定义事件找到id为True
        id_del = False
        # 如果old_list不为空
        if old_list:
            for stu_data in old_list:
                d = dict(eval(stu_data))
                if d['ID'] != del_id:
                    new_list.append(d)
                elif d['ID'] == del_id:
                    id_del = True
                    print('ID为{}的学生信息已查到!'.format(del_id))
​
            with open(file_name,'w') as wfile:
                for new_data in new_list:
                    wfile.write(str(new_data)+'\n')
                if id_del:
                    print('ID为{}的学生信息删除成功!'.format(del_id))
                else:
                    print('未找到该ID信息')
            show_func(new_list)
            mark_input = input('是否继续删除?Y/N:').lower().strip()
            if mark_input != 'y':
                mark = 0
        else:
            print('无学生信息')
        
#修改函数
def modify_func():
    new_list = []
    single_lis = []
    if not os.path.exists(file_name):
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    with open(file_name,'r')as rfile:
            old_list = rfile.readlines()
    # 默认是没有这个id
    id_del = False
    if old_list:
        modify_id = input('请输入要修改的ID号:').strip()
        for data in old_list:
            d = dict(eval(data))
            if d['ID'] != modify_id:
                new_list.append(d)
            elif d['ID'] == modify_id:
                id_del = True
                print('找到了这名学生,可以修改他的信息!')
                print('以下是原信息:')
                single_lis.append(d)
                show_func(single_lis)
                mark = 1
                while mark:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['English'] = int(input('请输入English成绩:'))
                        d['Python'] = int(input('请输入Python成绩:'))
                        d['C'] = int(input('请输入C语言成绩:'))
                        new_list.append(d)
                        mark = 0
                    except:
                        print('修改失败,请重试!')
        with open(file_name,'w') as wfile:
            for i in new_list:
                wfile.write(str(i)+'\n')
            if id_del:
                print('修改成功!')
            mark_state = input('是否继续修改?Y/N:').lower()
            if mark_state == 'y':
                modify_func()
            else:
                return
                
    else:
        print('无学生信息')
​
​
# 排序函数
def sort_func():
    if not os.path.exists(file_name):
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    new_list = []
    # 读取展示所有存在的学生信息
    with open(file_name,'r')as rfile:
        old_list = rfile.readlines()
        for data in old_list:
            new_list.append(dict(eval(data)))
        show_func(new_list)
    # 选择排序方式
    print('请选择排序方式:')
    subject_option = input('1按英语成绩排序,2按Python成绩排序,3按C语音成绩排序,0按总成绩排序').strip()
    ad_option = input('0升序,1降序').strip()
    if ad_option == '0':
        ad = False # 升序
    elif ad_option == '1':
        ad = True  # 降序
    else:
        print('您的输入有误,请重试!')
        return
​
    new_ad_list = []
    if subject_option == '1':
        new_ad_list = sorted(new_list,key = lambda x : x['English'], reverse=ad)
    elif subject_option == '2':
        new_ad_list = sorted(new_list,key = lambda x : x['Python'], reverse=ad)
    elif subject_option == '3':
        new_ad_list = sorted(new_list,key = lambda x : x['C'], reverse=ad)
    elif subject_option == '0':
        new_ad_list = sorted(new_list,key = lambda x : x['English'] + x['Python'] + x['C'], reverse=ad)
    else:
        print('您的输入有误,请重试!')
        return
        
    show_func(new_ad_list)
​
# 统计学生总人数
def count_func():
    if not os.path.exists(file_name):
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    # 读取展示所有存在的学生信息
    with open(file_name,'r')as rfile:
        old_list = rfile.readlines()
        print('一共有{}名学生'.format(len(old_list)))
        
​
# 显示所有学生信息
def show_all_func():
    if not os.path.exists(file_name):
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    # 读取展示所有存在的学生信息
    new_list = []
    with open(file_name,'r')as rfile:
        old_list = rfile.readlines()
        for i in old_list:
            new_list.append(dict(eval(i)))
    show_func(new_list)
​
​
if __name__ == '__main__':
    menu()