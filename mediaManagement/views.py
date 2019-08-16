import json
import os
import random
import time
from decimal import Decimal
from PIL import Image
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from . import models
from manager import models as ma_models

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from cms import settings


def media_list(request):
    """
    返回资源管理的页面
    :param request:
    :return:
    """
    list_type = int(request.GET["type"])
    # 当前div的宽度
    width = float(request.GET["width"])
    file_obj = models.Media.objects.all()
    dic = {"result": []}
    for i in file_obj:
        dic["result"].append({
            "id": i.id,
            "img_id": "img" + str(i.id),
            "name": i.name,
            "date": i.date,
            "original": (i.width, i.height),
            "url": settings.MEDIA_URL + str(i.url),
            "author": i.author.name,
        })
    if list_type == 0:  # 返回瀑布流式 视图
        part = 4
        one_width = round(width / part, 2)
        dic["width"] = str(one_width) + "px"
        dic["part"] = part
        # 控制瀑布流
        height_lis = []
        width_lis = []
        for i in range(part):
            height_lis.append(0)
            width_lis.append(round(one_width * i, 2))
        print(width_lis)
        for i in range(int(len(file_obj) / part) + 3):
            for n in range(part):
                min_id = min(height_lis)
                index = 0
                for m in range(len(height_lis)):
                    if height_lis[m] == min_id:
                        index = m
                        break
                if (n + i * part) < len(file_obj):
                    dic["result"][n + i * part]["top"] = str(height_lis[index]) + "px"
                    dic["result"][n + i * part]["left"] = str(width_lis[index]) + "px"
                    height = get_height(one_width, dic["result"][n + i * part]["original"])
                    dic["result"][n + i * part]["height"] = "%.2fpx" % height
                    height_lis[index] += round(height, 2)
        # -----
        print(dic['width'])
        page = int(request.GET["page"])
        if page == 0:
            return render(request, 'media.html', dic)
        else:
            return render(request, 'mediaList.html', dic)
    elif list_type == 1:  # 返回列表式视图
        pass


def get_height(width, original):
    return (original[1] / original[0]) * width


@csrf_exempt
def upload(request):
    try:
        upload_file = request.FILES["file"]
        if not upload_file:
            upload_file = request.FILES['editormd-image-file']
    except MultiValueDictKeyError as e:
        return JsonResponse({'state': 0, 'message': 'Not support method or Can not get file'})

    if request.method == "POST" and upload_file:
        success, message = 0, '上传失败'
        # 修改上传文件的名称
        file_name = time.strftime('%H%M%S') + "_" + upload_file.name
        img = Image.open(upload_file)
        width = img.size[0]
        height = img.size[1]
        upload_file.name = file_name
        author = ma_models.Manager.objects.get(name=request.COOKIES.get("uname"))
        # 创建本地保存本地文件图片
        dic = {
            "name": file_name,
            "author": author,
            "width": width,
            "height": height,
            "url": upload_file
        }
        try:
            file_obj = models.Media.objects.create(**dic)
            success, message = 1, '上传成功'
        except Exception as e:
            print(e)
            return JsonResponse({'state': 0, 'message': 'Not support method or Can not get file'})
        # 返回格式
        year = time.strftime('%Y', time.localtime())
        month = time.strftime('%m', time.localtime())
        day = time.strftime('%d', time.localtime())
        path = settings.MEDIA_URL + year + '/' + month + '/' + day + '/'
        data = {
            'success': success,
            'message': message,
            'url': path + file_name
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'state': 0, 'message': 'Not support method or Can not get file'})


@csrf_exempt
def delete(request):
    """
    删除资源文件方法
    :param request:
    :return:
    """
    result = {"code": 400}
    if request.method == "POST":
        did = request.POST['id']
        img_obj = models.Media.objects.get(id=did)
        try:
            img_obj.delete()
            result["code"] = 200
            return HttpResponse(json.dumps(result), content_type='application/json')
        except models.Media as e:
            print(e)
            return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        return HttpResponse(json.dumps(result), content_type='application/json')
