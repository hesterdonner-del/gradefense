# Name: Wade:@
# Data: 2026/3/12 15:25

import pandas as pd
import matplotlib.pyplot as plt

# 解决不显示的问题：中文设置为 宋体 格式，英文设置为 Times New Roman 格式
plt.rcParams['font.family'] = ['Times New Roman','SimSun']
df = pd.read_excel('.\\appendix\\Experimental_Data.xlsx',
                   sheet_name='抗折强度',
                   usecols=['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8'])
# print(df)
data = df.iloc[0:5]     # 获取第 1 到 6 行（索引0-5）
# print(data)

plt.boxplot(x=data,             # 绘制的数据
            patch_artist=True,  # 垂直排列箱线图
            widths=0.5,         # 箱型宽度
            showmeans=True,     # 显示均值点
            meanprops={'marker':'+',    # 设置均值点属性
                    'markerfacecolor':'k',
                    'markeredgecolor':'k',
                    'markersize':5
                       }
        )

plt.ylim([50,150])              # 设置 y 轴范围
plt.xticks([1,2,3,4,5,6,7,8],   # 替换刻度，前者为刻度位置，后者为对应的标签
           ['#1','#2','#3','#4','#5','#6','#7','#8'])
plt.ylabel('抗折强度(MPa)', fontsize=11)
plt.savefig('.\\appendix\\boxplot.svg')     # 保存 svg 格式的图片
plt.show()

