from django.http import JsonResponse
from django.shortcuts import render
import time
import os
from cms import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def show_index(request):
    """
    返回后台主页视图
    :param request:
    :return:
    """
    url = request.path
    return render(request, 'adminIndex.html', {'url': url})


@csrf_exempt
def upload(request):
    # markdown上传图片方法
    upload_file = request.FILES['editormd-image-file']
    if request.method == "POST" and upload_file:
        success, message = 0, '上传失败'

        # 创建本地保存本地文件图片
        year = time.strftime('%Y', time.localtime())
        month = time.strftime('%m', time.localtime())
        day = time.strftime('%d', time.localtime())
        path = settings.STATIC_URL + 'upload/' + year + '/' + month + '/' + day + '/'
        if not os.path.exists(settings.BASE_DIR + path):
            os.makedirs(settings.BASE_DIR + path)
        # 修改上传文件的名称
        file_name = time.strftime('%H%M%S') + "_" + upload_file.name
        local_file = settings.BASE_DIR + path + file_name
        # 写入文件
        with open(local_file, 'wb+') as f:
            for chunk in upload_file.chunks():
                f.write(chunk)
            success, message = 1, '上传成功'

        # 返回格式
        data = {
            'success': success,
            'message': message,
            'url': path + file_name
        }

        return JsonResponse(data)
    else:
        return JsonResponse({'state': 0, 'message': 'Not support method or Can not get file'})
