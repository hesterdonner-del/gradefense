# Name: Wade:@
# Data: 2026/3/12 15:25

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('demo.xlsx', sheet_name='Sheet2')
print(df)

x1 = df['#1']
x2 = df['#2']
x3 = df['#3']
x4 = df['#4']
# x5 = df['#5']
x6 = df['#6']
# x7 = df['#7']
x8 = df['#8']
# x9 = df['#9']
data = [x1.values, x2.values, x3.values, x4.values, x6.values, x8.values]

plt.boxplot(data,
            patch_artist=True,
            widths=0.5,
            showmeans=True,
            meanprops={'marker':'+',
                    'markerfacecolor':'k',
                    'markeredgecolor':'k',
                    'markersize':5
                       }
        )

plt.ylim([50,150])
plt.xticks([1,2,3,4,5,6],['#1','#2','#3','#4', '#6', '#8'])
plt.grid(axis='y',ls='--',alpha=0.5)
plt.ylabel('抗折强度(MPa)', fontsize=11)
plt.tight_layout()
plt.savefig('boxplot1.svg')
plt.show()