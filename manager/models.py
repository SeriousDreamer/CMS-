from django.db import models


# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    permission = models.IntegerField(default=0)
    date = models.DateTimeField()

    class Meta:
        db_table = "Manager"
