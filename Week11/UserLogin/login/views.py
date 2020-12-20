from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .form import LoginForm


def index(request):
    login_msg = '''
    您好!<br>
    这是登录成功后跳转的页面<br>
    您应该在用户验证成功后看到它<br>
    '''
    return HttpResponse(login_msg)


def userlogin(request):
    # POST
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            cd = loginform.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            print(user)
            if user:
                login(request, user)
                return HttpResponseRedirect('index')
            else:
                err_msg = '''
                登录失败！<br>
                请检查用户名或密码是否输入正确<br>
                如有疑问请联系系统管理员<br>
                '''
                return HttpResponse(err_msg)

    # GET
    if request.method == "GET":
        loginform = LoginForm()
        return render(request, 'loginform.html', {'form': loginform})
