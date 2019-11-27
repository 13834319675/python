import json
filename = "readable_eq_data.json"
with open(filename) as f:
    pop_date = json.load(f)
    print(pop_date)
# 打印每个国家的人口数量
for pop_dict in pop_date:
    print(pop_dict)
    for pop_features in pop_date[pop_dict]:
        for pop_properties in pop_date[pop_dict][pop_features]:
            print(pop_properties)



