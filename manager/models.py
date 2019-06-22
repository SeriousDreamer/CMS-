from django.db import models


# Create your models here.
class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    permission = models.IntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
        result = {'name': self.name, 'password': self.password, 'permission': self.permission, 'date': self.date}
        return result
