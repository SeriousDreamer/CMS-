import json

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect
from . import models


# Create your views here.
def show_index(request):
    """
    显示分类目录页面
    :param request:
    :return:
    """
    dic = select_column()
    if dic:
        try:
            # 这里是点击添加顶级标题返回的视图
            # 这里data是在执行完add_column函数后返回的值
            data = request.GET['data']
            dic['result'] = data
            return render(request, 'column_list.html', dic)
        except Exception as e:
            print(e)
            # 这里是点击栏目管理返回的视图
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
        dic1 = {}
        # 以下循环用于整理数据格式
        for column in spl:
            if column.parent == 0:
                dic1[column.columnId] = {"parent": [column], "child": []}
            elif column.parent != 0:
                dic1[column.parent]["child"].append(column)
        for k, v in dic1.items():
            dic['column'].append(v['parent'][0])
            for i in v['child']:
                dic['column'].append(i)
        return dic
    except Exception as e:
        print(e)
        return False


@csrf_protect
def add_column(request):
    """
    这个是点击添加顶级标题按钮后向数据库插入数据的逻辑控制函数
    :param request:
    :return:
    """
    column_name = request.POST['columnName']
    parent_name = request.POST['parentName']
    if parent_name:
        parent_name = int(parent_name)
    dic = {"name": column_name, 'parent': parent_name}
    result = {"status": 400, "result": "添加失败"}
    if not dic['name']:
        result["result"] = "请输入栏目名称"
        return HttpResponse(json.dumps(result), content_type='application/json')
    try:
        spl = models.Columns(**dic)
        spl.save()
        result['status'] = 200
        result['result'] = "添加成功"
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_protect
def delete_column(request):
    column_id = int(request.POST['columnId'])
    try:
        sql = models.Columns.objects.get(columnId=column_id)
        print(sql.name)
        if sql.parent == 0:
            column = models.Columns.objects.all()
            for i in column:
                if i.parent == column_id:
                    return HttpResponse('请删除该分类的所有子分类')
            sql.delete()
            return HttpResponse('删除成功')
        else:
            sql.delete()
            return HttpResponse('删除成功')
    except Exception as e:
        print(e)
        return HttpResponse('删除失败')
