from django.http import HttpResponse, Http404
from django.utils.deprecation import MiddlewareMixin
import re
from utils.is_login import is_login
from django.shortcuts import render


class loginMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        """
        执行视图之前被调用
        :param request:
        :return:
        """
        if not re.match('^/luna', request.path_info):
            return

        if is_login(request):
            return
        else:
            dic = {'status': '请登录!!'}
            return render(request, 'logins.html', dic)