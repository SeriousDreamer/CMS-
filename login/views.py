from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from utils import check_code


# Create your views here.
def show_login(request):
    """
    返回登录页面视图
    :param request:
    :return:
    """
    return render(request, 'logins.html')


@csrf_protect
def create_code(request):
    """
    返回验证码函数
    :param request:
    :return:
    """
    code, buf = check_code.create_code()
    if code:
        request.session['check_code'] = ''  # 清空session中的验证码信息
        request.session['check_code'] = code  # 将验证码存在服务器的session中，用于校验
        # fr = open(os.path.join(BASE_DIR, 'static/images/checkCode/code.png'), 'rb')
        # image = fr.read()
        return HttpResponse(buf.getvalue(), content_type="image/png")  # 将内存的数据读取出来，并以HttpResponse返回
    else:
        return HttpResponse('验证码获取失败')
