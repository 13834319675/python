from urllib import request
import json
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"

rep = request.urlopen(url)
data = rep.read().decode()

data = json.loads(data)

print(data)

for i in data:
    print(i)
    