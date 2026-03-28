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

import pandas as pd

File_PATH = ".\\appendix\\data.csv"

def main():
    while True:
        menu()
        choice = int(input("请选择："))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
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
                cal_shrinkage()
            elif choice == 7:
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
        "\n\t5.计算抗折强度"
        "\n\t6.计算线收缩率"
        "\n\t7.显示所有数据"
        "\n\t0.退出"
        "\n" + "-" * 52)


def insert():
    """
    数据数据并保存
    """
    data_list=[]
    blade_spacing = float(input("刀口距离(L)："))       # 提前设置好刀口距离
    while True:
        crafts = input("工艺序号：")
        if not crafts:
            break

        try:
            len_1 = float(input("烧结前试条长 l1(mm)："))
            len_2 = float(input("烧结后试条长 l2(mm)："))
            width = float(input("试条宽 d(mm)："))
            thickness = float(input("试条厚 h(mm)："))
            load_strength = float(input("荷载强度 P(N)："))

        except Exception as e:
            print(f"输入失败：{e}")
            continue
        # 数据保存到字典中
        data_no = {'crafts': crafts,
                   'L(mm)': blade_spacing,
                   'len_1(mm)': len_1,
                   'len_2(mm)': len_2,
                   'd(mm)': width,
                   'h(mm)': thickness,
                   'P(N)': load_strength}
        data_list.append(data_no)       # 数据添加到列表中

        continue_operate = input("继续？Y/n")
        if continue_operate == "Y" or continue_operate == "y":
            continue
        else:
            break

    # 存储数据
    # file_path = input("输入要保存数据的位置(保存此文件夹可用:'./data.csv')：")
    save_csv(data_list)
    print("保存完成")

def save_csv(data_list, file_path=File_PATH):
    try:
        csv_file = open(file_path, mode='a', newline='', encoding='utf-8')  # 追加
    except Exception as e:
        print(e)
        csv_file = open(file_path, mode='w', newline='', encoding='utf-8')  # 写入

    headers = list(data_list[0].keys())
    writer = csv.DictWriter(csv_file, fieldnames=headers)   # 指定表头结构
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)
    print(f"--- 写入完成: {file_path} ---")

def search():
    pass

def delete(file_path=File_PATH):

    # 读取 excel 文件
    df = pd.read_excel(file_path)

    while True:
        crafts = input("输入要删除的工艺号：")

        try:
            df = df[df['crafts'] != crafts]
        except Exception as e:
            print(e)
        # 保存数据
        df.to_csv(file_path, index=False)

        continue_operate = input("继续？Y/n")
        if continue_operate == "Y" or continue_operate == "y":
            continue
        else:
            break

    return df

def modify():
    pass

def cal_strength():
    pass

def cal_shrinkage():
    pass

def show_data(file_path=File_PATH):
    df = pd.read_csv(file_path)
    print(df)

    return None

if __name__ == '__main__':
    main()
