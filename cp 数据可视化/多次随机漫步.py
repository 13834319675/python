from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    def __init__(self,num_points=5000):
        self.x_values = [0]
        self.y_values = [0]
        self.num_points = num_points

    def fill_waik(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([1,2,3,4])
            x_step = x_distance * x_direction

            y_direction = choice([1,-1])
            y_distance = choice([1,2,3,4])
            y_step = y_distance * y_direction

            if x_step ==0 or y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:
    n = 1
    rw = RandomWalk()
    rw.fill_waik()
    # 随机漫步的颜色映射
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,s = 10,
                c = point_numbers,cmap=plt.cm.Blues,
                edgecolors="none",)
    # 设置起点的终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100)

    plt.title("RandomWalk points",fontsize = 24 )
    plt.xlabel("keys", fontsize = 14)
    plt.ylabel("values",fontsize = 14)
    plt.tick_params(axis="both",which = "major", labelsize = 10)
    plt.savefig("随机漫步{}.png".format(n))
    plt.show()
    keep_runing = input("Make another walk? (y/n)?")
    if keep_runing == "y" or keep_runing == "Y":
        break