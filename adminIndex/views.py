from django.shortcuts import render
from . import is_login


# Create your views here.


def show_index(request):
    if is_login.is_login(request):
        return render(request, 'adminIndex.html')
    else:
        dic = {'status': '请登录!!'}
        return render(request, 'logins.html', dic)
