# 问题
在制备莫来石陶瓷之后，测试其数据分析陶瓷性能的好坏。

能够完成：输入数据→数据处理→输出图表

# 需求分析

### 输入数据（float）
某一组
	试条的长
	试条的宽
	试条的高

### 数据处理（增删改查+计算）
存储数据
	csv
	数据库？
计算
	抗折强度
		计算一组实验强度观测值的平均值，并剔除相对误差过大的值。
	线收缩率

### 输出图表
表
	三线表（注意格式）
图
	箱线图
	柱状图（含误差线）
# 算法

抗折强度
	1. Input observation list
	2. Calculate average value
	3. Find maximum and minimum values
	4. Compute relative error of both
	5. Remove value with largest relative error if threshold exceeded
	6. Repeat until condition satisfied
	7. Output final average

# 程序结构


抗折强度
```
main()
 ├── read_data()
 ├── calculate_average()
 ├── calculate_relative_error()
 ├── filter_data()
 └── display_results()
```

