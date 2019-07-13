from django.db import models
from manager import models as ma_models


# Create your models here.
class Media(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="图片标题")
    author = models.ForeignKey(ma_models.Manager, verbose_name="图片作者")
    width = models.FloatField(verbose_name="宽度")
    height = models.FloatField(verbose_name="高度")
    date = models.DateTimeField(auto_now_add=True, verbose_name="图片上传时间")
    url = models.FileField(verbose_name="图片url", upload_to="%Y/%m/%d")

    class Meta:
        db_table = "Media"
