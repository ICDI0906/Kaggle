# https://www.kaggle.com/c/whale-categorization-playground/data
# PLI Python Imaging Library
# tqdm 终端进度条工具
#
import pandas as pd
import matplotlib.pyplot as plt
image = plt.imread('me.jpg')
from collections import Counter

# 图像文件读取
imgs = [image for i in range(10)]
figure = plt.figure(figsize = (13, 8))
cols = 3
rows = len(imgs) // cols + 1
for i in range(len(imgs)):
    subplot = figure.add_subplot(rows, cols, i+1) # 在原图中画子图
    # subplot.axis('Off')
    # plt.imshow(imgs[i], cmap = 'gray')
# plt.show()

# 随机采样
frame = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
frame.sample(frac = 0.25)  # 参数可以是n = 或者 frac = a 表示从Frame中采样n个或者a%个数据

# 统计计算
counter = Counter(frame[0].value_counts().values) # 对values进行统计个数计算
# print(counter.keys())

# 画图
x = range(3)
y = range(3)
xlabels = ['z', 'k', 's']
plt.bar(x, y)
plt.xticks(x, xlabels)  # 可以将x 对应的值转换为xlabel 对应的索引，然后显示xlabels的值
plt.show()