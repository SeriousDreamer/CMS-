from django.shortcuts import render
from . import is_login

# Create your views here.
"""
后台视图调用之前需要先判断用户是否登录，见show_index方法的示例。
is_login方法是用来判断用户是否已经登录的方法
"""


def show_index(request):
    if is_login.is_login(request):
        return render(request, 'adminIndex.html')
    else:
        dic = {'status': '请登录!!'}
        return render(request, 'logins.html', dic)
