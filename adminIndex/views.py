from django.shortcuts import render

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
    url = request.path
    return render(request, 'adminIndex.html', {'url': url})


