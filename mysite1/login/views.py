from django.shortcuts import render,redirect
from . import models
from . import froms

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')

"""def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容！'
        if username.strip() and password:
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', {'message': message})

            if user.password == password:
                print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')"""
def login(request):
    if request.session.get("is_login",None):#不允许重复登录
        return redirect('/index/')
    if request.method == "POST":
        login_from = froms.Userfroms(request.POST)
        massage = "请检查填写的内容"
        if login_from.is_valid(): #数据验证
            username = login_from.cleaned_data.get("username")
            password = login_from.cleaned_data.get("password")
            try:
                user = models.User.objects.get(name=username)
            except:
                massage = "用户名不存在"
                return render(request,"login/login.html",locals())
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect("/index/")
            else:
                massage = "密码错误"
                return render(request,'login/login.html',locals())
        else:
            return render(request,'login/login.html',locals())
    login_from = froms.Userfroms()
    return render(request,'login/login.html',locals())




def register(request):
    pass
    return render(request,"login/register.html")

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")

# Create your views here.
