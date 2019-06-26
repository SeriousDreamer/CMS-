from django.shortcuts import render
from django.http import HttpResponse
from . import models


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
