from django.shortcuts import render
from django.http import HttpResponse
from utils import check_code


# Create your views here.
def show_login(request):
    return render(request, 'logins.html')


def create_code(request):
    code = check_code.create_code()
    if code:
        request.session['check_code'] = ''  # 清空session中的验证码信息
        request.session['check_code'] = code  # 将验证码存在服务器的session中，用于校验
        fr = open('code.png', 'rb')
        image = fr.read()
        return HttpResponse(image, content_type="image/png")  # 将内存的数据读取出来，并以HttpResponse返回
