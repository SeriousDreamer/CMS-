from django.shortcuts import render
from django.http import HttpResponse,Http404
from . import models
from column import models as column_models
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def show_index(request):
    """
    返回文章列表视图函数
    :param request:
    :return:
    """
    articles = models.Article.objects.all()
    dic = {"article": []}
    for article in articles:
        dic['article'].append({'id': article.id, 'title': article.title,
                               'author': article.author, 'image': article.image,
                               'content': article.content, 'time': article.time,
                               'column': article.column, 'introduction': article.introduction,
                               'publicStatus': article.publicStatus, 'commentStatus': article.commentStatus,
                               'commentId': article.commentId, 'url': article.url})
    return render(request, 'articleList.html', dic)


@csrf_protect
def write_article(request):
    """
    处理写文章逻辑
    :param request:
    :return:
    """
    if request.method == "GET":
        all_column = column_models.Columns.objects.all()
        articles = models.Article.objects.order_by('-id')
        id_article = 0
        for article in articles:
            id_article = article.id
            break
        id_article += 1
        dic = {'column':[],'url':"127.0.0.1:8000/article/%s.html" %id_article}
        for i in all_column:
            dic['column'].append({"columnId":i.columnId,"parent":i.parent,"name":i.name})
        return render(request, 'writeArticle.html',dic)
    elif request.method == "POST":
        result = request.POST
        title = result['title']
        author = request.COOKIES.get('uname')
        content = result['content']
        column = result['column']
        introduction = result['introduction']
        publicStatus = result['publicStatus']
        commentStatus = result['commentStatus']
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
        if commentStatus == "true":
            commentStatus = True
        elif commentStatus == "false":
            commentStatus = False
        dic = {
            'title': title, 'author': author,
            'content': content, 'column': column,
            'introduction': introduction, "publicStatus": publicStatus,
            "commentStatus": commentStatus, 'url': url
        }
        try:
            article = models.Article(**dic)
            article.save()
        except Exception as e:
            print(e)
            return HttpResponse("发布失败")
        return HttpResponse("发布成功")


@csrf_protect
def update_article(request):
    url = request.POST['url']
    try:
        article = models.Article.objects.filter(url=url)
    except Exception as e:
        print(e)
        return HttpResponse("查找失败")
    column = article[0].column
    column = column.split(',')
    column_name = []
    try:
        for i in column:
            if i:
                column_name.append(column_models.Columns.objects.filter(columnId=int(i))[0].name)
        all_column = column_models.Columns.objects.all()
    except Exception as e:
        print(e)
        return Http404
    dic = {
        "title": article[0].title,
        "author": article[0].author,
        "content": article[0].content,
        "updateColumn": column_name,
        "introduction": article[0].introduction,
        "publicStatus": article[0].publicStatus,
        "commentStatus": article[0].commentStatus,
        "url": article[0].url,
        'column':[]
    }
    for i in all_column:
        dic['column'].append({"columnId": i.columnId, "parent": i.parent, "name": i.name})

    print(dic)
    return render(request,'writeArticle.html',dic)
