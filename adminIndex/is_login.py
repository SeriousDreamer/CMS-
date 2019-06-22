from manager.models import Manager
from django.shortcuts import render


def is_login(request):
    """
    判断用户cookie是否可登录后台
    :param request: request对象
    :return: bool类型，True表示验证通过，False表示验证失败
    """
    uname = request.COOKIES.get('uname')
    upwd = request.COOKIES.get('npwd')
    manager = Manager.objects.all()
    spassword = ""
    for i in manager:
        if uname == i.name:
            spassword = i.password
    if upwd == spassword:
        return True
    else:
        return False
