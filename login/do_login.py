from django.shortcuts import render
from django.views.decorators import csrf


def do_login(request):

    if request.POST:
        ctx = request.POST
        check_code = request.session['check_code']
        name = ctx['uname']
        password = ctx['upwd']
        validate = ctx['validate']
        print(ctx)
        print(check_code)

