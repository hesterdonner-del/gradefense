# Name: Wade:@
# Data: 2026/3/25 17:14

"""
 从 Excel 读取实验弯曲强度数据， 计算平均值和标准差， 并绘制带有误差线的柱状图。
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

# 设置中文字体（根据系统环境可能需要调整）
plt.rcParams['font.family'] = ['Times New Roman','SimSun']
plt.rcParams['axes.unicode_minus'] = False   # 解决负号显示问题


def load_data(file_path: Path, sheet_name: str) -> pd.DataFrame:
    """
    读取 Excel 文件

    Parameters
        file_path : Path excel文件路径
        sheet_name : str 包含实验数据的表格
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Excel文件未找到：{file_path}")

    df = pd.read_excel(file_path, sheet_name=sheet_name, header=0, index_col=0)
    # print(df.head())

    return df

def cal_std(df: pd.DataFrame):
    """
    功能：计算平均值和标准差
    总体标准差：针对整组数据（所有个体），准确描述总体数据的离散程度。
    样本标准差：针对总体中的部分抽样数据，用样本信息去无偏估计总体标准差
    （样本较少时，总体标准差通常比样本标准差小）

     返回值：
        mean_values : 数组
        std_values : 数组
        samples : 列表
    """
    # 样本名称（列名）
    samples = df.columns.tolist()

    # 数据行：第2-6行（对应索引1到5，因为第0行是列名）
    data_rows = df.iloc[0:5]       # 五个重复测量值
    # 平均值行：第7行（对应索引6）
    mean_row = df.iloc[5]          # AV 行

    mean_values = mean_row.values               # 提取平均值数据
    std_values = data_rows.std(ddof=1).values   # 计算每列的标准差（样本标准差，ddof=1）

    return mean_values, std_values, samples     # 样本标准差 (ddof=1)


def plot_bar_error(mean_values, std_values, samples):
    """
    绘制带有标准差误差线的柱状图。
    """
    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(
                samples, mean_values, yerr=std_values, capsize=5,
                color='#1f77b4', edgecolor='black', alpha=0.8,
                error_kw={'linewidth': 2, 'ecolor': 'red'}
            )

    # 添加数据标签（平均值）
    for bar, mean_val in zip(bars, mean_values):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.5,
            f'{mean_val:.2f}', ha='center', va='bottom', fontsize=15
        )

    # 设置标题和轴标签
    plt.title('抗折强度平均值及标准差', fontsize=14)
    # plt.xlabel('样本编号', fontsize=14)
    plt.ylabel('抗折强度 (MPa)', fontsize=12)
    plt.tight_layout()

    plt.savefig(".\\appendix\\Bar_error.svg", transparent=False)
    plt.show()



def main():
    FILE_PATH = Path(".\\appendix\\Experimental_Data.xlsx")
    SHEET_NAME = "抗折强度"

    df = load_data(FILE_PATH, SHEET_NAME)

    mean_values, std_values, samples = cal_std(df)

    plot_bar_error(mean_values, std_values, samples)


if __name__ == "__main__":
    main()



