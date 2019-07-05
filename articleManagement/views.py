from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import models
from column import models as column_models
from django.views.decorators.csrf import csrf_protect
from column import views as co_views
from column.views import select_column
import json


# Create your views here.
def show_index(request):
    """
    返回文章列表视图函数
    :param request:
    :return:
    """
    articles = models.Article.objects.filter(available=1)
    dic = {"article": []}
    for article in articles:
        dic['article'].append({'id': article.id, 'title': article.title,
                               'author': article.author, 'image': article.image,
                               'content': article.content, 'time': article.time,
                               'columns': article.column, 'introduction': article.introduction,
                               'publicStatus': article.publicStatus, 'commentStatus': article.commentStatus,
                               'commentId': article.commentId, 'url': article.url, 'column': article.column.all(),
                               'available': article.available})
    return render(request, 'articleList.html', dic)


@csrf_protect
def write_article(request):
    """
    处理写文章逻辑
    :param request:
    :return:
    """
    if request.method == "GET":
        # 返回写文章的视图
        articles = models.Article.objects.order_by('-id')
        id_article = 0
        for article in articles:
            id_article = article.id
            break
        id_article += 1
        dic = co_views.select_column()
        dic['url'] = "127.0.0.1:8000/article/%s.html" % id_article
        return render(request, 'writeArticle.html', dic)
    elif request.method == "POST":
        # 接受文章的内容
        result = request.POST
        title = result['title']
        author = request.COOKIES.get('uname')
        content = result['content']
        markdown = result['markdown']
        column = result['column']
        introduction = result['introduction']
        public_status = result['publicStatus']
        comment_status = result['commentStatus']
        url = result['url']
        if not title:
            title = "未命名"
        if not author:
            return render(request, 'logins.html', {"status": '请登录'})
        if not content:
            content = ""
        if not introduction:
            introduction = ""
        if not url:
            url = '127.0.0.1'
        if comment_status == "true":
            comment_status = True
        elif comment_status == "false":
            comment_status = False
        if public_status == "true":
            public_status = True
        elif public_status == "false":
            public_status = False
        dic = {
            'title': title, 'author': author,
            'content': content,
            'introduction': introduction, "publicStatus": public_status,
            "commentStatus": comment_status, 'url': url, 'markdown': markdown
        }
        column = column.split(',')[0:-1]
        try:
            # 处理文章的分类创建
            art = column_models.Columns.objects.get(columnId=int(column[0]))
            art = art.article_set.create(**dic)
            for i in range(1, len(column)):
                column_models.Columns.objects.get(columnId=int(column[i])).article_set.add(art)
        except Exception as e:
            print(e)
            return HttpResponse("发布失败")
        return HttpResponse("发布成功")


@csrf_protect
def update_article(request):
    """
    修改文章函数
    :param request:
    :return:
    """
    if request.method == "GET":
        # 当请求方式为GET时候是请求需要修改的文章的原本的内容
        url = request.GET['url']
        try:
            article = models.Article.objects.get(url=url)
        except Exception as e:
            print(e)
            return HttpResponse("查找失败")
        columns = article.column.all()
        column_name = []
        for i in columns:
            column_name.append(i.name)
        dic = select_column()
        dic["title"] = article.title
        dic["author"] = article.author
        dic["content"] = article.content
        dic["updateColumn"] = column_name
        dic["introduction"] = article.introduction
        dic["publicStatus"] = article.publicStatus
        dic["commentStatus"] = article.commentStatus
        dic["url"] = article.url
        dic["markdown"] = article.markdown
        print(dic['updateColumn'])
        print(dic['column'])
        for i in dic['column']:
            if i.name in dic['updateColumn']:
                print(i.name)
        dic['status'] = "update"
        return render(request, 'writeArticle.html', dic)
        # return HttpResponse(column_name)
    elif request.method == "POST":
        # 当请求的方式为POST的时候，是要更新当前文章的内容
        title = request.POST['title']
        introduction = request.POST['introduction']
        column = request.POST['column']
        comment_status = request.POST['commentStatus']
        public_status = request.POST['publicStatus']
        url = request.POST['url']
        content = request.POST['content']

        markdown = request.POST['markdown']
        if comment_status == "true":
            comment_status = True
        elif comment_status == "false":
            comment_status = False
        if public_status == "true":
            public_status = True
        elif public_status == "false":
            public_status = False
        try:
            sql = models.Article.objects.get(title=title)
            sql.title = title
            sql.introduction = introduction
            # sql.column = column # 需要修复,因为数据库已经改为多对多模式，所以不能这样添加数据
            column = column.split(',')[0:-1]
            # 获取对应文章的所有分类
            old_column = sql.column.all()
            old_column_list = []
            # 将文字的所有分类的id提取出来
            for i in old_column:
                old_column_list.append(str(i.columnId))
            # 将更新后的文章id与旧的进行比较，如果有新添加的，就更新
            for i in range(len(column)):
                if column[i] not in old_column_list:
                    sql.column.add(column_models.Columns.objects.get(columnId=i))
            sql.commentStatus = comment_status
            sql.publicStatus = public_status
            sql.url = url
            sql.content = content
            sql.markdown = markdown
            sql.save()
            return HttpResponse("更新成功")
        except Exception as e:
            print(e)
            return HttpResponse('更新失败')


@csrf_protect
def remove_article_recycle(request):
    # 将文章移动到回收站的逻辑操作
    title = request.POST['title']
    result = {"status": 0, "message": "移动错误", "id": 0}
    if title:
        try:
            article = models.Article.objects.get(title=title)
            article.available = False
            result['status'] = 1
            result['message'] = '移动成功'
            result['id'] = article.id
            article.save()
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        result['message'] = '没有获取到标题'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_protect
def recycle_article(request):
    """
    返回回收站列表的方法
    :param request:
    :return:
    """
    articles = models.Article.objects.filter(available=0)
    dic = {"article": []}
    for article in articles:
        dic['article'].append({'id': article.id, 'title': article.title,
                               'author': article.author, 'image': article.image,
                               'content': article.content, 'time': article.time,
                               'columns': article.column, 'introduction': article.introduction,
                               'publicStatus': article.publicStatus, 'commentStatus': article.commentStatus,
                               'commentId': article.commentId, 'url': article.url, 'column': article.column.all(),
                               'available': article.available})
    return render(request, 'articleList.html', dic)


@csrf_protect
def delete_article(request):
    title = request.POST['title']
    result = {"status": 0, "message": "删除错误", "id": 0}
    if title:
        try:
            article = models.Article.objects.get(title=title)
            result['status'] = 1
            result['message'] = '删除成功'
            result['id'] = article.id
            article.delete()
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        result['message'] = '没有获取到标题'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_protect
def recover_article(request):
    """
    将文章从回收站恢复的方法
    :param request:
    :return:
    """
    title = request.POST['title']
    result = {"status": 0, "message": "恢复错误", "id": 0}
    if title:
        try:
            article = models.Article.objects.get(title=title)
            article.available = 1
            result['status'] = 1
            result['message'] = '恢复成功'
            result['id'] = article.id
            article.save()
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        result['message'] = '没有获取到标题'
        return HttpResponse(json.dumps(result), content_type='application/json')
