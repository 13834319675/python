import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value,y_value,edgecolors="none",s=40,
            c=y_value, cmap=plt.cm.Blues)
plt.title("Squares",fontsize = 24)
plt.xlabel("Values",fontsize=14)
plt.ylabel("Squares of Values",fontsize=14)
plt.axis([0,1001,0,1100000])
plt.tick_params(axis="both",which="major",labelsize=14)
plt.show()
# 保存图像
plt.savefig("Squares.png",bbox_inches="tight")
