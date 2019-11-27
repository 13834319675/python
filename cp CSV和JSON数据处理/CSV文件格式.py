import csv
from datetime import datetime
filename = "sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index,colum_header in enumerate(header_row):
        print(index,colum_header)

    dates,highs,lows  = [],[],[] # 时间 最高 最低
    for row in reader:
        high = int(row[5])
        highs.append(high)
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        low = int(row[6])
        lows.append(low)
    print(row)
    print(highs)
    print(lows)
    print(dates)

import matplotlib.pyplot as plt
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)
plt.title("Daily high and low temperatures,2018",fontsize=24)
fig.autofmt_xdate() #倾斜
plt.xlabel("",fontsize=14)
plt.ylabel("Temperature()",fontsize=14)
plt.tick_params(axis="both",which="major",labelsize=16)
plt.show()