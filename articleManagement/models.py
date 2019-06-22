from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True)  # 文章ID
    title = models.CharField(max_length=50)  # 文章标题
    author = models.CharField(max_length=50)  # 作者
    image = models.ImageField(upload_to="static/images", default='null')  # 特色图片路径
    content = models.TextField()  # 文章内容
    time = models.DateTimeField(auto_now_add=True)  # 文章发布时间
    column = models.IntegerField(default=1)  # 栏目
    introduction = models.CharField(max_length=500)  # 文章摘要
    publicStatus = models.CharField(max_length=50)  # 发布状态
    commentStatus = models.BooleanField()  # 是否可以评论
    commentId = models.IntegerField()  # 评论ID
    url = models.TextField()  # 文章url

    class Meta:
        db_table = 'Article'
