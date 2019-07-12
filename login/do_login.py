from django.shortcuts import render, redirect
from manager.models import Manager
import hashlib, json, jwt, time
from cms import settings


def do_login(request):
    """
    登录逻辑处理函数
    :param request:
    :return:
    """
    if request.POST:
        ctx = request.POST
        check_code = request.session['check_code'].lower()
        name = ctx['uname']
        password = ctx['upwd']
        validate = ctx['validate'].lower()
        manager = Manager.objects.all()
        sname = ''
        spassword = ''
        for i in manager:
            if name == i.name:
                sname = i.name
                spassword = i.password
        h = hashlib.md5()
        h.update(str(password).encode())
        password = h.hexdigest()
        error = {'check': "验证码错误", 'up': "账号或密码错误"}
        if validate != check_code:
            dic = {'status': '验证码错误'}
            return render(request, 'logins.html', dic)
        if name != sname or password != spassword:
            dic = {'status': '账号或密码错误'}
            return render(request, 'logins.html', dic)
        # 经过上面验证成功后重定向到后台页面
        res = redirect('/luna/')
        exp = int(time.time() + settings.TOKEN_TIME)
        payload = {
            "exp": exp,
            "username": ctx['uname']
        }
        token = jwt.encode(payload, settings.TOKEN_KEY, algorithm="HS256")
        res.set_cookie('uname', name)
        res.set_cookie('token', token)
        return res
