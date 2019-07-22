# 文件存储
from urllib import request,error

if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"
    try:
        rep = request.urlopen(url)
        rsp = rep.read().decode()

        with open("html1.html","w") as f:
            f.write(rsp)
    except error.HTTPError as e:
        print(e)
    except error.URLError as  e:
        print(e)
    except Exception as e:
        print(e)

