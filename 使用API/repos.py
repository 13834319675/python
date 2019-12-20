import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
req = requests.get(url)
print("Staus code:",req.status_code)
# 将API响应存储在一个变量中
response_dict = req.json()
print(response_dict)
# 处理结果
print(response_dict.keys())
print("Total repositories:",response_dict["total_count"])

# 探索有关仓库的信息
repos_dicts = response_dict["items"]
print("Repositories returns:",len(repos_dicts))

# 研究第一个仓库
repo_dict = repos_dicts[0]
print(repo_dict)
print("\nLeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected information about frist repository")
print("Name:",repo_dict["name"])
print("Owner:",repo_dict["owner"]["login"])
print("Stars:",repo_dict["stargazers_count"])
print("Repository:",repo_dict["html_url"])
print("Creater:",repo_dict["created_at"])
print("Update:",repo_dict["updated_at"])
print('Description:', repo_dict['description'])