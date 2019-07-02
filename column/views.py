from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect
from . import models


# Create your views here.
def show_index(request):
    try:
        # 这里是点击添加顶级标题返回的视图
        if select_column():
            dic = select_column()
            # 这里data是在执行完add_column函数后返回的值
            data = request.GET['data']
            dic['result'] = data
            return render(request, 'column_list.html', dic)
        else:
            return render(request, 'column_list.html', {'result': "失败"})
    except:
        # 这里是点击栏目管理返回的视图
        if select_column():
            dic = select_column()
            return render(request, 'column_list.html', dic)
        else:
            return render(request, 'column_list.html', {'result': "失败"})


def select_column():
    """
    查询column的所有的值并且添加到字典中
    :return: dict类型，column的值
    """
    try:
        spl = models.Columns.objects.all()
        dic = {"column": []}
        for column in spl:
            dic["column"].append({
                "id": column.columnId, "name": column.name,
                "time": column.time, "parent": column.parent
            })
        return dic
    except Exception as e:
        return False


@csrf_protect
def add_column(request):
    """
    这个是点击添加顶级标题按钮后向数据库插入数据的逻辑控制函数
    :param request:
    :return:
    """
    column_name = request.POST['columnName']
    dic = {"name": column_name}
    try:
        spl = models.Columns(**dic)
        spl.save()
        return HttpResponse("添加成功")
    except Exception as e:
        print(e)
        return HttpResponse("添加失败")
