from django.shortcuts import render, redirect
from . import is_login

# Create your views here.
"""
后台视图调用之前需要先判断用户是否登录，见show_index方法的示例。
is_login方法是用来判断用户是否已经登录的方法
"""


def show_index(request):
    """
    返回后台主页视图
    :param request:
    :return:
    """
    if is_login.is_login(request):
        url = request.path
        return render(request, 'adminIndex.html', {'url': url})
    else:
        dic = {'status': '请登录!!'}
        return render(request, 'logins.html', dic)
