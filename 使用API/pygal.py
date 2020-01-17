import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("stayus_code:",r.status_code)
# 将Api相应存放在一个变量中,转换为json格式
response_dict = r.json()
print("Total repositories:",response_dict["total_count"])
# 研究有关仓库的信息
repo_dicts = response_dict["items"]

names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["Stargazers_count"])

# 可视化
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title =  'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add("",stars)
chart.render_to_file("python_rope.svg")