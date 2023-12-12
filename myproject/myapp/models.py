from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    # 定义 Student 模型的字段
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    # 其他字段...

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
