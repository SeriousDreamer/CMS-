from django.shortcuts import render,redirect
from django.views.decorators import csrf
from manager.models import Manager
from django.http import HttpResponse
import hashlib


def do_login(request):
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
        res = redirect('/luna/')
        res.set_cookie('uname',name)
        res.set_cookie('npwd',spassword)
        return res
