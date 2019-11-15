import pygal
import random

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(0,self.num_sides)

if __name__ == '__main__':
    die = Die()
    print(die.roll())
    # 掷骰子100
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # 分析结果
    frequencys = []
    for value in range(1,die.num_sides+1):
        frequency = results.count(value)
        frequencys.append(frequency)

    #print(frequencys)

# 绘制直方图
# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencys)
hist.render_to_file('die_visual.svg')
