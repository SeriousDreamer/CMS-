from manager.models import Manager
from django.shortcuts import render
import jwt, time
from cms import settings


def is_login(request):
    """
    判断用户cookie是否可登录后台
    :param request: request对象
    :return: bool类型，True表示验证通过，False表示验证失败
    """
    uname = request.COOKIES.get('uname')
    token = request.COOKIES.get('token')
    json_str = jwt.decode(token, settings.TOKEN_KEY, algorithms="HS256")
    if not json_str:
        return False
    manager = Manager.objects.get(name=uname)
    if manager.name != json_str["username"]:
        return False
    t = time.time() - json_str['exp']
    # 登录超时
    if t >= 0:
        return False
    return True
