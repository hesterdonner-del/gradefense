# Name: Wade:@
# Data: 2026/3/24 16:44

"""
1. 需求分析
    添加数据
    保存数据到文件中
    修改和删除数据
    查询数据
    数据计算

2. 系统设计
    增删改查
    计算
3. 主函数设计


"""

import os
import re


def main():
    while True:
        menu()
        choice = int(input("请选择："))
        if choice in [0, 1, 2, 3, 4, 5, 6]:
            if choice == 0:
                ans = input("确定推出系统？Y/n")
                if ans == "Y" or ans == "y":
                    break
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                cal_strength()
            elif choice == 6:
                show_data()
        else:
            print("请输入合适的数字！")
            break



def menu():
    print("=" * 20 + "数据管理系统" + "=" * 20,
        "\n" + "-"*22 + "功能菜单" + "-"*22,
        "\n\t1.保存数据"
        "\n\t2.查询数据"
        "\n\t3.删除数据"
        "\n\t4.修改数据"
        "\n\t5.抗折强度计算"
        "\n\t6.显示所有数据"
        "\n\t0.退出"
        "\n" + "-" * 52)


def insert():
    data_list=[]
    while True:
        process_no = input("工艺序号：")
        if not process_no:
            break

        try:
            length = float(input("试条长："))
            width = float(input("试条宽："))
            thickness = float(input("试条厚度："))
        except Exception as e:
            print(f"输入失败：{e}")
            continue
        # 数据保存到字典中
        data_no = {'process_no': process_no, 'length': length, 'width': width, 'thickness': thickness}
        data_list.append(data_no)       # 数据添加到列表中

        continue_insert = input("继续？Y/n")
        if continue_insert == "Y" or continue_insert == "y":
            continue
        else:
            break

    # 存储数据

def search():
    pass

def delete():
    pass

def modify():
    pass

def cal_strength():
    pass

def show_data():
    pass

if __name__ == '__main__':
    main()
