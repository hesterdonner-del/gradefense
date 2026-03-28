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


# 程序结构

数据处理
```
main()
 ├── menu()            # 打印功能菜单
 ├── insert()          # 插入数据
  └── save_csv()       # 保存数据
 ├── search()          # 搜索数据
 ├── delte()           # 删除数据
 ├── modify()          # 修改数据
 ├── cal_strength()    # 计算抗折强度 
 ├── cal_shrinkage()   # 计算线收缩率
 └── show_data()       # 展示数据
```

箱线图
```
main()
 └── box_plot()       # 绘制箱线图
```

柱状图
```
main()
└── box_plot()         # 读取数据
 ├── cal_std()         # 计算标准差
 └── plot_bar_error()  # 绘制柱状图
```

三线表
```
main()
 ├── open_file_folder()       # 选择文件夹和文件
 ├── print_excel()            # 读取 Excel 文件所有的页
 ├── read_excel()             # 读取 Excel 文件，返回 DataFrame
 └── dataframe_to_tlt()       # 将 DataFrame 数据转换为 Word 表格
  ├── remove_all_borders()    # 清除所有单元格边框
   └── set_cell_border()      # 设置单元格
  └── apply_tlt()             # 生成三线表
```
