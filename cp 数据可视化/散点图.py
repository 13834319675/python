import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)
# 设置图标的标题并绘制坐标轴和加上标签
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Squares of Value",fontsize=14)
# 设置刻度标记和大小
plt.tick_params(axis="both",which="major",labelsize=14)
plt.show()

# 视同scatter绘制一系列的点
x_vallue = [1,3,5,7,9]
y_vallue = [2,4,6,8,10]
# edgecolors 去除点的默认轮廓
plt.scatter(x_vallue,y_vallue,s=100,edgecolor="none")
plt.title("Squares number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Squares of Value",fontsize=14)
#设置刻度标记和大小
plt.tick_params(axis="both",which="major",labelsize=14)
plt.show()

# 手动计算生成点的坐标
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,edgecolors="none",
            c=(0,0.1,0.1),s=40)
plt.title("",fontsize=24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Squares of value",fontsize=14)
# 设置取值范围
plt.axis([0,1100,0,1100000])
# 奢姿刻度标记大小
plt.tick_params(axis="both",which="major",labelsize=14)
plt.show()

