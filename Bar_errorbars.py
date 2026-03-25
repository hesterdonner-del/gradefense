# Name: Wade:@
# Data: 2026/3/25 17:14
from random import sample

import matplotlib.pyplot as plt
import numpy as np


def cal_std(data_list):
    """
    :param data_list: 传入的数据为列表
    功能：计算标准差
    总体标准差：准确描述总体数据的离散程度。
    样本标准差：用样本信息去无偏估计总体标准差（样本较少时，总体标准差通常比样本标准差小）
    """
    pop_std = np.std(data_list)              # 总体标准差 (ddof=0, 默认)
    sample_std = np.std(data_list, ddof=1)   # 样本标准差 (ddof=1)
    return pop_std, sample_std



