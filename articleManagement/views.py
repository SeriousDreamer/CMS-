from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import models
from column import models as column_models
from django.views.decorators.csrf import csrf_protect
from column import views as co_views
from column.views import select_column


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
                               'columns': article.column, 'introduction': article.introduction,
                               'publicStatus': article.publicStatus, 'commentStatus': article.commentStatus,
                               'commentId': article.commentId, 'url': article.url, 'column': article.column.all()})
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
        all_column = column_models.Columns.objects.all()
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
        if publicStatus == "true":
            publicStatus = True
        elif publicStatus == "false":
            publicStatus = False
        dic = {
            'title': title, 'author': author,
            'content': content,
            'introduction': introduction, "publicStatus": publicStatus,
            "commentStatus": commentStatus, 'url': url, 'markdown': markdown
        }
        column = column.split(',')[0:-1]
        art = column_models.Columns.objects.get(columnId=int(column[0]))
        art = art.article_set.create(**dic)
        for i in range(1, len(column)):
            column_models.Columns.objects.get(columnId=int(column[i])).article_set.add(art)

        # try:
        #     article = models.Article(**dic)
        #     article.save()
        # except Exception as e:
        #     print(e)
        #     return HttpResponse("发布失败")
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
        commentStatus = request.POST['commentStatus']
        publicStatus = request.POST['publicStatus']
        url = request.POST['url']
        content = request.POST['content']
        markdown = request.POST['markdown']
        if commentStatus == "true":
            commentStatus = True
        elif commentStatus == "false":
            commentStatus = False
        if publicStatus == "true":
            publicStatus = True
        elif publicStatus == "false":
            publicStatus = False
        try:
            sql = models.Article.objects.get(title=title)
            sql.title = title
            sql.introduction = introduction
            sql.column = column
            sql.commentStatus = commentStatus
            sql.publicStatus = publicStatus
            sql.url = url
            sql.content = content
            sql.markdown = markdown
            sql.save()
            return HttpResponse("更新成功")
        except Exception as e:
            print(e)
            return HttpResponse('更新失败')
