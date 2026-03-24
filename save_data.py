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
import csv
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
    """
    数据数据并保存
    """
    data_list=[]
    blade_spacing = input("刀口距离(L)：")       # 提前设置好刀口距离
    while True:
        process_no = input("工艺序号：")
        if not process_no:
            break

        try:
            length_1 = float(input("烧结前试条长 l1(mm)："))
            length_2 = float(input("烧结后试条长 l2(mm)："))
            width = float(input("试条宽 d(mm)："))
            thickness = float(input("试条厚 h(mm)："))
            load_strength = float(input("荷载强度 P(N)："))

        except Exception as e:
            print(f"输入失败：{e}")
            continue
        # 数据保存到字典中
        data_no = {'process_no': process_no,
                   'blade_spacing': blade_spacing,
                   'length_1': length_1,
                   'length_2': length_2,
                   'width': width,
                   'thickness': thickness,
                   'load_strength': load_strength}
        data_list.append(data_no)       # 数据添加到列表中

        continue_insert = input("继续？Y/n")
        if continue_insert == "Y" or continue_insert == "y":
            continue
        else:
            break

    # 存储数据
    # file_path = input("输入要保存数据的位置(保存此文件夹可用:'./data.csv')：")
    save_csv(data_list)
    print("保存完成")

def save_csv(data_list, file_path="./data.csv"):
    try:
        csv_file = open(file_path, mode='a', newline='', encoding='utf-8')  # 追加
    except Exception as e:
        print(e)
        csv_file = open(file_path, mode='w', newline='', encoding='utf-8')  # 写入
    headers = list(data_list[0].keys())
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)
    print("写入完成".format(file_path))

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
