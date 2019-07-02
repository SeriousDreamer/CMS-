from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True, )  # 文章ID
    title = models.CharField(verbose_name="文章标题", max_length=50, unique=True)  # 文章标题
    author = models.CharField(verbose_name="作者", max_length=50)  # 作者
    image = models.ImageField(verbose_name="特色图片", upload_to="static/images", default='null')  # 特色图片路径
    content = models.TextField(verbose_name="文章内容", )  # 文章内容
    markdown = models.TextField(verbose_name="markdown", default="")  # markdown内容
    time = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)  # 文章发布时间
    column = models.CharField(max_length=50, verbose_name="分类", default=1)  # 栏目，需要外键
    introduction = models.CharField(verbose_name="摘要", max_length=500)  # 文章摘要
    publicStatus = models.CharField(verbose_name="发布状态", max_length=50)  # 发布状态
    commentStatus = models.BooleanField(verbose_name="是否开启评论", )  # 是否可以评论
    commentId = models.IntegerField(verbose_name="评论", default=0)  # 评论ID
    url = models.TextField(verbose_name="文章url", )  # 文章url

    class Meta:
        db_table = 'Article'
