from random import choice

class RandomWalk():
    """生成一个随机漫步的类"""
    def __init__(self,num_points=100000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        """所有的点都从[0,0]开始"""
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步所有的点"""
        # 不断漫步 知道表达到指定的长度
        while len(self.x_values) < self.num_points:
            """计算前进的方向 速度 距离"""
            x_direction = choice([1,-1]) # 方向
            x_distance = choice([1,2,3,4]) # 速度
            x_step = x_direction * x_distance # 计算距离

            y_direction = choice([1,-1])
            y_distance = choice([1,2,3,4])
            y_step = y_distance * y_direction

            # 禁止原地踏步
            if x_step == 0 or y_step == 0:
                continue

            # 计算下一个点的x和y的值
            mext_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            # 存储
            self.x_values.append(mext_x)
            self.y_values.append(next_y)

# 画出随机漫步的所有的点
import matplotlib.pyplot as plt

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=14,c=(0,0,0))
plt.title("RandomWalk",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("Squares of value",fontsize=14)
plt.tick_params(axis="both",which = "major",labelsize = 14)
plt.savefig("随机漫步.png")
plt.show()
