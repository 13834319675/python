import csv
filename = "sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    for index,colum_header in enumerate(header_row):
        print(index,colum_header)

    highs  = []
    for row in reader:
        high = [64, 71, 64, 59, 69, 62, 61, 55, 57, 61, 57, 59, 57, 61, 64, 61, 59, 63, 60, 57,
 69, 63, 62, 59, 57, 57, 61, 59, 61, 61, 66]      #int(row[1])
        highs.append(high)
    print(row)

import matplotlib.pyplot as plt
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c="red")
plt.title("Dally high temperatures,2018",fontsize=24)
plt.xlabel("",fontsize=14)
plt.ylabel("Temperature()",fontsize=14)
plt.tick_params(axis="both",which="major",labelsize=16)
plt.show()