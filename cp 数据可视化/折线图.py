import matplotlib.pyplot as plt
# 同时提供输入值和输出值
input_value = [1,2,3,4,5,6]
squares = [1,4,9,15,23,31]
plt.plot(input_value,squares,linewidth=5) # 线条的粗细
# 设置图标的标题,并绘制标轴加上标签
plt.title("Squers Nembers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Squers Value",fontsize=14)
# 设置刻度标记和大小
plt.tick_params(axis="both",labelsize=14)
plt.show()