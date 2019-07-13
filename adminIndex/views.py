from django.shortcuts import render


# Create your views here.


def show_index(request):
    """
    返回后台主页视图
    :param request:
    :return:
    """
    url = request.path
    return render(request, 'adminIndex.html', {'url': url})
